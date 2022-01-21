#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#task4
import random


import ctypes

class array:
    def __init__(self,size):
        assert size>0,"Array size must be greater than 0"
        
        self.size = size
        pyarray = ctypes.py_object * size
        self.element = pyarray()
        
        self.clear(None)
        
    def __len__(self):
        return self.size
    
    def clear(self,value):
        for i in range(self.size):
            self.element[i] = value
    
    def __iter__(self):
        return arrayiterator(self.element)
    
    def __getitem__(self,i):
        assert i>=0 and i <len(self), "out of range"
        return self.element[i]

    def __setitem__(self, i, value):
        assert i>=0 and i <len(self), "out of range"
        self.element[i] = value
            
class arrayiterator:
    def __init__(self,array):
        self.arrayref = array
        self.node = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.node < len(self.arrayref):
            entry = self.arrayref[self.node]
            self.node +=1
            return entry
        else:
            raise StopIteration
        


        
class Array2d:
    
    def __init__(self, numRows, numCols):
        self.rows = array(numRows)
        for i in range(numRows):
            self.rows[i] = array(numCols)
            
    def numRows(self):
        return len(self.rows)
        
    def numCols(self):
        return len(self.rows[0])
        
    def clear(self, value):
        for row in range(self.numRows()):
            self.rows[row].clear(value)
            
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "number of arrays is invalid"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row>=0 and row <self.numRows() and col >= 0 and col<self.numCols(), "Values out of range"
        array1d = self.rows[row]
        return array1d[col]
        
    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "number of arrays is invalid"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row>=0 and row <self.numRows() and col >= 0 and col<self.numCols(), "Values out of range"
        array1d = self.rows[row]
        array1d[col] = value
        

class gamegrid:
    deadcell = "."
    livecell = "@"
    def __init__(self,numrows,numcols):
        self.grid = Array2d(numrows,numcols)
        self.configure(list())
    def numofrow(self):
        return self.grid.numRows()
    def numofcol(self):
        return self.grid.numCols()
    
    def configure(self,coordlist):
        for i in range(self.numofrow()):
            for j in range(self.numofcol()):
                self.clear(i,j)
                
        for coord in coordlist:
            self.setcellLive(coord[0],coord[1])
    def setcellLive(self,row,col):
        self.grid[row,col] = gamegrid.livecell
                
    def clear(self,r,c):
        self.grid[r,c] = gamegrid.deadcell
    def isLiveCell(self,row,col):
        return self.grid[row,col] == gamegrid.livecell
    def isDeadCell(self,row,col):
        return self.grid[row,col] == gamegrid.deadcell
    
    def numofLiveNeighbours(self,r,c):
        count =0
        
        chk = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        
        for i in chk:
            
            
            x = i[0] + r
            y = i[1] + c
            
            if x>= 0 and x <self.numofrow() and y>=0 and y<self.numofcol() and self.grid[x,y]=="@":
                count +=1
            
            
        
        return count
    
    
    def lives(self):
        self.counting = 0
        for i in range(self.numofrow()):
            for j in range(self.numofcol()):
                if self.grid[i,j] == "@":
                    self.counting +=1
        return self.counting
        
    def evolve(self):
        
        
        self.livecells = list()
        
        for i in range(self.numofrow()):
            for j in range(self.numofcol()):
                    
                neighbors = self.numofLiveNeighbours(i,j)
                
                if (neighbors ==2 and self.isLiveCell(i,j)) or neighbors == 3:
                    self.livecells.append((i,j))
        self.configure(self.livecells)
        self.lives()
        
        
        
    def draw(self):
        for r in range(self.numofrow()):
            print("")
            for c in range(self.numofcol()):
                print(self.grid[r,c],end="")
                
    def evolve_untill_noLiveCells(self):
        l= self.lives()
        
        while self.lives() != 0:
            self.evolve()
            print("")
            self.draw()
            new = self.lives()
            if new == l:
                break
            else:
                
                l = new
                
            
            
            
obj = gamegrid(6,6)
obj.configure([(random.randint(0,5),random.randint(0,5)),(random.randint(0,5),random.randint(0,5)),(random.randint(0,5),random.randint(0,5)),(random.randint(0,5),random.randint(0,5)),(random.randint(0,5),random.randint(0,5)),(random.randint(0,5),random.randint(0,5)),(random.randint(0,5),random.randint(0,5)),(random.randint(0,5),random.randint(0,5))])
obj.draw()
print("")
#print(obj.grid[1,1])
#print(obj.numofLiveNeighbours(2,3))

obj.evolve_untill_noLiveCells()
print("")

