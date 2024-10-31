dictSinh = { 'Kim':'Thuy','Thuy':'Moc','Moc':'Hoa','Hoa':'Tho', 'Tho':'Kim' }
dictKhac = { 'Kim':'Moc','Thuy':'Hoa','Moc':'Tho','Hoa':'Kim', 'Tho':'Thuy' }

str1,str2 = map(str, input().split())
if dictSinh.get(str1)!=None and dictSinh[str1]== str2 :
    print(f'{str1} sinh {str2}')
elif dictSinh.get(str2)!=None and dictSinh[str2]== str1 :
    print(f'{str2} sinh {str1}')
elif dictKhac.get(str1)!=None and dictKhac[str1]== str2 :
    print(f'{str1} khac {str2}')
elif dictKhac.get(str2)!=None and dictKhac[str2]== str1 :
    print(f'{str2} khac {str1}')