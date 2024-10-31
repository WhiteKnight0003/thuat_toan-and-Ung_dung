from queue import LifoQueue
s = LifoQueue()
s_str =''
ut = {'(':0, '+':1, '-':1, '*':2, '/':2, '%':2}
str_in=input()
for x in str_in:
    if x=='(': s.put(x)
    elif '0'<=x<='9':
        s_str+=x
    elif x ==')':
        while(s.queue[-1] !="(" ):
            s_str+=s.get()
        s.get();  # xóa ngoặc (
    else:
        while s.qsize()>0 and ut[s.queue[-1]] >=ut[x]: s_str+=s.get()
        s.put(x)
while s.qsize(): s_str +=s.get()
print(s_str)
y = str_in.replace('/','//')
print(eval(y))



