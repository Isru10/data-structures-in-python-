class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self) :
        self.head=None
    def printlist(self):
        temp=self.head
        while(True):
            print(temp.data)
            temp=temp.next
    def searchll(self,sdata):
        current=self.head
        while current.next!=None:
            if current.data==sdata:
                print( 'found it ')
    def getnth(self,index):
            current=self.head
            count=0
            while current:
                if count==index:
                    return current.data
                count+=1
                current=current.next
            assert(False)
    def lengthllst(self):
        counter=1
        temp=self.head
        while temp.next!=None:
            temp=temp.next
            counter+=1

        print (counter)
    def push (self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def insertafter(self,prev_node,new_data):
        if prev_node is None:
            print('impossible')
            return 
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
    def append(self, new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
    def deleteatpos(self,position):
        index=0
        current=self.head
        while index<position and current.next:
            previous=current
            current=current.next
            index+=1
        if index<position:
            print('index out of bound ')
        elif(index==0):
            current=current.next
        else:
            previous.next=current.next
    def delete_last(self):
        temp=self.head
        while(temp.next !=None and temp.next.next!=None):
            temp=temp.next
        temp.next=None
    def delete_first(self):
        temp=self.head
        self.head=self.head.next
        temp=None
    def delete_all(self):
        current=self.head
        while current:
            next_current=current.next
            del(current.data)
            current=next_current
if __name__=='__main__':
    llst=Linkedlist()
    llst.head=Node(1)
   
    second=Node(2)
    third=Node(3)
    llst.head.next=second
    second.next=third
    llst.append(4)
    llst.append(5)
    llst.append(6)
    #llst.deleteatpos(2)
    #llst.searchll(0)
   # llst.lengthllst()
    #llst.delete_first()
    #llst.delete_all()
    #llst.printlist()
    print(llst.getnth(2))


'''nums = [0,0,1,1,1,2,2,3,3,4]
for i in range(len(nums)):
    for j in range(len(nums)+1):
        if (nums[i]==nums[j]):
           nums= nums.remove(nums[j])
print(len(nums))'''
