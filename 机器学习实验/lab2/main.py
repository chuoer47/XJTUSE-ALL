# 生成数据集
from sklearn.datasets import make_blobs, make_circles
from matplotlib import pyplot as plt
import numpy as np
from sklearn.svm import SVC  # Support Vector Classifier
from sklearn import svm
from scipy.io import loadmat


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


if __name__ == '__main__':
    train = load('data/spamTrain.mat', 'train')  # 4000条
    test = load('data/spamTest.mat', 'test')  # 1000条
    train_x = train['X']  # 4000*1899
    train_y = train['y']  # 4000*1
    test_x = test['Xtest']  # 1000*1899
    test_y = test['ytest']  # 1000*1
    predictor = svm.SVC(gamma='scale', C=1.0, decision_function_shape='ovr', kernel='rbf')
    # 进行训练
    predictor.fit(train_x, train_y.ravel())
    # 预测结果
    result = predictor.predict(test_x)
    # 进行评估
    from sklearn.metrics import f1_score,accuracy_score,recall_score
    print("acc: {}".format(accuracy_score(result, test_y)))
    print("recall: {}".format(recall_score(result, test_y)))
    print("F-score: {}".format(f1_score(result, test_y, average='micro')))
