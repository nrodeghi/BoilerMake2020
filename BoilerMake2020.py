import plaidml.keras
#from plaidml import keras
from tensorflow import keras

plaidml.keras.install_backend()
#import os
import pandas as pd
import numpy as np
np.random.seed(1337) # for reproducibility
#from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
#import tensorflow as tf
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
#from keras.utils.vis_utils import plot_model
from sklearn.metrics import classification_report, confusion_matrix

# AI Powered Sentiment Predictive Tool for Sustainability Awareness and Advocacy

def main(filename):

    x_orig, y_orig = preprocess(filename)

    x_orig = x_orig.astype(float)
    y_orig = y_orig.astype(float)

    y_orig1 = y_orig[:, 0]

    # using set named test for training, and set named train for testing

    X_train = x_orig[0:68, :]
    X_test = x_orig[68:84, :]

    y_train1 = y_orig[0:68, 0]
    y_train2 = y_orig[0:68, 1]
    y_train3 = y_orig[0:68, 2]

    y_test1 = y_orig[68:84, 0]
    y_test2 = y_orig[68:84, 1]
    y_test3 = y_orig[68:84, 2]

    predict_with_model(X_train, X_test, y_train1, y_test1, 'Info_Utility.h5')
    predict_with_model(X_train, X_test, y_train2, y_test2, 'Habit_Change.h5')
    predict_with_model(X_train, X_test, y_train3, y_test3, 'Care_Sentiment.h5')


def predict_with_model(X_train, X_test, y_train, y_test, modname):

    model = Sequential()
    model.add(Dense(30, input_dim=14, activation='relu'))
    model.add(Dense(25, activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_test, y_test, epochs=35)

    _, accuracy = model.evaluate(X_test, y_test)
    print('Accuracy: %.2f' % (accuracy * 100))
    print("Model Summary:")
    print(model.summary())

    scores = model.evaluate(X_test, y_test, verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
    # save model and architecture to single file
    model.save(modname)
    print("Saved model to disk")

    print("loading model")
    # load model
    model = load_model(modname)
    # summarize model.
    model.summary()

    # evaluate the model
    score = model.evaluate(X_test, y_test, verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], score[1] * 100))
    print("finished! :)")

    # make class predictions with the model
    predictions = model.predict_classes(X_train)

    #fpr, tpr, thresholds = roc_curve(y_train, predictions)

    for i in range(0, len(predictions)):
        #print('%d (expected %d)' % (predictions[i], y_test2[i]))
        print('%d (expected %d)' % (predictions[i], y_train[i]))

    ''''
    plot_roc_curve(fpr, tpr)
    print("auc score")
    auc_score = roc_auc_score(y_train, predictions)
    print(auc_score)

    print(classification_report(y_train, predictions))
    print("confusion matrix:")
    print(confusion_matrix(y_train, predictions))
    '''

def plot_roc_curve(fpr, tpr):
    plt.plot(fpr, tpr)
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.show()


