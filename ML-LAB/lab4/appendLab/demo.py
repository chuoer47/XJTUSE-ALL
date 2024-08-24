import mat73
import numpy as np
from sklearn import metrics
from sklearn.cluster import MiniBatchKMeans
from sklearn.decomposition import PCA

if __name__ == '__main__':
    v_train = mat73.loadmat('../data/vtrain.mat')['vtrain'].T.astype(np.float16)  # 5000404*128
    print("v_train finish")
    k = 2
    print("k is {}".format(k))
    minibatchkmeans = MiniBatchKMeans(n_clusters=k, batch_size=50)
    pca = PCA(n_components=0.9)  # 保留90%能量
    v_train_pca = pca.fit_transform(v_train)
    print("pca finish")
    # 获得pca形状
    print("pca shape:")
    print(v_train_pca.shape)
    # 训练模型
    minibatchkmeans.fit(v_train_pca)

    print("minibatchkmeans finish:")
    y_predict = minibatchkmeans.predict(v_train_pca)

    print("calinski_harabasz_score:")
    print(metrics.calinski_harabasz_score(v_train_pca, y_predict))

    print("cluster_centers_:")
    print(minibatchkmeans.cluster_centers_)

    print("silhouette_score:")
    print(metrics.silhouette_score(v_train_pca, y_predict))
