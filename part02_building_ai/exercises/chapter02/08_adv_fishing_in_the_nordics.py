#Suppose we also happen to know the gender of the lottery winner. Here are same OECD statistics as above broken down by gender:

# Write a function that uses the above numbers and tries to guess the nationality of the winner when we know that the winner is a fisher and their gender (either female or male).

#The argument of the function should be the gender of the winner ('female' or 'male'). The return value of the function should be a pair (country, probability) where country is the most likely nationality of the winner and probability is the probability of the country being the nationality of the winner.
#Output Example
#if the winner is male, my guess is he's from Finland; probability 08.56%
#if the winner is female, my guess is she's from Norway; probability 23.98%

#Tip: Your values might be different, but the formatting should be identical.

countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26] 

def guess(winner_gender):
    if winner_gender == 'female':
        fishers = female_fishers
    else:
        fishers = male_fishers

    # write your solution here

    total_fishers = sum(fishers)
    total_population = sum(populations)

    temp = (fishers[0] / total_fishers)
    for j in range(len(countries)):
        start = (fishers[j] / total_fishers)
        if start > temp:
            temp = (fishers[j] / total_fishers)
            guess = countries[j]
            biggest = fishers[j] / total_fishers * 100
    return (guess, biggest)  

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main()
