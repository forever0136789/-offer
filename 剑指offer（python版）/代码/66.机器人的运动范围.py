# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        matrix=[[True for j in range(cols)] for i in range(rows)]
        result=self.findgrid(threshold,matrix,rows,cols,0,0)
        return result
    
    def judge(self,threshold,i,j):
        if sum(map(int,str(i)+str(j)))<=threshold:
            return True
        else:
            return False
        
    def findgrid(self,threshold,matrix,rows,cols,i,j):
        count=0
        if i>=0 and i<rows and j>=0 and j<cols and self.judge(threshold,i,j) and matrix[i][j]:
            matrix[i][j]=False
            count=1+self.findgrid(threshold,matrix,rows,cols,i+1,j)+self.findgrid(threshold,matrix,rows,cols,i-1,j)+self.findgrid(threshold,matrix,rows,cols,i,j+1)+self.findgrid(threshold,matrix,rows,cols,i,j-1)
        return count
