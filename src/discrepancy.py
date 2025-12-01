import numpy as np

def compute_discrepancy(system1, system2):
    """
    Computes discrepancy between a system and its involuted image.
    This is used as the integrability criterion in the article.
    """
    return sum(abs(system1[key] - system2[key]) for key in system1)
