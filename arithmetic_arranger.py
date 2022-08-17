# OPERATORS
def add(num1, num2):
  return int(num1) + int(num2)

def sub(num1, num2):
  return int(num1) - int(num2)

ops = {
  "+": add,
  "-": sub
}

# MAIN
def arithmetic_arranger(list, *perform):
  if len(list) > 5:
    return "Error: Too many problems."

  formatted = [[],[],[],[]]
  for msg in list:
    msg = msg.split(" ")

    num1 = msg[0]
    num2 = msg[2]
    if not num1.isdigit() or not num2.isdigit():
      return "Error: Numbers must only contain digits."

    arti = msg[1]
    if arti not in ops:
      return "Error: Operator must be '+' or '-'."

    length = len(num1) if len(num1) > len(num2) else len(num2)
    if length > 4:
      return "Error: Numbers cannot be more than four digits."
    length += 2

    formatted[0].append(num1.rjust(length))
    formatted[1].append(num2.rjust(length).replace(" ", arti, 1))
    formatted[2].append("-"*length)
    formatted[3].append(str(ops[arti](num1, num2)).rjust(length))

  if len(perform) == 0 or perform[0] == False:
    formatted.pop()

  x = '{:}    '*len(list)
  x = x.strip()

  var = []
  for row in formatted:
    var.append(x.format(*row))
  
  return "\n".join(var)

# TEST
# print(arithmetic_arranger(["10 + 32", "14 - 3222", "110 + 32"], True))
