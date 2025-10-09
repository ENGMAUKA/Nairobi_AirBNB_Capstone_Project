# custom_funcs.py
import pandas as pd

def binary_mapper_occ(X):
    """Maps 't'/'f' binary features to 1/0."""
    return X.replace({'t': 1, 'f': 0})
