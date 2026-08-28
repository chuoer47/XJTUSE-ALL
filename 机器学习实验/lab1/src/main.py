import mnist_loader
import network
import os

if __name__ == '__main__':
    print("begin:")
    # 改变工作路径至当前文件目录
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    epochs = 50
    mini_batch_size = 10
    eta = 0.5
    net_sizes = [784, 192, 30, 10]
    lmbda = 0
    output_pic = 'epochs' + "test0703" + '_result.jpg'

    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
    net = network.Network(net_sizes, cost=network.CrossEntropyCost)
    test_cost, test_accuracy, training_cost, training_accuracy \
        = net.SGD(training_data, epochs, mini_batch_size, eta, lmbda=lmbda, evaluation_data=test_data,
                  monitor_evaluation_cost=True, monitor_evaluation_accuracy=True,
                  monitor_training_cost=True, monitor_training_accuracy=True)

    network.plot_result(epochs, test_cost, test_accuracy, training_cost, training_accuracy, output_pic)
