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

  def print_list(self):
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
  def delete_node_value(self, key):

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
  def delete_node_pos(self, pos):
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



llist = LinkedList()
for i in range(10):
  #llist.append(random.randint(1, 100))
  llist.append((random.choice(string.ascii_letters)).upper())


llist.prepend("D")
llist.print_list()
llist.delete_node_value("T")
llist.delete_node_pos(0)
llist.print_list()

print(llist.length(llist.head))