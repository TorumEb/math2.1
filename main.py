import numpy as np


# создание матрицы смежности для ориентированного графа
def createAdjacencyMatrixOriented(top, count_top, count_ribs):
    currentMatrix = np.zeros((count_top, count_top))
    for i in range(0, count_ribs):
        first_top = int(top[i][0] - 1)
        second_top = int(top[i][1] - 1)
        currentMatrix[first_top][second_top] = 1
    return currentMatrix


# проверяем рефлексиность(главную диагональ)
def isReflexive(adjacencyMatrix, count_top):
    flag = 0
    for i in range(0, count_top):
        if adjacencyMatrix[i][i] == 0:
            flag += 1
    if flag == 0:
        return True
    else:
        return False


# анти рефлексивность(на главной диагонали нули)
def isAntiReflexive(adjacencyMatrix, count_top):
    flag = 0
    for i in range(0, count_top):
        if adjacencyMatrix[i][i] == 0:
            flag += 1
    if flag == count_top:
        return True
    else:
        return False


# транзитивность(проверяем все тройки вершин)
def isTransitivity(adjacencyMatrix, count_top):
    for i in range(0, count_top):
        for j in range(i + 1, count_top):
            for k in range(0, count_top):
                n = 0
                if j != k and i != k:
                    n = adjacencyMatrix[i][j] \
                        + adjacencyMatrix[i][k] + adjacencyMatrix[j][k]
                if n == 2:
                    return False
    return True


# симметричность(сравниваем симметричные элементы матрицы смежности)
def isSymmetry(adjacencyMatrixOriented, count_top):
    for i in range(0, count_top):
        for j in range(0, count_top):
            if adjacencyMatrixOriented[i][j] != adjacencyMatrixOriented[j][i]:
                return False
    return True


if __name__ == "__main__":
    count_top, count_ribs = map(int, input().split())
    massive = np.zeros((count_ribs, 2))
    for i in range(0, count_ribs):
        entered_list = input().split()
        massive[i][0] = entered_list[0]
        massive[i][1] = entered_list[1]
    adjacencyMatrixOriented = createAdjacencyMatrixOriented(massive, count_top, count_ribs)

    if isReflexive(adjacencyMatrixOriented, count_top):
        print("Reflexive")
    else:
        print("Not Reflexive")

    if isAntiReflexive(adjacencyMatrixOriented, count_top):
        print("AntiReflexive")
    else:
        print("Not AntiReflexive")

    if isTransitivity(adjacencyMatrixOriented, count_top):
        print("Transitivity")
    else:
        print("Not Transitivity")

    if isSymmetry(adjacencyMatrixOriented, count_top):
        print("Symmetry")
    else:
        print("Not Symmetry")
