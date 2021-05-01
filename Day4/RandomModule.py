import random
import my_module

# Random whole number
random_integer = random.randint(1,10)
print(random_integer)
print(my_module.pi)

# Random floating point number
# random() always generate number btw 0 to 1 by default
random_float = random.random()
print(random_float)

# If you want to generate the number btw 1 to 5
random_helper1 = random.randint(1,6)
random_float2 = random.random()
print(random_float2*random_helper1)

###############################
# What is Module?
###############################

