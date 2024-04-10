# -*- coding: utf-8 -*-
"""Answer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kkIawGUvLIr8gv3N5yPT9vyIpcheGp3U
"""

!pip3 install torch torchaudio torchvision torchtext torchdata
!pip3 install pandas
!pip3 install openpyxl

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, Dataset, SubsetRandomSampler
import os
from PIL import Image
import pandas as pd
from google.colab import drive
import torch.nn.functional as F
from sklearn.model_selection import train_test_split, KFold, StratifiedKFold
import numpy as np





#Importing necessary libraries

from google.colab import drive
drive.mount('/content/drive')

class ImageDataset(Dataset):
    def __init__(self, root_dir, labels_file=None, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        if labels_file is not None:
            self.labels_df = pd.read_excel(labels_file)
        else:
            self.labels_df = None

    def __len__(self):
        if self.labels_df is not None:
            return len(self.labels_df)
        else:
            # Handle the case when labels_file is None (e.g., validation set)
            return len(os.listdir(self.root_dir))

    def __getitem__(self, idx):
      img_name = os.listdir(self.root_dir)[idx]
      img_path = os.path.join(self.root_dir, img_name)
      image = Image.open(img_path).convert('RGB')
      if self.transform:
          image = self.transform(image)

      if self.labels_df is not None:
          label_str = str(self.labels_df.iloc[idx, 3])  # Convert label to string
          label_mapping = {
              "Select": 0,
              "Low Choice": 1,
              "Upper 2/3 Choice": 2,
              "Prime": 3,
          }
          try:
              label = label_mapping[label_str]
          except KeyError:
              print("Encountered KeyError for label:", label_str)
              raise
      else:
          # For validation set where labels are not provided
          label = None

      return image, label

import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self, img_size=(300, 245)):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=2, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.dropout1 = nn.Dropout(p=0.25)
        dummy_input = torch.zeros(1, 3, *img_size)
        dummy_output = self.pool(nn.ReLU()(self.conv1(dummy_input)))
        linear_input_size = dummy_output.view(-1).size(0)

        self.fc1 = nn.Linear(linear_input_size, 520)
        self.fc3 = nn.Linear(520, 4)  # Output size is 4 for 4 classes

    def forward(self, x):
        x = self.pool(nn.ReLU()(self.conv1(x)))
        x = torch.flatten(x, 1)
        x = nn.ReLU()(self.fc1(x))
        x = self.fc3(x)
        x = self.dropout1(x)
        #x = F.softmax(x, dim=1)  # Softmax activation
        return x

# Define the paths
root_dir = "/content/drive/MyDrive/Training"
labels_file = "/content/drive/MyDrive/TrainingLabels.xlsx"

