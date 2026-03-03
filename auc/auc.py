import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # in here 
    # return np.trapezoid(fpr,tpr,dx=fpr) this fails due to order I guess
    return np.trapezoid(tpr,fpr)