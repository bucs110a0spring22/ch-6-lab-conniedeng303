def seq3np1(n):
  count = 0
  while n != 1:
    print(n)
    if(n % 2) == 0:        # n is even
      n = n // 2
      count += 1
    else:                 # n is odd
      n = n * 3 + 1
      print(n)  
      count += 1 # the last print is 1
  print("the count should be" ,count)
  

def main():
	seq3np1(10)
main()
