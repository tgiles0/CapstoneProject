# Required Python Packages
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

import pdb

# File Paths
INPUT_PATH = "botsv1.WinEventLog_Security.csv"
OUTPUT_PATH = "botsv1.WinEventLog_SecurityOUT.csv"

# Headers
HEADERS = ["_serial", "_time", "source", "sourcetype", "host",
               "index", "splunk_server", "_raw"]


def read_data(path):
    """
    Read the data into pandas dataframe
    :param path:
    :return:
    """
    data = pd.read_csv(path)
    return data


def get_headers(dataset):
    """
    dataset headers
    :param dataset:
    :return:
    """
    return dataset.columns.values


def add_headers(dataset, headers):
    """
    Add the headers to the dataset
    :param dataset:
    :param headers:
    :return:
    """
    dataset.columns = headers
    return dataset


def data_file_to_csv():
    """

    :return:
    """

    # Headers ,,,,,,"",""
    headers = ["_serial", "_time", "source", "sourcetype", "host",
               "index", "BareNuclei", "splunk_server", "_raw"]
    # Load the dataset into Pandas data frame
    dataset = read_data(INPUT_PATH)
    # Add the headers to the loaded dataset
    # dataset = add_headers(dataset, headers)
    # Save the loaded dataset into csv format
    # dataset.to_csv(OUTPUT_PATH, index=False)
    print ("File saved ...!")


def split_dataset(dataset, train_percentage, feature_headers, target_header):
    """
    Split the dataset with train_percentage
    :param dataset:
    :param train_percentage:
    :param feature_headers:
    :param target_header:
    :return: train_x, test_x, train_y, test_y
    """

    # Split dataset into train and test dataset
    train_x, test_x, train_y, test_y = train_test_split(dataset[feature_headers], dataset[target_header],
                                                        train_size=train_percentage)
    return train_x, test_x, train_y, test_y


def handel_missing_values(dataset, missing_values_header, missing_label):
    """
    Filter missing values from the dataset
    :param dataset:
    :param missing_values_header:
    :param missing_label:
    :return:
    """

    return dataset[dataset[missing_values_header] != missing_label]

def outlier_prediction(x_train, y_train):
    # Use built-in isolation forest or use predicted vs. actual
    # Compute squared residuals of every point
    # Make a threshold criteria for inclusion

    # The prediction returns 1 if sample point is inlier. If outlier prediction returns -1
    rng = np.random.RandomState(42)
    clf_all_features = IsolationForest(max_samples=100, random_state=rng)
    clf_all_features.fit(x_train)

    # Predict if a particular sample is an outlier using all features for higher dimensional data set.
    y_pred_train = clf_all_features.predict(x_train)

    # Exclude suggested outlier samples for improvement of prediction power/score
    outlier_map_out_train = np.array(map(lambda x: x == 1, y_pred_train))
    x_train_modified = x_train[outlier_map_out_train,]
    y_train_modified = y_train[outlier_map_out_train,]

    return x_train_modified, y_train_modified


def dataset_statistics(dataset):
    """
    Basic statistics of the dataset
    :param dataset: Pandas dataframe
    :return: None, print the basic statistics of the dataset
    """
    print (dataset.describe())


def main():
    """
    Main function
    :return:
    """
    # Load the csv file into pandas dataframe
    dataset = pd.read_csv("botsv1.WinEventLog_Application.csv")

    # dataset = pd.read_csv(INPUT_PATH)

    print ("FILE WAS READ!!")

    # dataset = pd.read_csv(OUTPUT_PATH)
    # Get basic statistics of the loaded dataset
    dataset_statistics(dataset)

    # Filter missing values
    dataset = handel_missing_values(dataset, HEADERS[6], '?')
    train_x, test_x, train_y, test_y = split_dataset(dataset, 0.7, HEADERS[1:-1], HEADERS[-1])

    # Train and Test dataset size details
    print ("Train_x Shape :: ", train_x.shape)
    print ("Train_y Shape :: ", train_y.shape)
    print ("Test_x Shape :: ", test_x.shape)
    print ("Test_y Shape :: ", test_y.shape)


    # Create Isolation Forest
    trained_model = outlier_prediction(train_x, train_y)
    print ("Trained model :: ", trained_model)
    predictions = trained_model.predict(test_x)

    for i in range(0, 5):
        print ("Actual outcome :: {} and Predicted outcome :: {}".format(list(test_y)[i], predictions[i]))

    print ("Train Accuracy :: ", accuracy_score(train_y, trained_model.predict(train_x)))
    print ("Test Accuracy  :: ", accuracy_score(test_y, predictions))
    print (" Confusion matrix ", confusion_matrix(test_y, predictions))


if __name__ == "__main__":
    main()