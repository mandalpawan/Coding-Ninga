class node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class Linklist:
    def __init__(self):
        self.start = None
    def listView(self):
        if(self.start== None):
            print("This is a empty list ")
        else:
            temp = self.start
            while(temp != None):
                print(temp.data,end=' ')
                temp = temp.next
    
    def insertLast(self,value):
        newNode = node(value)
        if(self.start==None):
            self.start = newNode
        else:
            temp = self.start
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
    def check(self):
        temp= self.start
        ls = []
        while temp:
            cur_node = temp
            count = 0
            while cur_node: 
                if cur_node.data == temp.data:
                    #print(count,cur_node.data)
                    ls.append(count)
                count+=1
                cur_node= cur_node.next
            print(max(ls)-1)
            temp = temp.next
            


mylist = Linklist()
my_string = input("Enter string")
for i in my_string:
    mylist.insertLast(i)
mylist.listView()
mylist.check()

