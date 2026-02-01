def perform_operation(num1, num2, operation):
 if operation == "addition":
  return num1 + num2
 elif operation == "subtraction":
  return num1 - num2
 elif operation == "multiply":
  return num1 * num2
 elif operation == "division":
  if num2 == 0:
   print("Can't divide by zero")
  else: 
   return num1 / num2
 else:
  print("Invalid input")  
