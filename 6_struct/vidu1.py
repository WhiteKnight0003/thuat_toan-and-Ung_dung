from collections import namedtuple
sv = namedtuple(typename="sinhvien", field_names='ten,tuoi,diem')

A = sv("tran anh", 15, 3.5)
print(A)
print(A.ten)
print(A.tuoi)
print(A.diem)