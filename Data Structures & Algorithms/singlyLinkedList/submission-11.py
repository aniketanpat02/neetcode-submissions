class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        while curr:
            if i==index:
                return curr.data
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node=Node(val)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        
        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = new_node
        

    def remove(self, index: int) -> bool:
        prev_ele = None
        next_ele = None
        curr = self.head 
        i = 0
        if self.head is None:
            return False
        while curr:
            if index == 0:
                self.head = self.head.next
                return True
            if i == index - 1:
                prev_ele = curr
            if i == index + 1:
                next_ele = curr 
            curr = curr.next
            if curr:
                i += 1

        if i < index:
            return False
        elif prev_ele:
            prev_ele.next = next_ele
            return True
        else:
            prev_ele.next = next_ele
            return True
        

    def getValues(self) -> List[int]:
        array = []
        curr = self.head
        while curr:
            array.append(curr.data)
            curr = curr.next
        return array


class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        
