# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:32:45 2018

@author: wangyang
"""
import numpy as np

class BinTree():
    def __init__(self,liftchildren = None,rightchildren = None, content = None, distance = None):
        self.__liftchildren = liftchildren
        self.__rightchildren = rightchildren
        self.__content = content
        self.__distance = distance
        
    def getLiftChildren(self):
        return self.__liftchildren
    
    def getRightChildern(self):
        return self.__rightchildren
    
    def getdistance(self):
        return self.__distance 
    
    def insertChildren(self,liftchildren = None,rightchildren = None):
        if not(liftchildren is None):
            self.__liftchildren = liftchildren
        
        if not(rightchildren is None):
            self.__rightchildren = rightchildren
    
    def showBinTree():
        pass
    
class NeighborJoining():
    def __init__(self,position,calculationMethon,JoiningMethon):
        self.__position = position
        self.__CalculationMethon =calculationMethon
        self.__DistanceMatrix = self.__getDistanceMatrix()
        self.__JoiningMethon = JoiningMethon
        self.__treeDictionaries = {}
        
    def distanceArr(self,position,point):
        distance = []
        for i in position:
            distance.append(self.__CalculationMethon(i,point))
            
        return np.asarray(distance,dtype = 'float')
    
    def __getDistanceMatrix(self):
        distance_Matrix = []
        i=0
        for  point in self.__position:
            distance_Matrix = np.insert(distance_Matrix,i,self.distanceArr(self.__position,point),0)
            i = i + 1
            
        return np.transpose(distance_Matrix)    
    
    def updateDistanceMatrix(self,deleteIndex=None, insertPoint=None):
        self.__position = np.delete(self.__position,deleteIndex,0)
        m,n = self.__position.shape
        self.__position = np.insert(self.__position,m,insertPoint,0)
        
        self.__DistanceMatrix = np.delete(self.__DistanceMatrix,deleteIndex,0)
        self.__DistanceMatrix = np.delete(self.__DistanceMatrix,deleteIndex,1)
        m,n = self.__DistanceMatrix.shape
        insertdata = self.distanceArr(self.__position,insertPoint)
        self.__DistanceMatrix = np.insert(self.__DistanceMatrix,m,insertdata,0)
        
    def __initTreeNode(self):
        for point in self.__position:
            self.__treeDictionaries[str(point)] = BinTree(content = str(point))
        
    def builtTree(self):
        self.__initTreeNode()
        while(True):
            minvalue = np.min(self.__DistanceMatrix)
            m,n = np.where(self.__DistanceMatrix==minvalue)
            deleteIndex = [m[0],n[0]]
            newNode = self.__JoiningMethon(self.__position,m[0],n[0])
            
            liftchildren = self.__treeDictionaries[str(self.__position[deleteIndex[0]])]
            rightchildren = self.__treeDictionaries[str(self.__position[deleteIndex[1]])]
            newTree = BinTree(liftchildren,rightchildren,content = str(newNode),minvalue)

            self.__treeDictionaries[str(newNode)] = newTree
            self.updateDistanceMatrix(deleteIndex,newNode)
            
            m,n = self.__position.shape
            
            if n==1:
                break
        rootNode = newTree
        return rootNode