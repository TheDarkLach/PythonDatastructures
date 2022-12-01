class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def printList(self):
        list = []
        curr_node = self.head
        while curr_node:
            list.append(curr_node.data)
            #print(cur_node.data)
            curr_node = curr_node.next
        #print(*list)
        #visual printing cuz it cool
        print(str(list).replace(',', ' <-> ').replace("[","").replace("]",""))

    def delete(self, key):
        curr = self.head
        while curr:
            if curr.data == key and curr == self.head:
                # Case 1: Only 1 node present
                if not curr.next:
                    curr = None 
                    self.head = None
                    return

                # Case 2: deleting head node
                else:
                    nxt = curr.next
                    curr.next = None 
                    nxt.prev = None
                    curr = None
                    self.head = nxt
                    return 

            elif curr.data == key:
            # Case 3: Deleting node other than head where curr.next is not none
                if curr.next:
                    nxt = curr.next 
                    prev = curr.prev
                    prev.next = nxt
                    nxt.prev = prev
                    curr.next = None 
                    curr.prev = None
                    curr = None
                    return

                    # Case 4: same as 3 but curr.next is none
                else:
                    prev = curr.prev 
                    prev.next = None 
                    curr.prev = None 
                    curr = None 
                    return 
            curr = curr.next
    def reverse(self):
        tmp = None
        curr = self.head
        while curr:
            tmp = curr.prev
            curr.prev = curr.next
            curr.next = tmp
            curr = curr.prev
        if tmp:
            self.head = tmp.prev


dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)

dllist.printList()

dllist.delete(2)
dllist.printList()

dllist.reverse()
dllist.printList()