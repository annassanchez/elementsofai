def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    # https://sea-distances.org/
    # nautical miles converted to km

    D = [
            [0,8943,8019,3652,10545],
            [8943,0,2619,6317,2078],
            [8019,2619,0,5836,4939],
            [3652,6317,5836,0,7825],
            [10545,2078,4939,7825,0]
        ]

    # https://timeforchange.org/co2-emissions-shipping-goods
    # assume 20g per km per metric ton (of pineapples)


    co2 = 0.020
    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]

                    # Modify this if statement to check if the route is valid
                    if 0 in route and 1 in route and 2 in route and 3 in route and 4 in route:
                        #route = [0, 1, 2, 3, 4]
                        distance = D[route[0]][route[1]] + D[route[1]][route[2]] + D[route[2]][route[3]] + D[route[3]][route[4]]
                        emissions = distance * co2
                        print(' '.join([portnames[i] for i in route]) + " %.1f kg" % emissions)
    
main()
