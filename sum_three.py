# sum_three = [0, 1, 2]
# appendsums(sum_three)
# print sum_three[10]

def appendsums(sum_three):  
     """  
     Repeatedly append the sum of the current last three elements  
     of lst to lst.  
     """ 
     # итерация списка с добавлением суммы последних трех элементов
     # loop 25 times
     i = 0
     while i <= 25: 
         lst = sum_three[-1] + sum_three[-2] + sum_three[-3] 
         sum_three.append(lst)
         i += 1
     print(sum_three)

sum_three = [0, 1, 2]
appendsums(sum_three)
print(sum_three[20])