import array as arr
class Queue:
    def __init__(self,size):
        self.que=arr.array('i',[])
        self.rear=-1
        self.front=-1
        self.size=size
    def qenqueue(self):
        if self.rear==-1 and self.front==-1:
            self.rear=self.front=0
        elif self.rear==self.size:
            print("Queue is full")
            return

        self.rear+=1
        val=int(input("Enter value to enqueue: "))
        self.que.append(val)
        
    def qdequeue(self):
        if self.front==self.rear or self.front==-1:
            print("Queue is empty")
        else:
            self.que.pop(0)
            self.front+=1
            
    def display(self):
        for i in self.que:
            print(i,end="  ")
        print("")

q=Queue(4)
print("Queue: \n 1.Add\n 2.Delete\n 3.Display\n 4.Exit\n")
while(True):
    ch=int(input("Enter choice: "))
    if ch==1:
        q.qenqueue()
    elif ch==2:
        q.qdequeue()
    elif ch==3:
        q.display()
    else:
      print("End of Process.")
      break
      exit()
