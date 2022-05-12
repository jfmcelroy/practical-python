# bounce.py
#
# Exercise 1.5
#A rubber ball is dropped from a height of 100 meters and each time it hits the ground, it bounces back up to 3/5 the height it fell
#Print the first 10 bounces

for i in range(11):
    print(i,round((3/5)**i * 100,4))
  
