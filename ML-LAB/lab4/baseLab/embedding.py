import mat73
import numpy as np

import config


def desc_postprocess(x, desc_mean):
    """
    数据预处理
    """
    # 取平方根，中心化
    x = np.sqrt(x) - desc_mean
    # L2正则化
    x /= np.linalg.norm(x, axis=1, keepdims=True)
    return x


def trie_suma(X, C, Xmean):
    """
    三角化嵌入函数

    输入 X.shape = (128, n), 输出 Y.shape = (128*k, 1)
    """
    n,nlearn = X.shape
    k = C.shape[0]
    D = k * 128
    d = 128
    Y = np.zeros(D)
    X = X.T
    for j in range(k):
        Y[j * d: j * d + d] = np.sum((X - C[j]) / np.linalg.norm(X - C[j], axis=1).reshape(n, 1), axis=0)
    Y -= n * Xmean
    return Y


def run_embedding(kc):
    """程序起点"""
    '''加载Holidays数据集和其余数据'''
    x_data = mat73.loadmat('../data/X.mat')['X'].T
    cndes = mat73.loadmat('../data/cndes.mat')['cndes'].astype('int')
    desc_mean = mat73.loadmat('../data/desc_mean.mat')['desc_mean']
    # 上一步训练好的数据
    centers = np.loadtxt('./temp/center_{}.csv'.format(kc))
    x_mean = np.loadtxt('./temp/x_mean_{}.csv'.format(kc))
    p_emb = np.loadtxt('./temp/p_emb_{}.csv'.format(kc))
    print('load finish')

    '''开始计算'''
    n = cndes.shape[0] - 1
    n_samples, n_features = x_data.shape
    psi = np.empty((n, kc * n_features), dtype=np.float32)
    # 逐图片计算
    print('train start')
    for i in range(n):
        # 得到第i张图片的sift特征
        x = x_data[cndes[i]:cndes[i + 1]]
        # 进行预处理
        x = desc_postprocess(x, desc_mean)
        # 三角化嵌入
        psi[i] = trie_suma(x, centers, x_mean)
    psi = psi @ p_emb.T

    '''保存'''
    np.savetxt('./temp/psi_{}.csv'.format(kc), psi)


if __name__ == '__main__':
    run_embedding(config.k)
