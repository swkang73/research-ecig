'''E-cigarette PCA + SVM Classifier
classifies e-cigarette mass scan into three e-cig (G6 / Juul / Blu)
reference: https://www.kaggle.com/cyberzhg/sklearn-pca-svm/data
'''
import numpy as np, csv
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC

COMPONENT_NUM = 20
RANOM_STATE = 0
CIGTOTAL = 3
G6 = 1
JUUL = 2
BLU = 3


def getAns(index):
    if index % CIGTOTAL != 0:
        return index % CIGTOTAL
    return BLU

print('Read training data...')
with open('training.csv', 'r') as reader:
    train_label = []
    train_data = []
    for line in reader.readlines():
        data = list(map(float, line.rstrip().split(',')))
        train_label.append(data[0])
        train_data.append(data[1:])
print('Loaded ' + str(len(train_label)))

print('Reduction...')
train_label = np.array(train_label)
train_data = np.array(train_data)
pca = PCA(n_components=COMPONENT_NUM, whiten=True)
pca.fit(train_data)
train_data = pca.transform(train_data)

print('Train SVM...')
svc = SVC(random_state=RANOM_STATE, probability=True)
svc.fit(train_data, train_label)

print('Read testing data...')
with open('testing_v2.csv', 'r') as reader:
    test_data = []
    for line in reader.readlines():
        pixels = list(map(float, line.rstrip().split(',')))
        test_data.append(pixels)
print('Loaded ' + str(len(test_data)))

print('Predicting...')
test_data = np.array(test_data)
test_data = pca.transform(test_data)
predict = svc.predict(test_data)
prob = svc.predict_proba(test_data)


print('Saving...')
with open('svm_pca_predict_v2.csv', 'w') as outcsv:
    writer = csv.DictWriter(outcsv, fieldnames = ['Index', 'Prediction'])
    writer.writeheader()

    count = 0
    for p in predict:
        count += 1
        #'Actual': str(getAns(count))
        writer.writerow({'Index': str(count), 'Prediction': str(p)})

