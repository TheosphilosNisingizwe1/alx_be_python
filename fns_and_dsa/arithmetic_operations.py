def perform_operation(num1, num2, operation):
 if operation == "addition":
  return num1 + num2
 elif operation == "subtraction":
  return num1 - num2
 elif operation == "multiply":
  return num1 * num2
 elif operation == "division":
  match num2:
   case 0:
     print("Can't divide by zero")
   case _:
    return num1 / num2
 else:
  print("Invalid input")  
