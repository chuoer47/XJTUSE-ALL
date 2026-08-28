# 标准库
import random

import matplotlib.pyplot as plt
# 第三方库
import numpy as np


# 定义 cross-entropy 和 quadratic 损失函数
class CrossEntropyCost(object):
    """
    该类表示交叉熵类，提供用于计算交叉熵相关的函数
    """

    @staticmethod
    def fn(a, y):
        """
        返回 a 和标签 y 之间的多分类交叉熵损失,
        使用np.nan_to_num 避免log计算导致的nan
        """
        loss = np.sum(np.nan_to_num(-y * np.log(a) - (1 - y) * np.log(1 - a)))
        return loss

    @staticmethod
    def delta(a, y):
        """返回偏导值 """
        return a - y


class QuadraticCost(object):
    """
    该类为均方误差损失函数
    """

    @staticmethod
    def fn(a, y):
        """返回 a 和标签 y 之间的损失"""
        return 0.5 * np.linalg.norm(a - y) ** 2

    @staticmethod
    def delta(a, y):
        """返回关于a的偏导 """
        return a - y


class Sigmoid(object):
    @staticmethod
    def fn(z):
        """sigmoid 激活函数"""
        return 1.0 / (1.0 + np.exp(-z))

    @staticmethod
    def prime(z):
        """sigmoid 激活函数的导数"""
        return Sigmoid.fn(z) * (1 - Sigmoid.fn(z))


class ReLU(object):
    @staticmethod
    def fn(z):
        return np.maximum(z, 0.0)

    @staticmethod
    def prime(z):
        return np.heaviside(z, 0.0)


def softmax(z):
    """softmax 函数"""
    e_x = np.exp(z - np.max(z))  # 向量运算
    return e_x / e_x.sum()


def softmax_derivative(x):
    y = np.exp(x)
    s = np.sum(y) + 1e-8  # 加上一个很小的值 epsilon
    grad = y * (s - y) / (s ** 2)
    return grad


