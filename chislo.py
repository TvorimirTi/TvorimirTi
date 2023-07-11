def get_largest_num(n1, n2, n3):
 if (n1 >= n2) and (n1 >= n2):
   return n1
 elif (n2 >= n1) and (n2 >= n3):
   return n2
 else:
   return n3

print(get_largest_num(1, 3, 2)) # 3

print(max(3, 1, 2))
