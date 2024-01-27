t = int(input())
l = ['A', 'B', 'C']
for i in range(t):
  a,b,c = list(input()), list(input()),list(input())
  al = a+b+c
  # print(al)
  for i in al:
    if al.count(i) > 1 and al.count(i) != 3:
      print(i)
      break
      