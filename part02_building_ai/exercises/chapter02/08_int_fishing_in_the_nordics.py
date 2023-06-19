# Write a program that uses statistics about the population and fishing industry employment to print out conditional probabilities of each nationality given that the winner works in the fishing industry.

#The data is given in lists containing the population and the number of fishers in each country.
#Output Example

#Denmark 14.32%

#Sweden 08.45%

#Tip: Your values might be different, but the formatting should be identical. 

def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)

    cond_pop = []
    for j in range(len(countries)):
        cond_pop.append(fishers[j] / total_fishers * 100)

    for country, prob in zip(countries, cond_pop):
        #prob = (fisher / total_fishers) / (popu / total_population) #* 100
        print(f"{country} {prob:.2f}%")  # Modified print statement to format correctly

main()

