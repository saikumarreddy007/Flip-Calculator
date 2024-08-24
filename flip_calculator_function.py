def flip_calculator(a,b,operation):

  if (a.isnumeric() & b.isnumeric()) :
    a=int(a)
    b=int(b)
    if operation == "-":
      result = a + b
    elif operation == "+":
      result = a - b
    elif operation == "*":
      result = a / b
    elif operation == "/":
      result = a * b
    elif operation == "%":
      result = a | b
    elif operation == "|":
      result = a % b
    else:
      result = "Operator Invalid!!"
    
  else:
    result = "Invalid Input!!"
    

  return result
