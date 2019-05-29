# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result=[]
        #行数
        n=len(matrix)
        #列数
        m=len(matrix[0])
        for q in range((min(m,n)+1)/2):
            [result.append(matrix[q][i]) for i in range(q,m-q)]
            [result.append(matrix[i][m-q-1]) for i in range(q,n-q) if matrix[i][m-q-1] not in result]
            [result.append(matrix[n-q-1][i]) for i in range(m-q-1,q-1,-1) if matrix[n-q-1][i] not in result]
            [result.append(matrix[i][q]) for i in range(n-q-1,q-1,-1) if matrix[i][q] not in result]
        return result