# 定义主网络
class Network(object):

    def __init__(self, sizes, cost=CrossEntropyCost, activation_functions=Sigmoid):
        """
        参数 sizes 列表中包括神经网路中各层神经元的个数, 例如 [784, 192, 30, 10] 表示一个包含两个隐藏层的神经网络, 输入层
        包含 784 个神经元, 第一隐层包含 192 个神经元, 第二隐层包含 30 个神经元, 输出层包含 10 个神经元。此外, 对网络中的
        biases 和 weights 进行了初始化。
        activation_functions  # 激活函数
        """
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.default_weight_initializer()
        self.cost = cost
        self.activation_functions = activation_functions

    def default_weight_initializer(self):
        """初始化 weights 和 biases 均值为 0, 标准差为 1 的高斯分布, 输入层的神经元不设置 biases """
        self.biases = [np.random.randn(y, 1) for y in self.sizes[1:]]
        self.weights = [np.random.randn(x, y) for x, y in zip(self.sizes[:-1], self.sizes[1:])]  # 给输入层和隐藏层设置权重
        # randn(x,y)为返回维度为(x,y)的矩阵，符合高斯分布(正态分布)

    def feedforward(self, a):
        """输入 a, 返回神经网络的输出结果"""
        for b, w in zip(self.biases[:-1], self.weights[:-1]):
            a = self.activation_functions.fn(np.dot(w.transpose(), a) + b)  # \delta = W^{T} a + b 神经网络的一层结构
        b, w = self.biases[-1], self.weights[-1]  # 最后一层输出层的输出
        a = softmax(np.dot(w.transpose(), a) + b)  # 结果
        return a

    def SGD(self, training_data, epochs, mini_batch_size, eta,
            lmbda=0.0,
            evaluation_data=None,
            monitor_evaluation_cost=False,
            monitor_evaluation_accuracy=False,
            monitor_training_cost=False,
            monitor_training_accuracy=False):
        """
        使用小批量随机梯度下降算法来训练神经网络。training_data 是由元组 (x, y) 组成的列表, 表示训练输入和对应的标签。lmbda 为 L2
        正则化参数, 默认取值为 0.0, 即不使用 L2 正则化。evaluation_data 可以为验证集或测试集。该方法返回一个包含四个列表的元组, 
        列表内存有每个 epoch 的计算结果。
        """
        evaluation_data, training_data = list(evaluation_data), list(training_data)
        if evaluation_data:
            n_data = len(evaluation_data)
        n = len(training_data)
        evaluation_cost, evaluation_accuracy = [], []
        training_cost, training_accuracy = [], []

        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [training_data[k:k + mini_batch_size] for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta, lmbda, len(training_data))
            print("Epoch %s training complete" % j)

            if monitor_training_cost:
                cost = self.total_cost(training_data, lmbda)
                training_cost.append(cost)
                print("Cost on training data: {}".format(cost))
            if monitor_training_accuracy:
                accuracy = self.accuracy(training_data, convert=True) / n
                training_accuracy.append(accuracy)
                print("Accuracy on training data: {} / {}".format(accuracy * n, n))
            if monitor_evaluation_cost:
                cost = self.total_cost(evaluation_data, lmbda, convert=True)
                evaluation_cost.append(cost)
                print("Cost on evaluation data: {}".format(cost))
            if monitor_evaluation_accuracy:
                accuracy = self.accuracy(evaluation_data) / n_data
                evaluation_accuracy.append(accuracy)
                print("Accuracy on evaluation data: {} / {}\n".format(accuracy * n_data, n_data))

        return evaluation_cost, evaluation_accuracy, training_cost, training_accuracy

    def update_mini_batch(self, mini_batch, eta, lmbda, n):
        """
        对单个 mini batch 使用梯度下降算法来更新网络的权重和偏置, 其中, mini_batch 是由元组 (x, y) 组成的列表, eta 是学习率, 
        lmbda 是 L2 正则化参数, 默认情况下不使用 L2 正则化, n 是训练集的总长度。
        """
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            # TODO: 完成一个mini_batch中 nabla_b 和 nabla_w 的计算
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        # 参数更新
        batch_size = len(mini_batch)
        self.weights = [(1 - eta * (lmbda / n)) * w - (eta / batch_size) * nw
                        for w, nw in zip(self.weights, nabla_w)]  # 正则化的参数更新公式
        self.biases = [b - (eta / batch_size) * nb
                       for b, nb in zip(self.biases, nabla_b)]

    def backprop(self, x, y):
        """
        返回表示对于指定损失函数 C_x 的梯度元组 (nabla_b, nabla_w), 其中, nabla_b 和 nabla_w 是由 numpy arrays 组成的列表, 与
        self.biases 和 self.weights 的组成相似。
        """
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # 前向传播
        activation = x
        activations = [x]  # 该列表存储层与层之间所有的 a(激活) 值, a = sigmoid(w*x + b)
        zs = []  # 该列表存储层与层之间的 z 值, z = w*x + b
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w.transpose(), activation) + b
            zs.append(z)
            activation = self.activation_functions.fn(z)
            activations.append(activation)
        activations[-1] = softmax(zs[-1])  # 输出层为 softmax 函数, 而不是采用 sigmoid
        # 后向传播
        # TODO: 此处为BP1的计算
        prime = softmax_derivative(zs[-1])
        # prime2 = self.activation_functions.prime(zs[-1])
        delta = self.cost.delta(activations[-1], y)*prime
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(activations[-2], delta.transpose())

        # 循环中变量 l 的含义如下: l = 1 表示最后一层神经元, l = 2 表示倒数第二层神经元...
        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = self.activation_functions.prime(z)
            # TODO: 完成 delta 的计算，对应PPT中的BP2
            delta = np.dot(self.weights[-l + 1], delta) * sp
            # TODO: 完成 Partial E / Partial b 和 Partial E / Partial w, 对应PPT中的BP3和BP4
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(activations[-l - 1], delta.transpose())
        return nabla_b, nabla_w

    def accuracy(self, data, convert=False):
        """返回 data 中分类正确的图像的总数, 其中 convert 在训练集上应初始化为 True, 验证集或测试集上应初始化为 False """
        if convert:
            results = [(np.argmax(self.feedforward(x)), np.argmax(y)) for (x, y) in data]
        else:
            results = [(np.argmax(self.feedforward(x)), y) for (x, y) in data]
        return sum(int(x == y) for (x, y) in results)

    def total_cost(self, data, lmbda, convert=False):
        """返回 data 对应的损失, 其中 convert 在训练集上应初始化为 False, 验证集或测试集上应初始化为 True, lmbda 对应
         L2 正则化参数, 默认取值为 0.0, 即不进行 L2 正则化 """
        cost = 0.0
        for x, y in data:
            a = self.feedforward(x)
            if convert: y = vectorized_result(y)
            cost += self.cost.fn(a, y) / len(data)
        cost += 0.5 * (lmbda / len(data)) * sum(np.linalg.norm(w) ** 2 for w in self.weights)
        return cost


def vectorized_result(j):
    """将对应的数字 (0...9) 转化为对应的 one-hot 向量, 该向量的 j 下标对应的取值为 1.0, 其他为 0 """
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e


def plot_result(epochs, test_cost, test_accuracy, training_cost, training_accuracy, file_name):
    """绘制训练集和测试集的损失及准确率, 并将所得结果保存"""
    epoch = np.arange(epochs)
    plt.subplot(1, 2, 1)
    plt.plot(epoch, test_cost, 'r', label='test_cost')
    plt.plot(epoch, training_cost, 'k', label='training_cost')
    plt.title("Cost Range")
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(epoch, test_accuracy, 'r', label='test_accuracy')
    plt.plot(epoch, training_accuracy, 'k', label='training_accuracy')
    plt.title("Accuracy Range")
    plt.legend()
    plt.savefig('../output/' + file_name)
