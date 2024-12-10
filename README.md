# **Image Classification with DeepLab and PyTorch**

This project showcases a custom implementation of **image classification** using PyTorch. The repository includes a **DeepLab Jupyter Notebook** for experimentation and visualization, along with a standalone Python script for the neural network implementation. The primary focus is on training and evaluating models for effective image classification.

---

## **Key Features**

- **DeepLab.ipynb**: A Jupyter Notebook for interactive exploration and fine-tuning of models.
- **Neural-Network.py**: A Python script implementing a custom Convolutional Neural Network (CNN) for image classification.
- **Dataset Handling**: Supports custom datasets with dynamic transformations and label mappings.
- **Cross-Validation**: Integrates Stratified K-Fold for robust evaluation.
- **Result Export**: Saves predictions in CSV format for easy analysis.

---

## **Table of Contents**

- [Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Jupyter Notebook](#running-the-jupyter-notebook)
  - [Running the Python Script](#running-the-python-script)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## **Installation**

### **Prerequisites**
- Python 3.7 or higher
- Jupyter Notebook or Google Colab (for DeepLab.ipynb)
- Libraries: PyTorch, Torchvision, Pandas, OpenPyXL

### **Setup Instructions**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/T-Stewart25/image-classification.git
   cd image-classification
   ```

2. **Install Dependencies**
   ```bash
   pip install torch torchvision pandas openpyxl
   ```

---

## **Usage**

### **Running the Jupyter Notebook**
- Open `DeepLab.ipynb` in Jupyter Notebook or Google Colab.
- Follow the step-by-step instructions to:
  - Load and preprocess datasets.
  - Train the model using a CNN.
  - Evaluate performance metrics such as accuracy and mean squared error.

### **Running the Python Script**
- Execute the `Neural-Network.py` script for a streamlined workflow:
   ```bash
   python Neural-Network.py
   ```
- The script handles dataset loading, training, and validation automatically.

---

## **Project Structure**

```
image-classification/
├── .ipynb_checkpoints/   # Jupyter Notebook checkpoints
├── DeepLab.ipynb         # Jupyter Notebook for model experimentation
├── Neural-Network.py     # Standalone Python script for training and evaluation
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
- **Personal Portfolio**: [Portfolio](https://thomasstewartpersonal.com)
