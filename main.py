import random
class Node:
  def __init__(self, strPtr):
    self.strPtr = strPtr
    self.children = {}
    self.weights = {}
class AllNodes:
  def __init__(self, k):
    self.k = k
    self.nodes = {}
    self.nodeOcc = {}
  def addChild(self, parent, chr):
    newStrPtr = parent.strPtr[1:] + chr
    
    if not newStrPtr in self.nodes:
      self.nodes[newStrPtr] = Node(newStrPtr)
      self.nodeOcc[newStrPtr] = 0
    self.nodeOcc[newStrPtr] += 1
    newNode = self.nodes[newStrPtr]
    
    if not chr in parent.children: 
      parent.children[chr] = newNode
      parent.weights[chr] = 0
    parent.weights[chr] += 1
    return newNode
  def useString(self, txt):
    k = self.k
    startingStr = txt[:k]
    ptr = Node(startingStr)
    self.nodes[startingStr] = ptr
    self.nodeOcc[startingStr] = 0
    for i in range(k, len(txt)):
      newNode = self.addChild(ptr, txt[i])
      ptr = newNode
  def generateText(self, length):
    k = self.k
    txtOut = []
    startingStr = random.choices(list(self.nodeOcc.keys()), weights=list(self.nodeOcc.values()))[0]
    txtOut.append(startingStr)
    ptr = self.nodes[startingStr]
    for i in range(k, length):
      newChar = random.choices(list(ptr.weights.keys()), weights=list(ptr.weights.values()) )[0]
      txtOut.append(newChar)
      ptr = ptr.children[newChar]
    return ''.join(txtOut)
with open("tomsawyer.txt", 'r') as file:
     txt = str(file.read()).replace("\n", ' ').replace("_", '')
     file.close()
  
allnodes = AllNodes(8)
allnodes.useString(txt)
print(allnodes.generateText(250))
