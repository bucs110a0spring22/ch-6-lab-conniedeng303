import turtle 

window = turtle.Screen()
myturtle = turtle.Turtle()
myturtle_writer = turtle.Turtle()
myturtle.speed(0)
myturtle_writer.speed(0)

def setupWindowTurtles(myturtle=None,myturtle_writer=None,window = None, upperend_bound = 0):
  myturtle.clear()
  myturtle_writer.clear()
  myturtle.penup()
  myturtle_writer.penup()
  myturtle.goto(0,0)
  myturtle_writer.goto(0,0)
  myturtle.pendown()
  myturtle_writer.pendown()
  
def graph_data(myturtle=None,myturtle_writer=None,window=None,upperend_bound=0):
  setupWindowTurtles(myturtle,myturtle_writer,window,upperend_bound=0)
  max_so_far = 0
  for start in (1,upperend_bound+1):
    myturtle.clear()
    myturtle_writer.clear()
    result = seq3np1(start)
    myturtle.pendown()
    myturtle_writer.pendown()
    myturtle.goto(start,seq3np1(start))
    if max_so_far < result:
      max_so_far = result
  myturtle_writer.pendown()
  myturtle_writer.goto(0,max_so_far)
  myturtle_writer.write("Maximum so far:"+"<"+ str(start)+">,<"+str(max_so_far)+">", align = "left", font=("Arial",8,"normal"))
  window.setworldcoordinates(0,0,start+10,max_so_far+10)
    
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
  return count

def main():
  setupWindowTurtles(myturtle,myturtle_writer,window,upperend_bound=0)
  window.setworldcoordinates(0,0,10,10)
  upperend_bound = int(input("What positive value do you want?"))
  if 0<upperend_bound:
    for start in range(1,upperend_bound+1):
      print("Current Loop Value:", start ,"and Number of Iterations:",seq3np1(start)) 
  else:
    quit()
  graph_data(myturtle,myturtle_writer,window,0)
  window.exitonclick()

  
main()