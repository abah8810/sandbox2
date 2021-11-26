def calc_fibonacci(n):
  f = []
  for i in range(n+1):
    if i == 0 or i == 1:
      f.append(i)
    else:
      f.append(f[i-1] + f[i-2])
  return f[-1]

num = int(input("数値を入力してください "))

for i in range(num + 1):
  print(i, calc_fibonacci(i))
