import numpy as np

import embedding
import eval
import trie
import config

if __name__ == '__main__':
    '''超参数'''
    np.seterr(divide='ignore', invalid='ignore')
    k = config.k  # 聚类中心个数
    init = config.init

    '''处理Flickr60k数据并得到聚类中心和对应的特征值'''
    trie.run_trie(k, init)
    print("begin embedding.run_embedding")

    '''处理Holidays数据并进行特征表示'''
    embedding.run_embedding(k)

    '''计算mAP'''
    eval.mAP(k)
