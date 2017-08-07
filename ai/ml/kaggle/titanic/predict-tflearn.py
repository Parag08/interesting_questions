import tflearn

from tflearn.data_utils import load_csv
data, labels = load_csv('test.csv', target_column=0,
                        categorical_labels=True, n_classes=2)

net = tflearn.input_data(shape=[None, 6])
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 2, activation='softmax')
net = tflearn.regression(net)

# Define model

model = tflearn.DNN(net)


model.load("./model/titanic-model.tfl")



model
