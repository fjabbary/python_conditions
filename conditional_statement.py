number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
    
    
# ================================================== 
# ================================================== 
# ================================================== 
min = None
max = None
num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))
num3 = int(input("What is the third number? "))

if num1 >= num2 and num1 >= num3:
  max = num1
elif num2 >= num1 and num2 >= num3:
  max = num2
elif num3 >= num1 and num3 >= num2:
  max = num3
  
# ================================================== 
  
if num1 <= num2 and num1 <= num3:
  min = num1 
elif num2 <= num1 and num2 <= num3:
  min = num2
elif num3 <= num1 and num3 <= num2:
  min = num3   
  
print(f"Min number is {min}")
print(f"Max number is {max}")



  