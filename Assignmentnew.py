matrix = [
    [True, 34, 5, 'School'],
    [8, 23, 20, 11, 37, 55, 17],
    ['book', 'mosh', 'arc', 'photo'],
    [-1, 'Mani']
]
 
#for c in matrix[2]:
#      print(c.upper()) 
for c in matrix:
      for j in c:
         if type(j)==str:     
          print(j.upper())
#      for j in c:
#         if type(c)==int:    
#           print(c)
           
            
for c in matrix[1]:
      print(c)     
     