# Define the transformations
transform = transforms.Compose([
    transforms.Resize((300, 245)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

# Load dataset
dataset = ImageDataset(root_dir, labels_file, transform=transform)

# Define k-fold cross-validator
k_folds = 4 #best result with 4
skf = StratifiedKFold(n_splits=k_folds, shuffle=True)

# Training and testing loop
model = Net()
accuracies = []
mse_values = []

for fold, (train_indices, test_indices) in enumerate(skf.split(dataset, dataset.labels_df.iloc[:, 3])):
    print(f'Fold {fold + 1}/{k_folds}')

    train_sampler = torch.utils.data.SubsetRandomSampler(train_indices)
    test_sampler = torch.utils.data.SubsetRandomSampler(test_indices)

    train_loader = DataLoader(dataset, batch_size=32, sampler=train_sampler)
    test_loader = DataLoader(dataset, batch_size=32, sampler=test_sampler)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Training loop
    for epoch in range(3):  # Best result with 3
        running_loss = 0.0
        for i, data in enumerate(train_loader, 0):
            inputs, labels = data

            optimizer.zero_grad()

            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            if i % 10 == 9:  # Print every 10 mini-batches
                print('[%d, %5d] loss: %.3f' %
                      (epoch + 1, i + 1, running_loss / 10))
                running_loss = 0.0

    print('Finished Training for Fold', fold + 1)

    # Testing loop
    correct = 0
    total = 0
    mse_fold = 0
    with torch.no_grad():
        for data in test_loader:
            images, labels = data
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

            # Calculate MSE
            # Calculate MSE
            mse = ((predicted.float() - labels.float()) ** 2).mean()

            mse_fold += mse.item()

    accuracy = 100 * correct / total
    accuracies.append(accuracy)

    # Calculate mean squared error for the fold
    mse_fold /= len(test_loader)
    mse_values.append(mse_fold)

    print('Accuracy on Test set for Fold', fold + 1, ': %.2f %%' % accuracy)
    print('Mean Squared Error on Test set for Fold', fold + 1, ': %.2f' % mse_fold)

# Calculate mean and standard deviation of accuracy and MSE
mean_accuracy = np.mean(accuracies)
mean_mse = np.mean(mse_values)
std_accuracy = np.std(accuracies)
std_mse = np.std(mse_values)

print('Overall Mean Accuracy: %.2f %%' % mean_accuracy)
print('Overall Standard Deviation of Accuracy: %.2f %%' % std_accuracy)
print('Overall Mean Squared Error: %.2f' % mean_mse)
print('Overall Standard Deviation of MSE: %.2f' % std_mse)

# Define the validation directory
val_dir = "/content/drive/MyDrive/Validation"


# Define the model and label mapping
label_mapping = {
    "Select": 1,
    "Low Choice": 2,
    "Upper 2/3 Choice": 3,
    "Prime": 4,
}

predicted_counts = {i: 0 for i, label in enumerate(label_mapping)}

# Iterate over the files in the validation directory
total_predictions = 0
with torch.no_grad():
    for img_name in os.listdir(val_dir):
        img_path = os.path.join(val_dir, img_name)
        image = Image.open(img_path).convert('RGB')
        image = transform(image).unsqueeze(0)  # Add batch dimension

        outputs = model(image)
        _, predicted = torch.max(outputs.data, 1)
        for pred in predicted:
            label = pred.item()
            predicted_counts[label] += 1
            total_predictions += 1

# Print predicted counts
print("Predicted counts:")
for label, count in predicted_counts.items():
    percentage = (count / total_predictions) * 100 if total_predictions != 0 else 0
    print(f"{label}: {count} ({percentage:.2f}%)")

# Define the validation directory
val_dir = "/content/drive/MyDrive/Validation"

# Define the model and label mapping
label_mapping = {
    1: "Select",
    2: "Low Choice",
    3: "Upper 2/3 Choice",
    4: "Prime",
}

predicted_counts = {i: 0 for i, label in enumerate(label_mapping)}
all_predictions = []  # List to store all predictions
file_predictions = {}  # Dictionary to store predictions with filenames

# Iterate over the files in the validation directory
total_predictions = 0
with torch.no_grad():
    for img_name in os.listdir(val_dir):
        img_path = os.path.join(val_dir, img_name)
        image = Image.open(img_path).convert('RGB')
        image = transform(image).unsqueeze(0)  # Add batch dimension

        outputs = model(image)
        _, predicted = torch.max(outputs.data, 1)

        for pred in predicted:
            label = pred.item()
            all_predictions.append(label)  # Store prediction
            predicted_counts[label] += 1
            total_predictions += 1
            file_predictions[img_name] = label  # Store prediction with filename

# Print predicted counts
print("Predicted counts:")
for label, count in predicted_counts.items():
    percentage = (count / total_predictions) * 100 if total_predictions != 0 else 0
    print(f"{label}: {count} ({percentage:.2f}%)")

label_mapping = {
    0: "Select",
    1: "Low Choice",
    2: "Upper 2/3 Choice",
    3: "Prime",
}
df = pd.DataFrame()

# Initialize an empty list to store DataFrames
appended_dfs = []

# Add values to the DataFrame by mapping predictions through label_mapping
for prediction in all_predictions:
    # Assuming label_mapping[prediction] returns a string
    data = pd.DataFrame([label_mapping[prediction]])
    appended_dfs.append(data)

# Concatenate the list of DataFrames with the DataFrame
df = pd.concat(appended_dfs, ignore_index=True)

# Display the DataFrame
print(df)

df.to_csv('/content/drive/MyDrive/predictions.csv', index=False)