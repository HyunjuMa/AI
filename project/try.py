import numpy as np
import pandas as pd 
import seaborn as sns
import tensorflow as tf

import itertools
import os
import tflearn


from matplotlib import pyplot as plt
from sklearn.decomposition.kernel_pca import KernelPCA
from sklearn.metrics import classification_report
from sklearn.preprocessing import PolynomialFeatures

%matplotlib inline

train = pd.read_csv("../input/train.csv")
test = pd.read_csv("../input/test.csv")

submission = pd.read_csv("../input/sample_submission.csv")
submission["type"] = "Unknown"

sns.pairplot(train.drop("id",axis=1), hue="type", diag_kind="kde")

poly_features = PolynomialFeatures(interaction_only=True)

try_comb = pd.DataFrame(
    poly_features.fit_transform(train.drop(["id", "color", "type"], axis=1))[:,5:],
    columns=["boneXrotting", "boneXhair", "boneXsoul",
             "rottingXhair", "rottingXsoul", 
             "hairXsoul"]
)
try_comb["type"] = train.type

sns.pairplot(try_comb, hue="type", diag_kind="kde")