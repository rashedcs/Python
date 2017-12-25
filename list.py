#n, k = map(int,input().split())   # jokhn aksathe 2 or more input nibo

Problem : Input a n number and n numbers of elements
    
Case - 1 :
    
#input : 
    5
    1 2 3 4 5
 #Output :
   [ 1 2 3 4 5]
  
n = int(input())
arr = list(map(int, input().split()))
print(arr)


Case 2 :
    input : 
      Number of element : 5
        1
        2
        3
        4
        5
        
     Output : [ 1 2 3 4 5]
        
num = int(input())
arr = list()

print("Enter elements :")

for i in range(num) :
  ele  = int(input())
  arr.append(ele)

print(arr)
