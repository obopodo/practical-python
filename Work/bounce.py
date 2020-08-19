# bounce.py
#
# Exercise 1.5

height = 100

for bounce in range(10):
    height *= 3/5
    print(bounce, round(height, 4))
