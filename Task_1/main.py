from cmath import nan
from hashlib import new
from math import sqrt
from typing import List
import numpy
import pandas
import math

def is_palindrome(s: str) -> bool:
    length = len(s) - 1
    for i in range(int(len(s)/2)):
        if s[i] != s[length]:
            return False
        length = length - 1
    return True


def solve_quad(a: float, b: float, c: float):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return (x1, x2)
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        return False


def merge(a: List[int], b: List[int]) -> List[int]:

    newer = []
    for i in range(len(a)):
        newer.append(a[i])

    for i in range(len(b)):
        newer.append(b[i])

    newer = sorted(newer)
    return newer


def merge_(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def MergeSort_(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        MergeSort_(arr, l, m)
        MergeSort_(arr, m+1, r)
        merge_(arr, l, m, r)


def MergeSort(arr):
    MergeSort_(arr, l=0, r=len(arr) - 1)
    return arr


def is_equal(X, Y, Z):
    if numpy.array_equal(Y, X, equal_nan=True):
        if numpy.array_equal(Z, X, equal_nan=True):
            if numpy.array_equal(Y, Z, equal_nan=True):
                return True
    return False

def rot_vec(x):
    lenght = len(x)
    x = numpy.reshape(x, (lenght, 1))
    return x

def get_diag(X):
    return numpy.diag(X)


def sec_diag(X):
    c = numpy.r_[numpy.diag(X, k = 1)[None,:],numpy.diag(X, k = -1)[None,:]]
    return c


def who_more():
    dataset = pandas.read_csv('titanic.csv')
    s = dataset[(dataset["Sex"] == "male")]
    return len(s)

def statistic():
    dataset = pandas.read_csv('titanic.csv', header=0, index_col=["Age", "Sex"], usecols=["Age", "Sex"])
    av_male = 0.0
    av_female = 0.0
    len_male = 0
    len_female = 0
    av_all = 0.0
    len_all = 0
    max_all = dataset.index[0][0]
    min_all = dataset.index[0][0]
    for i in range(len(dataset.index)):
        if math.isnan(dataset.index[i][0]) == False:
            len_all += 1
            av_all += dataset.index[i][0]
            if dataset.index[i][1] == "male":
                len_male = len_male + 1
                av_male += dataset.index[i][0]
            if dataset.index[i][1] == "female":
                len_female = len_female + 1
                av_female += dataset.index[i][0]
            if max_all < dataset.index[i][0]:
                max_all = dataset.index[i][0]
            if min_all > dataset.index[i][0]:
                min_all = dataset.index[i][0]

    return av_all/len_all, av_male/len_male, av_female/len_female, min_all, max_all

if __name__ == "__main__":
    assert is_palindrome("ada") == True
    assert is_palindrome("adda") == True
    assert is_palindrome("adxda") == True
    assert is_palindrome("ytradxdarty") == True
    assert is_palindrome("ada2") == False
    assert is_palindrome("sadda") == False
    assert is_palindrome("adaxda") == False
    assert is_palindrome("ytfradxdarty") == False

    assert solve_quad(2.0, 4.0, 2.0) == -1.0
    assert solve_quad(3.2, -7.8, 1.0) == (2.3017327156977156,0.13576728430228405)
    assert solve_quad(8.0, 4.0, 2.0) == False

    assert merge([1, 3, 3, 5], [3, 5, 5, 7]) == [1, 3, 3, 3, 5, 5, 5, 7]
    assert MergeSort([3, 1, 3, 5]) == [1, 3, 3, 5]

    assert is_equal([1, 2], [1, 2], [1, 2]) == True

    assert numpy.array_equal(rot_vec([1, 2, 3, 4, 5, 6]), numpy.array([[1], [2], [3], [4], [5], [6]])) == True
    assert numpy.array_equal(rot_vec([1, 2]), numpy.array([[1], [2]])) == True

    assert numpy.array_equal(get_diag([[1, 2], [3, 4]]), numpy.array([1, 4])) == True
    assert numpy.array_equal(sec_diag([[1, 2], [3, 4]]), numpy.array([[2], [3]])) == True
    assert who_more() == 577
    print(statistic())
