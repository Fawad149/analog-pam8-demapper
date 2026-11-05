import numpy as np

# PAM-8 points: -7d, -5d, ..., +7d
D = 1 / np.sqrt(42)
X = D * np.array([-7, -5, -3, -1, 1, 3, 5, 7])

# Gray labels (b1, b2, b3)
LABELS = np.array([
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 1],
    [0, 1, 0],
    [1, 1, 0],
    [1, 1, 1],
    [1, 0, 1],
    [1, 0, 0],
])

ALPHA = 0.04 / D
BETA = 0.32