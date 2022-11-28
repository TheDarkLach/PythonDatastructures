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

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def printnth(self, n):

        p = self.head
        q = self.head

        if n > 0:
            count = 0
            while q:
                count += 1
                if(count>=n):
                    break
                q = q.next
                
            if not q:
                print(str(n) + " is greater than the number of nodes in list.")
                return

            while p and q.next:
                p = p.next
                q = q.next
            return p.data
        else:
            return None


    def palindrome(self):
        if self.head:
            p = self.head 
            q = self.head 
            prev = []
            
            i = 0
            while q:
                prev.append(q)
                q = q.next
                i += 1
            q = prev[i-1]

            count = 1

            while count <= i//2 + 1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return True

llist = LinkedList()
list2=LinkedList()

llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

list2.append("A")
list2.append("B")
list2.append("C")
list2.append("B")
list2.append("A")

print(llist.printnth(4))
print(llist.printnth(2))
print(llist.palindrome())
print(list2.palindrome())