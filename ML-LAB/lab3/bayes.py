# 从sklearn.datasets里导入20类新闻文本数据抓取器。
from sklearn.datasets import fetch_20newsgroups
# 从sklearn.cross_validation导入train_test_split模块用于分割数据集。
from sklearn.model_selection import train_test_split
# 从sklearn.feature_extraction.text里导入CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
# 从sklearn.naive_bayes里导入朴素贝叶斯分类器。
from sklearn.naive_bayes import MultinomialNB
# 从sklearn.metrics 导入 classification_report。
from sklearn.metrics import classification_report
from main import *

text_type = {'World': 0, 'Sci/Tech': 1, 'Sports': 2, 'Business': 3}


def load(path):
    """
    加载数据并进行预处理
    :param path: 数据路径
    """
    x, y = [], []
    file = open(path, 'r')
    for line in file:
        temp = line.split('|')  # 将类别和文本分离开
        x.append(temp[1])  # 载入文本
        #  预处理类别
        y.append(text_type[temp[0].strip()])
    file.close()
    return x, y


# 加载数据集
train_x, train_y = load('./data/news_category_train_mini.csv')
test_x, test_y = load('./data/news_category_test_mini.csv')
data_x = train_x + test_x
data_y = train_y + test_y
# 获取停用词
stopwords = set(nltk.corpus.stopwords.words('english'))
stopwords = list(stopwords)
# 随机打乱
# X_train, X_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.25, random_state=33)
# 不随机打乱
X_train, X_test, y_train, y_test = train_x, test_x, train_y, test_y
# print(y_train)
# 采用默认的配置对CountVectorizer进行初始化（默认配置不去除英文停用词），并且赋值给变量count_vec。
count_vec = CountVectorizer(stop_words=None)
# count_vec = CountVectorizer(stop_words=stopwords)

# 只使用词频统计的方式将原始训练和测试文本转化为特征向量。
# 学习词汇的词典并返回文档矩阵。
X_count_train = count_vec.fit_transform(X_train)
X_count_test = count_vec.transform(X_test)

# 使用默认的配置对分类器进行初始化。
mnb_count = MultinomialNB()
# 使用朴素贝叶斯分类器，对CountVectorizer（不去除停用词）后的训练样本进行参数学习。
mnb_count.fit(X_count_train, y_train)

# 输出模型准确性结果。
print('The accuracy of classifying :',
      mnb_count.score(X_count_test, y_test))
# 将分类预测的结果存储在变量y_count_predict中。
y_count_predict = mnb_count.predict(X_count_test)

# 输出更加详细的其他评价分类性能的指标。
print(classification_report(y_test, y_count_predict))
