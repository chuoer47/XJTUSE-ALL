import copy
import string
import nltk
import numpy as np
from collections import Counter
from scipy.sparse import lil_matrix

# TODO 数据加载
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')
#  加载停用词
stopwords = set(nltk.corpus.stopwords.words('english'))
#  文本类别
text_type = {'World': 0, 'Sci/Tech': 1, 'Sports': 2, 'Business': 3}


def load(path, type_r):
    """
    加载数据并进行预处理
    :param path: 数据路径
    :param type_r: 使用的单词还原方法
    """
    x, y = [], []
    file = open(path, 'r')
    trans = str.maketrans('', '', string.punctuation)
    if type_r == 'stemmer':
        re = nltk.stem.porter.PorterStemmer().stem
    elif type_r == 'lemmatizer':
        re = nltk.stem.WordNetLemmatizer().lemmatize
    else:
        raise ValueError('type error')
    for line in file:
        temp = line.split('|')  # 将类别和文本分离开
        # 预处理文本
        sent = temp[1].strip().lower()  # 全小写
        sent = sent.translate(trans)  # 去除标点符号
        sent = nltk.word_tokenize(sent)  # 将文本标记化
        sent = [s for s in sent if not ((s in stopwords) or s.isdigit())]  # 去停用词和数字
        sent = [re(s) for s in sent]  # 还原: 词干提取/词形还原
        x.append(sent)
        #  预处理类别
        y.append(text_type[temp[0].strip()])
    file.close()
    return x, y


def words2dic(sent):
    """
    生成数据对应的文本库id
    :param sent: 数据集
    :return: 文本库
    """
    dicts = {}
    i = 0
    for words in sent:
        for word in words:
            if word not in dicts:
                dicts[word] = i
                i += 1
    return dicts


def train_TF(data_x, data_y, sigma=1):
    """
    朴素贝叶斯训练
    :param data_x:训练数据
    :param data_y:真值
    """
    # 构建词典，用于生成统计矩阵
    dicts = words2dic(data_x)
    # n(w_i in w_c) 创建词频矩阵
    word_fre = np.zeros((len(dicts), 4), dtype=np.int32)
    # n(c, text) 每类下的句总数
    sent_fre = np.zeros((1, 4), dtype=np.int32)
    # 更新矩阵
    for x, y in zip(data_x, data_y):
        for word in x:
            word_fre[dicts[word], y] += 1
        sent_fre[0, y] += 1
    # TODO 计算P(c)
    p_c = np.zeros(len(text_type), dtype=float)
    for i in range(len(text_type)):
        p_c[i] = sent_fre[0, i] / len(data_x)
    # TODO n(w_c) 每类下的词总数（维度：类别数*1）
    text_type_words = np.zeros(len(text_type), dtype=np.int32)
    for i in range(len(text_type)):
        for j in range(len(dicts)):
            text_type_words[i] += word_fre[j][i]
    # TODO 计算P(w_i|c)，并加入拉普拉斯平滑
    p_stage = np.zeros((len(dicts), len(text_type)), dtype=float)
    for i in range(len(dicts)):
        for j in range(len(text_type)):
            p_stage[i][j] = (word_fre[i][j] + sigma) / (text_type_words[j] + len(dicts))
    return dicts, p_stage, p_c


def test_TF(data_x, data_y, dicts, p_stage, p_c):
    """
    测试准确率
    """
    # 计算ln P(c)
    ln_p_c = np.log(p_c)
    # 计算准确率
    count = 0
    # 计算ln P(w_i|c)
    p_log_stage = np.log(p_stage)
    # TODO 计算对应的预测值并统计，注意过滤未收录词
    for i, words in enumerate(data_x):
        p_final = np.zeros(len(text_type), dtype=float)
        p_final += ln_p_c
        for j in range(len(text_type)):
            for k in range(len(words)):
                if words[k] in dicts:
                    p_final[j] += p_log_stage[dicts[words[k]]][j]
        if np.argmax(p_final, axis=0) == data_y[i]:  # 预测成功
            count += 1
    print('Accuracy: {}/{} {:.2f}%'.format(count, len(data_y), 100 * count / len(data_y)))


