# Michael L. Kelley Jr.
# June 26, 2023
# infinite-loop.py
# A while loop that never stops running

x = 0

while x % 2 == 0:
    x = x / 2
    print("Stuck in a loop!!!")
    
    