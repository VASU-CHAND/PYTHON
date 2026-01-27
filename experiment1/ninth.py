sec= int (input("enter the seconds\n"))
min= int (sec/60)
sec= int (sec%60)
hours= int (min/60)
min= int (min%60)
print(hours , ":" , min ,":" , sec)

