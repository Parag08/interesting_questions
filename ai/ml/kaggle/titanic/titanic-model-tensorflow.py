import numpy as np
import tflearn

from tflearn.datasets import titanic
titanic.download_dataset('titanic_dataset.csv')

# Load CSV file, indicate that the first column represents labels
from tflearn.data_utils import load_csv
data, labels = load_csv('train.csv', target_column=0,
                        categorical_labels=True, n_classes=0)

# Preprocessing function
def preprocess(passengers, columns_to_delete):
    # Sort by descending id and delete columns
    for column_to_delete in sorted(columns_to_delete, reverse=True):
        [passenger.pop(column_to_delete) for passenger in passengers]
    for i in range(len(passengers)):
        # Converting 'sex' field to float (id is 1 after removing labels column)
        passengers[i][1] = 1. if passengers[i][1] == 'female' else 0.
    return np.array(passengers, dtype=np.float32)

# Ignore 'name' and 'ticket' columns (id 1 & 6 of data array)
to_ignore=[1, 6]

# Preprocess data
data = preprocess(data, to_ignore)

# Build neural network
net = tflearn.input_data(shape=[None, 6])
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 2, activation='softmax')
net = tflearn.regression(net)

# Define model
model = tflearn.DNN(net)
# Start training (apply gradient descent algorithm)
model.fit(data, labels, n_epoch=10, batch_size=16, show_metric=True)

model.save("./model/titanic-model.tfl")
