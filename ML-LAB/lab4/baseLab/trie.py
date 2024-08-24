import mat73
from scipy.spatial.distance import cdist
import numpy as np
import config


def k_means(data_x, k, init='k-means++'):
    """
    实现K_means++算法
    :param data_x:数据，{个数*特征数}
    :param k: 聚类中心个数
    :param init:确定初始中心点的方法
    """
    '''将data中心化以得到更准确的结果'''
    data_mean = data_x.mean(axis=0, keepdims=True)
    data_x = data_x - data_mean
    '''初始化中心点'''
    n_samples, n_features = data_x.shape
    centers = np.empty((k, n_features), dtype=data_x.dtype)
    if init == 'k-means++':
        center_id = np.random.mtrand.choice(n_samples)
        centers[0] = data_x[center_id]
        # 计算距离
        closest_dist = cdist(centers[[0]], data_x)
        # 其余中心
        n_local_trials = 2 + int(np.log(k))
        for i in range(1, k):
            center_ids = np.random.mtrand.choice(n_samples, size=n_local_trials, replace=False)
            closest_dists = cdist(data_x[center_ids], data_x)
            np.minimum(closest_dist, closest_dists, out=closest_dists)
            dists_cost = closest_dists.sum(axis=1)
            # 选择总距离最小的点
            best_c = np.argmin(dists_cost)
            closest_dist = closest_dists[best_c]
            best_id = center_ids[best_c]
            centers[i] = data_x[best_id]
    elif init == 'random':
        # TODO 随机选取k个中心点
        centers = data_x[np.random.randint(0, n_samples, k)]
    else:
        raise ValueError('init must be "k-means++" or "random"')
    '''K_means迭代计算中心'''
    while True:
        # TODO 完成计算部分
        closest_dist = cdist(data_x, centers)
        closest_id = np.argmin(closest_dist, axis=1)
        # 计算新的中心点
        new_centers = np.zeros_like(centers)
        for i in range(k):
            new_centers[i] = np.mean(data_x[closest_id == i], axis=0)
        # 判断收敛
        if np.allclose(centers, new_centers):
            break
        # 更新中心点
        centers = new_centers
    '''加上均值'''
    centers += data_mean
    return centers


def trie_learn(data, centers):
    """
    计算特征
    :param data: 数据
    :param centers: 聚类中心
    """
    nlearn, n_features = data.shape
    k, c_features = centers.shape
    D = k * 128
    step = 50000 * int(64 / k)
    '''求取特征均值x_mean'''
    # TODO:下面为计算，核心思想为小批量相加
    x = np.zeros((D, nlearn), dtype=np.float16)
    for i in range(0, nlearn, step):
        for j in range(0, k):
            next = min(nlearn, i + step)
            # 小批量计算的核心代码
            x[j * 128:(j + 1) * 128, i:next] = ((x[j * 128:(j + 1) * 128, i:next].T + data[i:next, :] - centers[j,
                                                                                                        :]) / np.linalg.norm(
                x[j * 128:(j + 1) * 128, i:next].T + data[i:next, :] - centers[j, :], 2, axis=0)).T
            print("the i={}&j={} is OK".format(i, j))
    x_sum = np.array([x.sum(axis=1)], dtype=np.float16).T
    x_mean = x_sum / nlearn
    print("x_mean finish")

    # TODO:下面代码保证我的计算机可以计算，内存问题
    cov_d = np.zeros((D, D), dtype=np.float16)
    for i in range(0, nlearn, step):
        next = min(nlearn, i + step)
        cov_d += (x[:, i:next] - x_mean).T.dot(x[:, i:next] - x_mean)
    print("cov_d finish")

    '''计算特征值和特征向量'''
    # TODO:下面代码保证我的计算机可以计算，内存问题
    cov_d = cov_d.astype(np.float32)
    eigval, eigvec = np.linalg.eig(cov_d)
    print("eigval, eigvec finish")
    idx = eigval.argsort()[::-1]  # descending sort
    eigval = eigval[idx]
    eigvec = eigvec[:, idx]
    return x_mean, eigvec, eigval


def run_trie(kc, init, mode=0):
    """程序起点"""
    '''加载Flickr60k数据'''
    # TODO:修改数据类型，减少内存占比
    v_train = mat73.loadmat('../data/vtrain.mat')['vtrain'].T.astype(np.float16)  # 5000404*128
    print('load Flickr60k train data')

    '''使用K-means聚类算法，得到对应的k个聚类中心，表现形式为k*128维向量'''
    if mode == 0:
        # 第一次做，还没计算出来，直接使用下面的代码
        c = k_means(v_train, kc, init)
        # 保存计算出的聚类中心
        np.savetxt('./temp/center_{}.csv'.format(kc), c)
    else:
        # 节省时间时可以注释掉k_means计算，直接加载计算好的中心
        c = np.loadtxt('./temp/center_{}.csv'.format(kc))
    print('K-means finish')

    '''计算三角化嵌入所需参数'''
    x_mean, eigvec, eigval = trie_learn(v_train, c)
    print('trie finish')

    '''计算投影矩阵'''
    eigval[-128:] = eigval[-129]
    p_emb = np.diag(np.power(eigval, -0.5)) @ eigvec.T

    '''保存'''
    np.savetxt('./temp/eigval_{}.csv'.format(kc), eigval)
    np.savetxt('./temp/eigvec_{}.csv'.format(kc), eigvec)
    np.savetxt('./temp/x_mean_{}.csv'.format(kc), x_mean)
    np.savetxt('./temp/p_emb_{}.csv'.format(kc), p_emb)


if __name__ == '__main__':
    init = config.init
    k = config.k
    run_trie(k, init, mode=config.mode)
