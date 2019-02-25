import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean, pdist, squareform
from matplotlib import pyplot as plt
from sklearn import manifold

data = pd.read_excel("matrix.xlSx")
def similarity_func(u, v):
	return 1/(1+euclidean(u,v))

dists = pdist(data[data.columns[1:]], similarity_func)
similarities = pd.DataFrame(squareform(dists))

mds = manifold.MDS(n_components=2, max_iter=200, eps=1e-9, dissimilarity="precomputed", n_jobs=1)
pos = mds.fit(similarities).embedding_

plt.scatter(pos[:, 0], pos[:, 1], color='turquoise', s=111, lw=0, label='MDS')
plt.savefig('plot.png')
plt.close()