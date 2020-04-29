# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:44:47 2020

@author: USER
"""
# %% class

class HeapTree:
    
    def __init__(self):
        self.nodes =  []
        self.heapSize = 0
    # Up heap is necessary operation after the adding new elements to the heap
    def upHeap(self):
        i = self.heapSize - 1
        flag = True
        while i > 0 and flag:
            # if i is even, we should look at the (i -2 )/2
            if i % 2 == 0:   
                k = (i - 2) / 2
            # if i is odd, we should look at the (i-1)/2
            else:
                k = (i - 1) / 2
            k = int(k)
            if k >= 0 and self.nodes[k] > self.nodes[i]:
                tmp = self.nodes[k]
                self.nodes[k] = self.nodes[i]
                self.nodes[i] = tmp
                i = k
                
            else:
                flag = False
    # Down heap is necessary operation after the removing an elements from the heap
    def downHeap(self):
        i = 0
        flag = True
        while i < self.heapSize and flag:
            left_child_index = 2 * i + 1
            right_child_index = 2 * i + 2
            if right_child_index < self.heapSize:
                if self.nodes[right_child_index] < self.nodes[left_child_index]:
                    min_child = right_child_index
                else:
                    min_child = left_child_index
            elif left_child_index < self.heapSize:
                min_child = left_child_index
            else:
                min_child = i
            
            if self.nodes[i] > self.nodes[min_child]:
                tmp = self.nodes[i]
                self.nodes[i] = self.nodes[min_child]
                self.nodes[min_child] = tmp
                i = min_child
            else:
                flag = False
    # This method has to be used for adding new elements to the heap tree            
    def addElement(self,val):
        self.nodes.append(val)
        self.heapSize += 1
        self.upHeap()
    # This method has to be used for removing an element from the heap
    # This method returns root of the tree which has the minimum value
    def removeElement(self):
        if self.heapSize > 0:
            # Swapping between first and last element in the heap
            min_value = self.nodes[0]
            self.nodes[0] = self.nodes[self.heapSize-1]
            self.nodes[self.heapSize-1] = min_value
            self.nodes.pop((self.heapSize-1))
            # We should decrease the heap size
            self.heapSize -= 1
            self.downHeap()

            return min_value
        else:
            return None
    # This method is written to write the elements of the heap tree
    def writeElements(self):
        list1 = []
        for i in range(self.heapSize):
            list1.append(self.nodes[i])
        print(list1)
# %% Example

def Test_Method():
    heap = HeapTree()
    heap.addElement(5)
    heap.writeElements()
    heap.addElement(3)
    heap.writeElements()
    heap.addElement(4)
    heap.writeElements()
    heap.addElement(1)
    heap.writeElements()
    
    print("remove edilen eleman --->",heap.removeElement())
    heap.writeElements()
    
    
    print("remove edilen eleman --->",heap.removeElement())
    heap.writeElements()
    # to left ---> 2*k+1
    # to right --->2*k+2
    
