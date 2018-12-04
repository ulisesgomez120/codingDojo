class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class slist:
    def __init__(self,value):
        node = Node(value)
        self.head = node
    def add_node(self,value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node
        return self
    def remove_node(self,value):
        runner = self.head
        if runner.value == value:
                self.head = runner.next
        while (runner.next != None):
            if runner.next.value == value:
                if runner.next.next == None:
                    runner.next = None
                    return self
                else:
                    runner.next = runner.next.next
            runner = runner.next
        return self
    def print_values(self, msg=""):
        runner = self.head
        print("\n head points to ", id(self.head))
        print("printing the values in the list ---", msg, "---")
        while (runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next
        print(id(runner), runner.value, id(runner.next))
        return self
s = slist(3)
s.add_node(6).add_node(7).add_node(2).add_node(12).add_node(1).add_node(8).print_values().remove_node(1).print_values()