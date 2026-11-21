# House Price Prediction – MLOps Project

## 1. Project Overview
This project demonstrates the implementation of an end-to-end MLOps lifecycle for predicting house prices using machine learning. It focuses on version control, data preparation, model development, testing, deployment planning, and continuous improvement.

## 2. Problem Statement
Estimating house prices manually can be difficult because prices depend on several factors such as location, area, number of bedrooms, and property characteristics. This project aims to build a machine learning model that predicts house prices using available property data.

## 3. Project Objectives
- Develop a machine learning model for house price prediction.
- Organize the project using a structured Git branching strategy.
- Maintain code and documentation version history.
- Test the model using automated unit tests.
- Document the complete MLOps lifecycle.

## 4. MLOps Lifecycle

### Stage 1: Data Collection
Collect house price data containing property features such as area, number of bedrooms, bathrooms, location, and price.

### Stage 2: Data Preparation
Inspect the dataset, handle missing values, remove duplicate records, identify relevant features, and prepare the data for model training.

### Stage 3: Feature Engineering
Select useful input variables and convert categorical data into a suitable numerical format. Separate input features from the target house price.

### Stage 4: Model Training
Train a Linear Regression model using the prepared dataset. Split the data into training and testing subsets to evaluate its performance.

### Stage 5: Model Evaluation
Evaluate the trained model using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared score.

### Stage 6: Model Testing
Write automated unit tests using pytest to verify data processing and model prediction functionality.

### Stage 7: Version Control
Use Git and GitHub to maintain project history. Develop features through separate branches and merge tested changes into the development branch.

### Stage 8: Deployment
The trained model can be integrated into an application or API to provide house price predictions to users.

### Stage 9: Monitoring and Maintenance
Monitor prediction performance, identify changes in incoming data, and retrain the model when necessary.

## 5. Git Branching Strategy
- main: Contains stable and released project versions.
- dev: Integrates completed features before release.
- feature/mlops-readme: Contains MLOps lifecycle documentation.
- feature/model-training: Contains model training implementation and tests.
- feature/update-author: Contains author information updates.

## 6. Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Git
- GitHub
- Pytest

## 7. Expected Outcome
The project will provide a structured and version-controlled machine learning workflow for house price prediction, demonstrating the major stages of the MLOps lifecycle.

## 8. Author
Rahul Joshi
