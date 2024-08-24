import os

import numpy as np
from matplotlib import pyplot as plt
from scipy.io import loadmat

from svm import SVM


def load(path: str, data_type: str) -> dict:
    """
    根据指定路径读取数据，并对数据进行预处理
    原始数据真值为0/1，为训练需转换为-1/1
    Args:
        path: 数据集路径
        data_type: 选择训练集还是测试集

    Returns:
        一个包含输入值和真值的字典
    """
    data = loadmat(path)
    # uint8 -> int   0/1 -> -1/1
    if data_type == 'train':
        data['X'] = data['X'].astype(np.int32)
        data['y'] = data['y'].astype(np.int32) * 2 - 1
    elif data_type == 'test':
        data['Xtest'] = data['Xtest'].astype(np.int32)
        data['ytest'] = data['ytest'].astype(np.int32) * 2 - 1
    else:
        raise ValueError('data_type value error')
    return data


def plots(i_list, fun_list, acc_list, C, T, loss_type,type="linear"):
    """
    画图并保存
    """
    plt.figure(figsize=(10, 5))
    ax1 = plt.subplot(1, 2, 1)
    ax1.plot(i_list, fun_list, 'k')
    ax1.set_xlabel('t')
    ax1.set_ylabel('f(w, b)')
    plt.title('{} C={} T={} func'.format(loss_type, C, T))
    ax2 = plt.subplot(1, 2, 2)
    ax2.plot(i_list, acc_list, 'k')
    ax2.set_xlabel('t')
    ax2.set_ylabel('acc')
    plt.title('{} C={} T={} acc'.format(loss_type, C, T))
    if not os.path.exists('../output'):
        os.makedirs('../output')
    plt.savefig('./try/{}-C={}-T={}-type={}.png'.format(loss_type,C,T,type))


if __name__ == '__main__':
    '''
    程序初始化，超参设置
    '''
    C = 0.0005  # 设置C的初始值，越大表示越偏向硬SVM算法
    T = 9000  # 迭代随机取样次数
    f = 500  # 每训练多少次计算一次目标函数的值，建议能整除T
    loss_type = 'hinge'
    # loss_type = 'exp'
    # loss_type = 'log'  # loss函数的类型
    num_features = 1899  # 输入数据的特征维度
    # np.random.seed(42)  设置随机数种子
    '''
    加载数据
    '''
    train = load('../data/spamTrain.mat', 'train')  # 4000条
    test = load('../data/spamTest.mat', 'test')  # 1000条
    '''
    开始训练
    '''
    svm = SVM(features=num_features)  # 初始化svm
    i_list, fun_list, acc_list = svm.pegasos(train, test, C, T, f, loss_type=loss_type)  # 佩加索斯
    '''
    画图
    '''
    plots(i_list, fun_list, acc_list, C, T, loss_type,kernel)