def train_B(train_x, train_y):
    # TODO 扩展，实现Bernoulli方法
    # 构建词典，用于生成统计矩阵
    dicts = words2dic(train_x)
    len_dicts = len(dicts)
    len_text_type = len(text_type)
    len_train_x = len(train_x)
    # n(w_i in w_c) 词-类-词频矩阵（维度：词汇数*类别树）
    words_fre = np.zeros((len_dicts, len_text_type), dtype=int)
    for i in range(len_train_x):
        # flag判断当前样本是否出现过某单词
        flag = np.zeros(len_dicts, dtype=int)
        for j in range(len(train_x[i])):
            flag[dicts[train_x[i][j]]] = 1
        for k in range(len_dicts):
            if flag[k]:
                words_fre[k][train_y[i]] += 1
    # n(c,text)每类下的句总数
    type_sents = np.zeros(len_text_type, dtype=int)
    for i in range(len_train_x):
        type_sents[train_y[i]] += 1
    # p(c)的计算 维度:类别数*1
    p_c = np.zeros(len_text_type, dtype=float)
    for i in range(len_text_type):
        p_c[i] = type_sents[i] / len_train_x
    # p(w_i|c)(维度：词汇数*类别数)
    p_stage = np.zeros((len_dicts, len_text_type), dtype=float)
    for i in range(len_dicts):
        for j in range(len_text_type):
            p_stage[i][j] = (words_fre[i][j] + 1) / (type_sents[j] + 2)
    return dicts, p_stage, p_c


def test_B(data_x, data_y, dicts, p_stage, p_c):
    count = 0
    ln_p_c = np.log(p_c)
    len_text_type = len(text_type)
    for i, words in enumerate(data_x):
        flag = np.zeros(len(dicts), dtype=int)
        p_final = np.zeros(len(text_type), dtype=float)
        p_final += ln_p_c
        for k in range(len(words)):
            if words[k] in dicts:
                flag[dicts[words[k]]] = 1
        for j in range(len(text_type)):
            for l in range(len(dicts)):
                if flag[l]:
                    p_final[j] += np.log(p_stage[l][j])
                else:
                    p_final[j] += np.log(1 - p_stage[l][j])
        if np.argmax(p_final, axis=0) == data_y[i]:
            count += 1
    print('Accuracy: {}/{} {:.2f}%'.format(count, len(data_y), 100 * count / len(data_y)))


if __name__ == '__main__':
    '''超参数设置'''
    # 单词还原方法
    type_re = ['stemmer', 'lemmatizer'][0]
    # 训练方法
    type_train = ['TF', 'Bernoulli'][0]
    sigma = 10e-2

    print('训练方法: {}'.format(type_train))
    print('还原方法: {}'.format(type_re))
    print("sigma:{}".format(sigma))

    '''读取训练数据并进行预处理'''
    train_x, train_y = load('./data/news_category_train_mini.csv', type_re)
    test_x, test_y = load('./data/news_category_test_mini.csv', type_re)
    print('load success')

    '''开始训练'''
    if type_train == 'TF':
        dictionary, p_stage, p_c = train_TF(train_x, train_y, sigma=sigma)
    elif type_train == 'Bernoulli':
        dictionary, p_stage, p_c = train_B(train_x, train_y)
    print("train over!")
    '''计算准确率'''
    if type_train == 'TF':
        test_TF(train_x, train_y, dictionary, p_stage, p_c)
        test_TF(test_x, test_y, dictionary, p_stage, p_c)
    elif type_train == 'Bernoulli':
        test_B(train_x, train_y, dictionary, p_stage, p_c)
        test_B(test_x, test_y, dictionary, p_stage, p_c)
