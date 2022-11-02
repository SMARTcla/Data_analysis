from cmath import nan
import pandas
import numpy
import math
import seaborn
import os
import matplotlib.pyplot

def task_1():
    dataset = pandas.read_csv("titanic.csv")
    # друк набору даних
    print(dataset)
    # приймати int змінні
    titanic_data = pandas.read_csv("titanic.csv", names=["Age", "PassengerId", "Survived", "PClass", "SibSp","Parch"])
    # роздрукувати цю інформацію
    print(titanic_data.head())
    # кількість рядків, зроблених за допомогою len()
    number_of_lines = len(dataset)
    # кількість ліній, зроблених за допомогою shape()
    number_of_column = dataset.shape
    # кількість ліній, зроблених за допомогою size
    number_of_value = dataset.size
    print("Number of Lines")
    print(number_of_lines)
    print("Number of Column and Lines")
    print(number_of_column)
    print("Number of Value")
    print(number_of_value)
    # типи друку всіх стовпців
    print(f"PassengerId - {type(dataset['PassengerId'][0])}")
    print(f"Survived - {type(dataset['Survived'][0])}")
    print(f"Pclass - {type(dataset['Pclass'][0])}")
    print(f"Name - {type(dataset['Name'][0])}")
    print(f"Sex - {type(dataset['Sex'][0])}")
    print(f"Age - {type(dataset['Age'][0])}")
    print(f"SibSp - {type(dataset['SibSp'][0])}")
    print(f"Parch - {type(dataset['Parch'][0])}")
    print(f"Ticket - {type(dataset['Ticket'][0])}")
    print(f"Fare - {type(dataset['Fare'][0])}")
    print(f"Cabin - {type(dataset['Cabin'][0])}")
    print(f"Embarked - {type(dataset['Embarked'][0])}")

def task_2():
    # відкрити csv
    news_ = ["PassengerId", "Survived", "Pclass", "Name", "Sex","Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]
    dataset = pandas.read_csv("titanic.csv", header=0, index_col=news_, usecols=news_)
    # друк набору даних
    # print(dataset)
    # формування списка пропущених значень по кожному атрибуту
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # цикл по кількості столбців і по всім елементам
    for i in range(len(dataset.index)):
        for j in range(4, 11):
            if type(dataset.index[i][j]) != type("adwa"):
                if math.isnan(dataset.index[i][j]) == True:
                    arr[j] = arr[j] + 1
    # виведення результатів
    for i in range(12):
        print(f"Missing items in field |{news_[i]}|  =  {arr[i]}")


def task_3():
    # відкриття csv файлу
    dataset = pandas.read_csv("titanic.csv")
    # получение списка з int типами даних
    numeric_col = ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch']

    # Формування кореляційної матриці
    matrix_ = dataset.loc[:,numeric_col].corr()
    print(matrix_)

    #Використання теплокарти для візуалізації кореляційної матриці
    seaborn.heatmap(matrix_, annot=True)
    corr = dataset.corr()
    corr.style.background_gradient(cmap='coolwarm')


def task_5():
    news_ = ["PassengerId", "Survived", "Pclass", "Name", "Sex","Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]
    dataset = pandas.read_csv("titanic.csv", header=0, index_col=news_, usecols=news_)
    tutors = []
    print(dataset.index[0][5])
    print(dataset.index[1][5])
    print(dataset.index[2][5])
    for i in range(891):
        if math.isnan(dataset.index[i][5]) == False:
            if dataset.index[i][5] <= 16.0:
                tutors.append(0)
            if dataset.index[i][5] > 16.0 and dataset.index[i][5] <= 32.0:
                tutors.append(1)
            if dataset.index[i][5] > 32.0 and dataset.index[i][5] <= 48.0:
                tutors.append(2)
            if dataset.index[i][5] > 48.0 and dataset.index[i][5] <= 64.0:
                tutors.append(3)
            if dataset.index[i][5] > 64.0 and dataset.index[i][5] <= 80.0:
                tutors.append(4)
        else:
            tutors.append(float('nan'))
    dataset = dataset.assign(Age_bin=tutors)
    dataset = pandas.read_csv("titanic.csv", header=0, index_col='Age_bin', usecols='Age_bin')
    dataset.plot()
    matplotlib.pyplot.show()

    dataset.plot(x="Age_bin", y=["PassengerId"])
    matplotlib.pyplot.show()

def task_6():
    news_ = ["Fare"]
    dataset = pandas.read_csv("titanic.csv", header=0, index_col=news_, usecols=news_)
    array = []
    for i in range(891):
        array.append(dataset.index[i])
    pandas.qcut(array, q=5)
def task_7():
    news_ = ["PassengerId", "Survived", "Pclass", "Name", "Sex","Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]
    dataset = pandas.read_csv("titanic.csv", header=0, index_col=news_, usecols=news_)
    family_size = []
    alone = []
    for i in range(891):
        family_size.append(dataset.index[i][7] + dataset.index[i][6])
        if dataset.index[i][7] == 0 and dataset.index[i][6] == 0:
            alone.append(False)
        else:
            alone.append(True)
    dataset['Family_size'] = family_size
    dataset['Alone'] = alone
    print(dataset)

def task_8():
    news_ = ["PassengerId", "Survived", "Pclass", "Name", "Sex","Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]
    dataset = pandas.read_csv("titanic.csv", header=0, index_col=news_, usecols=news_)
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    array = []
    for i in range(len(dataset.index)):
        array.append(0)
        for j in range(4, 12):
            if type(dataset.index[i][j]) == type(float('nan')):
                if math.isnan(dataset.index[i][j]) == True:
                    array[i] += 1
    new_arr = []
    for i in range(len(dataset.index)):
        if array[i] == 2 or array[i] == 3:
            new_arr.append(i)
    dataset.drop(new_arr)



task_8()
