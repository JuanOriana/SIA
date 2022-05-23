import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

from TP4.parse_csv import getInputsStandard

if __name__ == "__main__":
    pca = PCA()
    data_standarized, countries, data, labels = getInputsStandard('europe.csv')
    components = pca.fit_transform(data_standarized)

    print(components[:, 0:2][:,0])

    principal_df = pd.DataFrame(data=components
                               , columns=['principal component ' + str(i) for i in range(7)])
    print(principal_df)
    np.set_printoptions(precision=6,suppress=True)
    print(pca.components_)
    accum_variance = 0

    for idx,variance in enumerate(pca.explained_variance_ratio_):
        accum_variance += variance
        print('principal component ' + str(idx) + ': '  + str(accum_variance))

    # BIPLOT
    x_country = principal_df.values[:, 0]
    y_country = principal_df.values[:, 1]
    x_scale = 1.0 / (x_country.max() - x_country.min())
    y_scale = 1.0 / (y_country.max() - y_country.min())
    plt.scatter(components[:, 0:2][:,0] * x_scale, components[:, 0:2][:,1] * y_scale, s=3)

    for i in range(np.transpose(pca.components_[0:2, :]).shape[0]):
        plt.arrow(0, 0, np.transpose(pca.components_[0:2, :])[i, 0], np.transpose(pca.components_[0:2, :])[i, 1], color='r', alpha=0.5)
        plt.text(np.transpose(pca.components_[0:2, :])[i, 0] * 1.15, np.transpose(pca.components_[0:2, :])[i, 1] * 1.15, labels[i], color='g', ha='center', va='center')
    for i in range(len(components[:, 0:2][:,0])):
        plt.text(components[:, 0:2][:,0][i] * x_scale, components[:, 0:2][:,1][i] * (y_scale + 0.015), countries[i], color='b', ha='center', va='center', fontsize=4)

    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.grid()
    plt.show()




