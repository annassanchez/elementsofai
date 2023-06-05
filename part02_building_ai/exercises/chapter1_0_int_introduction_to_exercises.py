# you can define your own functions
def greet(name):
    print("Welcome " + name + "!")

# go ahead and enter your own name in variable 'name' below to get a warm welcome from us.

def main():
    name = "Emma"
    greet(name)

main()

import numpy as np
import matplotlib.pyplot as plt
# generate a 30-by-50 array of random numbers
x = np.random.rand(30, 50)
# the following code that will plot the numbers as colors would normally
# be hidden from you, so again, you won't have to worry about it.
# try clicking the 'Plot' button to see the outcome.
plt.figure(figsize=(3,5))
plt.axis('off')
plt.imshow(x, cmap='Set3')

# you can define your own functions
def greet(name):
    print("Welcome " + name + "!")

# go ahead and enter your own name in variable 'name' below to get a warm welcome from us.
# to pass the test, you should change the name to "to Building AI" (note the word 'to')
def main():
    name = "to Building AI"
    greet(name)

main()