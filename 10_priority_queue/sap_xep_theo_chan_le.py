import queue
class item:
    # hàm tạo trong class luôn là __init__ 
    def __init__(seft, d=0): seft.data = d

    # xét - nếu chắn thì xếp trước 
    def __lt__(seft, other):
        if seft.data%2 != other.data%2: 
            return seft.data%2 < other.data%2
        if seft.data%2 ==0 : 
            return seft.data < other.data
        return seft.data > other.data
    
q = queue.PriorityQueue()
for x in 42, 34, 63, 435, 85, 726, 435 , 85 , 726:
    q.put(x)
while(q.qsize()):
    print(q.get().data , end=' ')