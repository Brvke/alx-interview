#!/usr/bin/python3
""" a module for the rotate_2d_matrix function """


def rotate_2d_matrix(matrix):
    n = len(matrix)
    
    # transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
