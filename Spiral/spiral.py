import random

from NeuralNetwork import NeuralNetwork
import nnfs
from nnfs.datasets import spiral_data
import matplotlib.pyplot as plt

if __name__ == '__main__':
    nnfs.init()

    # Create dataset
    points, targetClasses = spiral_data(samples = 1000, classes=3)
    # classes[i] means that points[i] belongs to the class classes[i].
    data = list(zip(points, targetClasses))
    random.shuffle(data)
    trainingData = data[:1000]
    testData = data[1000:1150]
    #plt.scatter(points[:, 0], points[:, 1])
    #plt.scatter(points[:, 0], points[:, 1], c=targetClasses, cmap='brg')
    #plt.show()

    neuralNetwork = NeuralNetwork([2, 64, 64, 3])
    neuralNetwork.train(trainingData, testData)
