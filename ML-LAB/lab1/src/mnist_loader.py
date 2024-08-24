# 标准库
import pickle
import gzip

# 第三方库
import numpy as np


def load_data():
    """
    以元组的形式加载 MNIST 数据集, 包括训练集、测试集、验证集。其中, 训练集是一个二维元组, 第一维具有 50000 组条目, 
    每个条目有 784 个数值, 代表单个 MNIST 图片的 28 * 28 = 784 像素值; 第二维同样具有 50000 组条目, 每个条目对应该
    手写数字的标签, 取值范围为 (0...9)。验证集和测试集的数据组成方式与训练集相似, 只是仅包含 10000 张照片。
    """
    f = gzip.open('../data/mnist.pkl.gz', 'rb')
    training_data, validation_data, test_data = pickle.load(f, encoding='bytes')
    f.close()
    return (training_data, validation_data, test_data)


def load_data_wrapper():
    """
    在 load_data 函数的基础上, 返回一个 (training_data, validation_data, test_data) 元组。其中, training_data 是包括 50000 个
    二维元组 (x, y) 的列表, x 是一个 784 维的 numpy.ndarray, 表示输入图像 (28*28 = 784) 的像素信息, y 是对应的 one-hot 标签向量。
    validation_data 和 test_data 是包括 10000 个二维元组 (x, y) 的列表, x 是一个 784 维的 numpy.ndarray, 表示输入图像 (28*28) 
    的像素信息, y 是对应的标签值。
    """
    tr_d, va_d, te_d = load_data()  # 加载数据

    training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]  # 将一个一维的x向量变为二维向量
    training_results = [vectorized_result(y) for y in tr_d[1]]  # 独热码向量
    training_data = zip(training_inputs, training_results)  # 打包

    validation_inputs = [np.reshape(x, (784, 1)) for x in va_d[0]]
    validation_data = zip(validation_inputs, va_d[1])  # 没有做独热码处理，后面操作注意！

    test_inputs = [np.reshape(x, (784, 1)) for x in te_d[0]]
    test_data = zip(test_inputs, te_d[1])

    return (training_data, validation_data, test_data)


def vectorized_result(j):
    """将对应的数字 (0...9) 转化为对应的 one-hot 向量, 该向量的 j 下标对应的取值为 1.0, 其他为 0 """
    e = np.zeros((10, 1))  # 利用numpy快速生成
    e[j] = 1.0
    return e


if __name__ == '__main__':
    load_data_wrapper()
