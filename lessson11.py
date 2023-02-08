#def summ(a, b):
   #result = a + b
  # print("Result: ", result)
#summ(5, 7)

nums = [11, 4, 0.02, 6, 77, 33, 90, 2, 678, 3, 0.1]

min2 = nums[0]

for el in nums:
   if el < min2:
      min2 = el 
print(min2)


func = lambda x, y: x * y
result = func(5, 7)
print(result)