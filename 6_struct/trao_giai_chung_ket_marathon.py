from collections import namedtuple
sv = namedtuple(typename="sinhvien", field_names='ten,diem')

D = [] #ddt
K =[] # khác
for i in range(int(input())):
    s = input()
    # ten , diem , khoa = s.rsplit('', 2) - or 
    *a , diem , khoa = s.split()
    ten =" ".join(a)
    if khoa=="DDT":
        D.append(sv(ten, int(diem)))
    else:
        K.append(sv(ten, int(diem)))
D.sort(key = lambda x: x.diem, reverse=True) #sx giảm theo điểm
print("Giai nhat :%s"%D[0].ten)
print("Giai nhi :%s"%D[1].ten)
print("Giai ba :%s"%D[2].ten)
k=max(K,key= lambda x:x.diem)
print("Giai giao luu :%s"%k.ten)

