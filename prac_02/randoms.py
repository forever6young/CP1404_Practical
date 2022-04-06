import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""What did you see on line 1?
What was the smallest number you could have seen, what was the largest?"""
# All integers from five to nineteen
# smallest：5
# largest：19

"""What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?"""
# 3, 5, 7, 9
# smallest：3
# largest：9
# line 2 can not produce a 4

"""What did you see on line 3?
What was the smallest number you could have seen, what was the largest?"""
# the numbers between [2.5, 5.5)
# smallest：2.5
# largest：infinitely towards 5.5 decimals

"""Write code, not a comment, to produce a random number between 1 and 100 inclusive."""
# import random
# print(random.randint(1, 101))
