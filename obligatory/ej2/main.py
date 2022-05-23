import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

from TP4.parse_csv import getInputsStandard

if __name__ == "__main__":
    pca = PCA()
    components = pca.fit_transform(getInputsStandard('europe.csv')[0])
    principal_df = pd.DataFrame(data=components
                               , columns=['principal component ' + str(i) for i in range(7)])
    print(principal_df)
    np.set_printoptions(precision=6,suppress=True)
    print(pca.components_)
    accum_variance = 0
    for idx,variance in enumerate(pca.explained_variance_ratio_):
        accum_variance += variance
        print('principal component ' + str(idx) + ': '  + str(accum_variance))
