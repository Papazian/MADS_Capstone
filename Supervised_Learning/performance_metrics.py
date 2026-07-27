import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay, average_precision_score

def evaluate_classifier(model, y_test, y_pred, y_probs):
    """
    Print performance metrics to evaluate a sklearn classifier model

    Parameters:
        model: sklearn classifier model
        y_test: target variable from the holdout validation dataset from train_test_split()
        y_pred: predict binary class (0 or 1)
        y_probs: Predict raw probabilities
    """

    print(f"Accuracy Score: {accuracy_score(y_test, y_pred):.2f}")

    print(f"\nAverage Precision Score (summarizes the Precision-Recall curve): {average_precision_score(y_test, y_probs):.2f}\n")

    print("Classification Report:")
    
    print(classification_report(y_test, y_pred))

    print("Confusion Matrix:")

    cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    disp.plot()
    plt.show()