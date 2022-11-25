# remember doing these in C++
import random
import string

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def printList(self):
    list = []
    cur_node = self.head
    while cur_node:
      list.append(cur_node.data)
      #print(cur_node.data)
      cur_node = cur_node.next
    print(*list)
    #visual printing cuz it cool
    print(str(list).replace(',', ' <- ').replace("[","").replace("]",""))

  #new head p much
  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node

  #whaaaaa
  def prepend(self, data):
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node

  #delete based off value
  def deleteNodeVal(self, key):

    cur_node = self.head

    if cur_node and cur_node.data == key:
      self.head = cur_node.next
      cur_node = None
      return

    prev = None
    while cur_node and cur_node.data != key:
      prev = cur_node
      cur_node = cur_node.next

    if cur_node is None:
      return

    prev.next = cur_node.next
    cur_node = None

  #delete based off pos
  def deleteNodePos(self, pos):
    if self.head:
      cur_node = self.head

      if pos == 0:
        self.head = cur_node.next
        cur_node = None
        return

      prev = None
      count = 0
      while cur_node and count != pos:
        prev = cur_node
        cur_node = cur_node.next
        count += 1

      if cur_node is None:
        return

      prev.next = cur_node.next
      cur_node = None

  def length(self, node):
    if node is None:
      return 0
    return 1 + self.length(node.next)

  def swapNodes(self, key_1, key_2):

    if key_1 == key_2:
      return

    prev_1 = None
    curr_1 = self.head
    while curr_1 and curr_1.data != key_1:
      prev_1 = curr_1
      curr_1 = curr_1.next

    prev_2 = None
    curr_2 = self.head
    while curr_2 and curr_2.data != key_2:
      prev_2 = curr_2
      curr_2 = curr_2.next

    if not curr_1 or not curr_2:
      return

    if prev_1:
      prev_1.next = curr_2
    else:
      self.head = curr_2

    if prev_2:
      prev_2.next = curr_1
    else:
      self.head = curr_1

    curr_1.next, curr_2.next = curr_2.next, curr_1.next



llist = LinkedList()
for i in range(10):
  #llist.append(random.randint(1, 100))
  llist.append((random.choice(string.ascii_letters)).upper())


llist.prepend("D")
llist.printList()
llist.deleteNodeVal("T")
llist.deleteNodePos(0)
llist.printList()

print(llist.length(llist.head))