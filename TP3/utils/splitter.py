import numpy as np


def split_train_and_learn(raw_in:np.ndarray,raw_out:np.ndarray, percentage:float):
    train_idx = np.random.choice(len(raw_in), int(percentage*len(raw_in)),replace=False)
    Xtrain = raw_in[train_idx]
    Ytrain = raw_out[train_idx]

    test_idx = [idx for idx in range(len(raw_in)) if idx not in train_idx]
    Xtest = raw_in[test_idx]
    Ytest = raw_out[test_idx]

    return Xtrain,Ytrain,Xtest,Ytest