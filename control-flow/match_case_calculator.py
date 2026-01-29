num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): " )
match operator:
 case "+":
  result = (num1 + num2)
 case "-":
  result = (num1 - num2)
 case "*":
  result = (num1 * num2)
 case "/":
  match num2:
   case "0":
    print("Can notndivide by zero")
   case _:
    result = (num1 / num2) 
 case _:
  print("Invalid inputs")
print(f"The result is {result}.")
