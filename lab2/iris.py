import numpy as np
import matplotlib.pyplot as plt


def load(name):
    lista = []
    category = []
    f = open(name, "r")
    for line in f:
        line = line.strip().split(",")
        lista.append(np.array([[line[0]], [line[1]], [line[2]], [line[3]]]))
        if line[4] == "Iris-setosa":
            category.append(0)
        if line[4] == "Iris-versicolor":
            category.append(1)
        if line[4] == "Iris-virginica":
            category.append(2)
    f.close()
    return np.hstack(lista), np.hstack(category)


[a, b] = load("iris.csv")
setosa = a[:, b == 0]
versicolor = a[:, b == 1]
virginica = a[:, b == 2]
# sepal length Iris-setosa
plt.hist(setosa[0], bins=10, density=True, ec="white", color="black", alpha=0.6)
# sepal length Iris-versicolor
plt.hist(versicolor[0], bins=10, density=True, ec="black", color="yellow", alpha=0.6)
# sepal length Iris-virginica
plt.hist(virginica[0], bins=10, density=True, ec="black", color="red", alpha=0.6)
# plt.hist(a, bins=20, density=True, ec="black", color="#800000")
# plt.show()
setosa[0]=np.sort(setosa[0])
versicolor[0]=np.sort(versicolor[0])
virginica[0]=np.sort(virginica[0])
plt.scatter(setosa[0],setosa[1])
# plt.xlim(8,4)
plt.scatter(versicolor[0],versicolor[1],color="red")
plt.scatter(virginica[0],virginica[1],color="black")
# plt.axis((0,8,0,20))
plt.show()
# sepal width Iris-setosa
plt.hist(setosa[1], bins=10, density=True, ec="black", color="green", alpha=0.6)
# sepal width Iris-versicolor
plt.hist(versicolor[1], bins=10, density=True, ec="black", color="yellow", alpha=0.6)
# sepal width Iris-virginica
plt.hist(virginica[1], bins=10, density=True, ec="black", color="red", alpha=0.6)
# plt.show()

# petal length Iris-setosa
plt.hist(setosa[2], bins=10, density=True, ec="black", color="green", alpha=0.6)
# petal length Iris-versicolor
plt.hist(versicolor[2], bins=10, density=True, ec="black", color="yellow", alpha=0.6)
# petal length Iris-virginica
plt.hist(virginica[2], bins=10, density=True, ec="black", color="red", alpha=0.6)
# plt.show()

# petal width Iris-setosa
plt.hist(setosa[3], bins=10, density=True, ec="black", color="green", alpha=0.6)
# petal width Iris-versicolor
plt.hist(versicolor[3], bins=10, density=True, ec="black", color="yellow", alpha=0.6)
# petal width Iris-virginica
plt.hist(virginica[3], bins=10, density=True, ec="black", color="red", alpha=0.6)
# plt.show()

