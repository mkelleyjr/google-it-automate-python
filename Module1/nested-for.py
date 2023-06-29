# Michael L. Kelley Jr.
# June 26, 2023
# nested-for.py
# Nested for loop example using range

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
        print()
        
        