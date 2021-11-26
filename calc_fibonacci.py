def calc_fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  return calc_fibonacci(n-1) + calc_fibonacci(n-2)

num = int(input("数値を入力してください "))

for i in range(num + 1):
  print(i, calc_fibonacci(i))
