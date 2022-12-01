class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node


    def printList(self):
        #im not sure how to print this in the cool way cuz of the circular nature
        # A -> B -> C -> D -> E -> A -
        # |^                         |
        #  ---------------------------
        list = []
        curr = self.head

        while curr:
            #print(curr.data)
            list.append(curr.data)
            curr = curr.next
            if curr == self.head:
                break
        print(*list)

    """def printList(self):
        list = []
        cur_node = self.head
        while cur_node:
            list.append(cur_node.data)
            #print(cur_node.data)
            cur_node = cur_node.next
        print(*list)
        #visual printing cuz it cool
        print(str(list).replace(',', ' <- ').replace("[","").replace("]",""))"""
    def remove(self, key):
        if self.head:
            if self.head.data == key:
                cur = self.head 
                while cur.next != self.head:
                    cur = cur.next 
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head 
                prev = None 
                while cur.next != self.head:
                    prev = cur 
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next 
                        cur = cur.next


cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.printList()

cllist.remove("A")
cllist.printList()