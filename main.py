import turtle 

window = turtle.Screen()
myturtle = turtle.Turtle()
myturtle_writer = turtle.Turtle()
myturtle.speed(0)
myturtle_writer.speed(0)

def setupWindowTurtles(myturtle=None,myturtle_writer=None, window=None,max_so_far=0,upperend_bound = 0):
  myturtle.clear()
  myturtle_writer.clear()
  myturtle.goto(0,0)
  myturtle.pendown()
  myturtle_writer.pendown()
  myturtle_writer.clear()
  max_so_far = 0
  window.setworldcoordinates(0,0,upperend_bound+10,max_so_far+10)
  myturtle_writer.goto(0,max_so_far+10)
  for i in (1,upperend_bound+1):    
    myturtle.goto(i,seq3np1(i))
  
#PartB
def upperboundgraph(upperend_bound = 0, count = 0):
  max_so_far = 0
  for i in (1,upperend_bound+1):
    seq3np1(i)
    result = seq3np1(upperend_bound+1,)
    max_so_far += 1
  if max_so_far < result:
    max_so_far = result
    
#PARTA
def seq3np1(n):
  count = 0
  while n != 1:
    if(n % 2) == 0:        # n is even
      n = n // 2
      count += 1
    else:                 # n is odd
      n = n * 3 + 1
      count += 1 # the last print is 1
    count+=1
  return count

#myturtle_writer.write("Maximum so far:"max_so_far, font=Arial,8,normal)


def main():
  window.setworldcoordinates(0,0,10,10)
  upperend_bound = int(input("What positive value do you want?"))
  if 0<upperend_bound:
    for start in range(1,upperend_bound+1):
      seq3np1(start)
      print("Current Loop Value:", start ,"and Number of Iterations:",seq3np1(start)) 
  else:
    quit()
  upperboundgraph(0,0)
  setupWindowTurtles(myturtle,myturtle_writer,window,0,0)

main()