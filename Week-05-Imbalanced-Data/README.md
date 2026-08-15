# Handling Imbalanced & Messy Real-World Data

## Dataset

Credit Card Fraud Detection dataset from Kaggle.

## Objective

The goal of this task is to understand class imbalance and evaluate
different approaches for improving fraud detection.

## Approach

- Checked the target class distribution
- Visualized class imbalance
- Trained a baseline Logistic Regression model
- Applied SMOTE to the training data
- Compared Precision, Recall, and F1-Score
- Evaluated the effect of balancing on fraud detection

## Results

| Model | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Baseline Logistic Regression | 82.67% | 63.27% | 71.68% |
| Logistic Regression + SMOTE | 5.78% | 91.84% | 10.88% |

## Conclusion

SMOTE substantially improved recall but caused a large decrease in
precision. This demonstrates the trade-off involved in handling highly
imbalanced fraud detection data.

Accuracy alone can be misleading because a model can achieve high
accuracy by predicting the majority legitimate class while failing to
identify fraudulent transactions.