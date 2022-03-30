import turtle 

def graph_data(upperend_bound=0):
  window = turtle.Screen()
  window.setworldcoordinates(0,0,10,10)
  myturtle = turtle.Turtle()
  myturtle_writer = turtle.Turtle()
  myturtle.speed(0)
  myturtle_writer.speed(0)
  max_so_far = 0
  for start in range(1,upperend_bound+1):
    result = seq3np1(start)
    myturtle.pendown()
    myturtle_writer.pendown()
    myturtle.goto(start,seq3np1(start))
    if max_so_far <= result:
      max_so_far = result
      myturtle_writer.clear()
      myturtle_writer.pendown()
      myturtle_writer.goto(0,max_so_far)
      myturtle_writer.write("Maximum so far:"+"<"+str(start)+">,<"+str(max_so_far)+">", align = "left", font=("Arial",8,"normal"))
      window.setworldcoordinates(0,0,start+10,max_so_far+10)
  
  window.exitonclick()
#PARTA
def seq3np1(n):
  count = 0
  while n != 1:
    if (n % 2 == 0):       # n is even
      n = n // 2
    else:                 # n is odd
      n = n * 3 + 1
    count+=1
  return count

def main():
  upperend_bound = int(input("What positive value do you want?"))
  if (upperend_bound > 0):
    for start in range(1,upperend_bound+1):
      print("Current Loop Value: " + str(start) + " and Number of Iterations: " + str(seq3np1(start)))
    graph_data(upperend_bound)
  else:
    quit()

main()