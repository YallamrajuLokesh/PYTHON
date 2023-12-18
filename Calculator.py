def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def div(n1,n2):
  return n1/n2

def mul(n1,n2):
  return n1*n2

operator = {
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
}

n1=int(input("enter num1"))
n2=int(input("enter num2"))
for i in operator:
  print(i)

symbol=input("enter symbol")
calculation=operator[symbol]
print(f"{n1} {symbol} {n2} = {calculation(n1,n2)}")
