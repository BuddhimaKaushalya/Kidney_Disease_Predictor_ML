Overview
This project is a Chronic Kidney Disease (CKD) predictor implemented using Machine Learning. The model utilizes a dataset from Kaggle to classify whether a person has CKD based on medical attributes.

Models Used
The model evaluation is done using cross-validation, and three classifiers are trained:

RandomForestClassifier (Mean Accuracy: 99.27%)
GradientBoostingClassifier (Mean Accuracy: 96.36%)
MLPClassifier (Neural Network) (Mean Accuracy: 98.18%)
An ensemble approach (majority voting) is used to improve prediction stability.

Implementation Details
Dataset: Kaggle CKD dataset
Training Approach:
Individual models trained using cross-validation
Evaluated based on accuracy and standard deviation
An ensemble model is built using majority voting
