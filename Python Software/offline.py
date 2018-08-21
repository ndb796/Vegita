import tensorflow as tf
import numpy as np
from pandas.io.parsers import read_csv

model = tf.global_variables_initializer();

data = read_csv('price data.csv', sep=',')

xy = np.array(data, dtype=np.float32)

# 4개의 변인을 입력을 받습니다.
x_data = xy[:, 1:-1]

# 가격 값을 입력 받습니다.
y_data = xy[:, [-1]]

# 플레이스 홀더를 설정합니다.
X = tf.placeholder(tf.float32, shape=[None, 4])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([4, 1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")

# 가설을 설정합니다.
hypothesis = tf.matmul(X, W) + b

# 비용 함수를 설정합니다.
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# 최적화 함수를 설정합니다.
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000005)
train = optimizer.minimize(cost)

# 세션을 생성합니다.
sess = tf.Session()

# 글로벌 변수를 초기화합니다.
sess.run(tf.global_variables_initializer())

# 학습을 수행합니다.
for step in range(100001):
    cost_, hypo_, _ = sess.run([cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
    if step % 500 == 0:
        print("#", step, " 손실 비용: ", cost_)
        print("- 배추 가격: ", hypo_[0])

# 학습된 모델을 저장합니다.
saver = tf.train.Saver()
save_path = saver.save(sess, "./saved.cpkt")
print('학습된 모델을 저장했습니다.')