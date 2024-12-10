# **Image Classification with CNN and PyTorch**

This project implements a Convolutional Neural Network (CNN) for image classification using PyTorch. The dataset is processed through custom and augmented transformations to prepare for classification into multiple categories. The project demonstrates key steps, including preprocessing, k-fold cross-validation, model training, evaluation, and prediction with a clean pipeline for testing new datasets.

---

## **Key Features**

- **Custom Dataset Handling**: Includes a flexible `ImageDataset` class for loading images and optional labels.
- **Convolutional Neural Network (CNN)**: Implements a custom architecture with PyTorch for robust image classification.
- **K-Fold Cross-Validation**: Evaluates model performance across multiple folds to ensure reliability.
- **Training and Testing Pipeline**: End-to-end process for data loading, model training, and testing on validation datasets.
- **Dynamic Label Mapping**: Supports mapping categorical labels to numerical values for seamless processing.
- **Result Export**: Predictions are saved in CSV format for further analysis.

---

## **Table of Contents**

- [Features](#key-features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
  - [Data Preparation](#data-preparation)
  - [Training the Model](#training-the-model)
  - [Evaluating the Model](#evaluating-the-model)
  - [Making Predictions](#making-predictions)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## **Demo**

*Demonstration of the training process and sample predictions will be shown here.*

---

## **Installation**

### **Prerequisites**
- Python 3.7 or higher
- Google Colab (optional for cloud-based training)
- Libraries: PyTorch, Torchvision, Pandas, OpenPyXL

### **Setup Instructions**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/image-classification-cnn.git
   cd image-classification-cnn
   ```

2. **Install Dependencies**
   ```bash
   pip install torch torchvision torchaudio torchtext torchdata
   pip install pandas openpyxl
   ```

---

## **Usage**

### **Data Preparation**
- Place your training images in the `Training` folder.
- Ensure labels are provided in an Excel file named `TrainingLabels.xlsx` with the label column indexed as `3`.
- Validation images should be stored in the `Validation` folder.

### **Training the Model**
1. Configure the dataset paths and transformations:
   ```python
   root_dir = "/path/to/Training"
   labels_file = "/path/to/TrainingLabels.xlsx"
   ```
2. Run the training script. The model uses k-fold cross-validation to evaluate performance:
   ```python
   python train_model.py
   ```

### **Evaluating the Model**
- During training, validation accuracy and Mean Squared Error (MSE) are computed for each fold.
- Final performance metrics, including mean accuracy and standard deviation, are displayed after training.

### **Making Predictions**
1. Specify the directory containing the validation images:
   ```python
   val_dir = "/path/to/Validation"
   ```
2. Use the pre-trained model to generate predictions. Results are saved in a CSV file:
   ```python
   python predict.py
   ```

---

## **Project Structure**

```
image-classification-cnn/
├── train_model.py        # Script for training the CNN model
├── predict.py            # Script for generating predictions
├── dataset.py            # Custom dataset class for image loading
├── model.py              # CNN architecture definition
├── Training/             # Folder containing training images
├── Validation/           # Folder containing validation images
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── LICENSE               # License information
```

---

## **Contributing**

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request for review.

---

## **License**

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it under the terms of the license.

---

## **Contact**

- **Author**: Thomas Stewart
- **Email**: thomaslstewart1@gmail.com
- **GitHub**: [T-Stewart25](https://github.com/T-Stewart25)
