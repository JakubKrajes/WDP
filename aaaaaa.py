from typing import Any
class Node:
    def __init__(self, value=None, next=None):
        self.value=value
        self.next=next

class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value: Any):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node  # if list is empty, head and tail point to the same node (same value)
            self.tail = new_node
        else:
            new_node.next = self.head  # moves head to another node
            self.head = new_node  # new node has become the head

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node  # if list is empty, head and tail point to the same node (same value)
            self.tail = new_node
        else:
            self.tail.next = new_node  # moves tail to another node
            self.tail = new_node  # new node has become the tail

    def node(self, at: int) -> Node:
        index = 0
        if at == 0:
            return self.head
        if self.head is None:
            return None
        temp = self.head  # temp is at head
        while temp:
            if index == at:  # if we're looking for head (index 0), return head
                return temp
            index += 1
            temp = temp.next
        return temp

    def insert(self, value: Any, after: Node) -> None:
        if self.head is None:
            self.head = value  # if list is empty, it gives head the value
        new_node = Node(value)
        new_node.next = after.next  # connects new node with next node after the after
        after.next = new_node  # adds new node after the after

    def pop(self) -> Any:
        if self.head is None:
            self.tail = None
            return None
        temp = self.head
        self.head = self.head.next  # moves head to next node
        temp.next = None  # disconects temp from list
        if self.head.next is None:
            self.tail = None
        return temp.value

    def remove_last(self) -> Any:
        if self.head is None:
            return None
        temp = self.head
        temp_value = self.head
        while (temp.next):  # goes through next nodes
            temp_value = temp  # saves the last searched node value
            temp = temp.next  # moves to next node
        self.tail = temp_value  # saves new tail
        self.tail.next = None  # removes (pops) previous tail
        return temp.value

    def remove(self, after: Node) -> Any:
        temp = after.next  # temp to remove the node
        after.next = temp.next  # connects previous node with next node after the after node
        temp.next = None  # temp node gets removed

    def __str__(self):
        temp = self.head
        return_str = ""  # if head is empty, returns empty
        if temp is not None:
            while temp is not None:
                return_str += str(temp.value)  # adds value of temp node
                temp = temp.next  # moves to next node
                if temp is not None:
                    return_str += " -> "  # adds arrows between
        return return_str

    def __len__(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count


class Stack:
    def __init__(self,top=None):
        self._storage=top
        self.size=0

    def push(self, element:any):
        node=Node(element)

        if self._storage is None:
            self._storage=node
            self.size = self.size + 1
            return

        temp=self._storage
        self._storage=node
        node.next=temp
        self.size=self.size+1

    def pop(self):
        if self._storage is None:
            print("nie mozna pop, stack jest pusty")
            return

        value=self._storage

        self._storage=self._storage.next
        self.size = self.size - 1

        return value

    def __len__(self):
        return self.size

    def print(self):
        node = self._storage

        while node is not None:
            print(node.value)
            node = node.next


# stack=Stack()
# stack.push(10)
# stack.push(11)
# stack.push(12)
# stack.print()
# print("-------------")
# stack.pop()
# stack.print()
# print(len(stack))
class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def peek(self):
        return self._storage.node(0)  # looks at "head", so node 0

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)  # appends the element

    def dequeue(self) -> Any:
        return self._storage.pop()  # pops the queue

    def __len__(self):
        return len(self._storage)

    def __str__(self):
        return str(self._storage).replace(" -> ", ", ")  # replaces str from linked list


queue = Queue()

assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

assert str(queue) == 'klient1, klient2, klient3'


print(queue)