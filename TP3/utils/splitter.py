import numpy as np


def split_train_and_learn(raw_in: np.ndarray, raw_out: np.ndarray, percentage: float):
    train_idx = np.random.choice(len(raw_in), int(percentage * len(raw_in)), replace=False)
    Xtrain = raw_in[train_idx]
    Ytrain = raw_out[train_idx]

    test_idx = [idx for idx in range(len(raw_in)) if idx not in train_idx]
    Xtest = raw_in[test_idx]
    Ytest = raw_out[test_idx]

    return Xtrain, Ytrain, Xtest, Ytest


def k_splitting(raw_in: np.ndarray, raw_out: np.ndarray, k: int):
    if k > raw_in.shape[0]:
        raise Exception
    split_size = raw_in.shape[0] // k
    indexes = np.arange(0, raw_in.shape[0], dtype=int)
    np.random.shuffle(indexes)
    train_sets_idx = []
    test_sets_idx = []
    for i in range(k):
        test = indexes[i * split_size:(i + 1) * split_size]
        before = indexes[0:i * split_size]
        after = indexes[(i + 1) * split_size :]
        train = np.concatenate((before,after))
        train_sets_idx.append(train)
        test_sets_idx.append(test)
    # Train sets X,Y  then test sets, X and Y
    return np.take(raw_in,train_sets_idx, axis=0),np.take(raw_out,train_sets_idx, axis=0), \
           np.take(raw_in,test_sets_idx, axis=0),np.take(raw_out,test_sets_idx, axis=0)
