print(
    """
     Let the elevation at each point on the mountain be stored in array h of size 100. The elevation at the leftmost point is thus stored in h[0] and the elevation at the rightmost point is stored in h[99].

    Here's an example chart. The green box represents Venla's starting position, and the red triangle marks the point where Venla stops. A blue triangle (not shown here) marks the summit. 
    """
)

print(
    """
     The following program starts at a random position and keeps going to the right until Venla can no longer go up. However, perhaps the mountain is a bit rugged which means it's necessary to look a bit further ahead.

    Edit the program so that Venla doesn't stop climbing as long as she can go up by moving up to five steps either left or right. If there are multiple choices within five steps that go up, any one of them is good. To check how your climbing algorithm works in action, you can plot the results of your hill climbing using the Plot button. As a reminder, the summit will be marked with a blue triangle. 
    """
)

import math
import random             	# just for generating random mountains                                 	 

# generate random mountains                                                                               	 

w = [.05, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]

def climb(x, h):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:
        summit = True         # stop unless there's a way up
        if h[x + 1] > h[x]:
            x = x + 1         # right is higher, go there
            summit = False    # and keep going
    return x


def main(h):
    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    return x0, x

main(h)
