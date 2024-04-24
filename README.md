# Stroke Prediction Mini Project

## About
SC1015 Mini-Project related to patients and their background information that serves to show how certain aspects of their lives can contribute to getting a stroke. It makes use of [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) which contains over 5000 rows of patients' attributes like age, smoking history, hypertension, etc. 

## Problem Definition
- To identify the most significant risk factors that contribute to strokes
- To predict whether a patient is at risk of having a stroke or not based on their personal health and other characteristics

## Difficulty encountered
- Small sample size with imbalance amount of patients with stroke (only 249 out of the 5110 patient have stroke)
- Notebook have conflict between different computer as the version of certain python library might be different

## Conclusion
Our dataset shows that hypertension and heart disease are the most significant risk factors for stroke. Among patients with hypertension, 17% had a stroke, compared to only 4% of those without hypertension. Similarly, among patients with heart disease, 17% had a stroke, compared to 4% without heart disease. This indicates a strong correlation of 13% (we indicate it as high as our stroke data is highly imbalance) between both hypertension and heart disease and the occurrence of stroke. 

We've chosen Random Forest classification over Decision Tree because it's more robust to noisy data and faster to train due to parallelization. To tackle imbalanced data, we're using oversampling, which sacrifices overall accuracy but significantly improves prediction for positive stroke. We're also fine-tuning hyperparameters to boost accuracy further.

  

## Contributors
- Lim Wei Yang, Justin: Data extraction & preparation, Exploratory Data Analysis (Numerical), Youtube Video 
- Li ZhangYi: Waffle Plot, Machine Learning with oversampling, hyperparameter tuning and random forest classification
- Qiu YiBin: Discussion on what Machine Learning techique to use, Exploratory Data Analysis (Categorical), ReadMe Report

## Reference
- https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset