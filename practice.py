# class node:
#     def __init__(self,child_node, parent_node):
#          self.child_node = child_node
#          self.parent_node = parent_node
class Node:
    def append(self,node, new_data):
 
        new_node = Node(new_data)
 
        if self.head is None:
            self.head = new_node
        return



class node:
    def __init__(self,puzzle_list,parent,null,action):
        self.puzzle_list=puzzle_list
        self.parent=parent
        if(parent==null):
            self.g=self.parent.g+1
            self.f=0
    
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class Mycar(Car):
    def calltion(self,name):
        self.brand
        self.model
        self.name=name



# class LinkedList:
# 	def __init__(self,head=None):
# 		self.head = head    
# 		def append(self, new_node):
#             current = self.head
#             if current:
#                 while current.next:
#                     current = current.next
#                 current.next = new_node
#             else:
#                 self.head = new_node