def preprocess(filename):
    print("loading dataset")
    # load the dataset
    dataset = pd.read_csv(filename, skiprows=0)

    training_array = np.array(dataset)
    #print(training_array[1][1])

    array2 = (np.where(training_array == '18–22', 1, training_array))
    array2 = (np.where(array2 == '23–27', 2, array2))
    array2 = (np.where(array2 == 'Prefer not to say', 3, array2))

    #print(training_array[:, 2])
    array2 = (np.where(array2 == 'In full-time education', 0, array2))
    #print(array2[:, 2])

    #print(training_array[:, 3])
    array2 = (np.where(array2 == 'Not working at all', 0, array2))
    array2 = (np.where(array2 == 'Part-time', 1, array2))
    #print(array2[:, 3])

    #print(training_array[:, 4])
    array2 = (np.where(array2 == 'Walk / Cycle', 1, array2))
    array2 = (np.where(array2 == 'Bus / Train', 2, array2))
    array2 = (np.where(array2 == 'Car / Motorbike', 3, array2))
    array2 = (np.where(array2 == 'I don\'t travel', 0, array2))

    array2 = (np.where(array2 == 'Walk / Cycle;Bus / Train', 1.5, array2))
    array2 = (np.where(array2 == 'Walk / Cycle;Car / Motorbike', 2, array2))
    array2 = (np.where(array2 == 'Bus / Train;Car / Motorbike', 2.5, array2))
    array2 = (np.where(array2 == 'Walk / Cycle;Car / Motorbike;Bus / Train', 2, array2))
    array2 = (np.where(array2 == 'Walk / Cycle;I don\'t travel', -1, array2))
    array2 = (np.where(array2 == 'Car / Motorbike;Bus / Train', 2.5, array2))
    #print(array2[:, 4])

    #print(training_array[:, 5])
    array2 = (np.where(array2 == 'Less than 15 minutes', 2, array2))
    array2 = (np.where(array2 == 'I don\'t travel', -1, array2))
    array2 = (np.where(array2 == 'Less than an hour', 1, array2))
    array2 = (np.where(array2 == 'Less than 5 minutes', 0, array2))
    #print(array2[:, 5])

    #print(training_array[:, 7])
    array2 = (np.where(array2 == 'Yes', 0, array2))
    array2 = (np.where(array2 == 'No', 1, array2))
    #print(array2[:, 7])

    #print(training_array[:, 13])
    array2 = (np.where(array2 == 'Yes', 0, array2))
    array2 = (np.where(array2 == 'Maybe', 1, array2))
    #print(array2[:, 13])

    #print(training_array[:, 14])
    array2 = (np.where(array2 == 'Changed what I buy', 1, array2))
    array2 = (np.where(array2 == 'Changed how I travel', 2, array2))
    array2 = (np.where(array2 == 'Changed what I eat', 3, array2))
    array2 = (np.where(array2 == 'Changed devices or appliances in my house', 4, array2))
    array2 = (np.where(array2 == 'Changed my gas or electricity supplier', 5, array2))
    array2 = (np.where(array2 == 'I have not tried to reduce my carbon footprint', 0, array2))

    # combinations in dataset + .5 to distinguish after point total
    array2 = (np.where(array2 == 'Changed what I buy;Changed how I travel', 3.5, array2))
    array2 = (np.where(array2 == 'Changed how I travel;Changed devices or appliances in my house', 6.5, array2))
    array2 = (np.where(array2 == 'Changed how I travel;Changed what I eat', 5.5, array2))
    array2 = (np.where(array2 == 'Changed how I travel;Changed my gas or electricity supplier', 7.5, array2))
    array2 = (np.where(array2 == 'Changed what I buy;Changed what I eat', 4.5, array2))
    array2 = (np.where(array2 == 'Changed what I buy;Changed how I travel;Changed what I eat', 6.5, array2))
    array2 = (np.where(array2 == 'Changed how I travel;Changed devices or appliances in my house;Changed my gas or electricity supplier', 11, array2))

    #weird special cases
    array2 = (np.where(array2 == 'no', 0, array2))
    array2 = (np.where(array2 == 'Changed what I buy;Changed how I travel;Changed devices or appliances in my house;Sace water', 0, array2))
    array2 = (np.where(array2 == 'I still dont know what this is', 0, array2))
    array2 = (np.where(array2 == 'I just save water, and make sure the lights and pc are off if they are not needed', 0, array2))
    array2 = (np.where(array2 == 'Changed what I buy;Changed how I travel;Changed what I eat;Always make sure my electrics/lights are switched off when i go out', 0, array2))
    array2 = (np.where(array2 == 'Does recycling count?', 0, array2))
    array2 = (np.where(array2 == 'None', 0, array2))

    # L, M, and P will be output variables
    #print(training_array[:, 11])
    ##print(training_array[:, 12])
    #print(training_array[:, 15])

    for i in range (0,84):
        if (array2[i, 11]) > 3:
            array2[i, 11] = 1
        else:
            array2[i, 11] = 0

    for i in range(0, 84):
        if (array2[i, 15]) > 3:
            array2[i, 15] = 1
        else:
            array2[i, 15] = 0

    a = array2[:, 11]
    b = array2[:, 12]
    c = array2[:, 15]
    output = np.column_stack((a, b, c))
    #print(output)

    array2 = np.delete(array2, [0, 10, 13, 16, 18], axis=1)

    ''''
    print('test')
    for i in range(0, 13):
        print(array2[:, i])
    '''
    return array2, output


if __name__ == '__main__':
    main("student-responses-without-ids.csv")