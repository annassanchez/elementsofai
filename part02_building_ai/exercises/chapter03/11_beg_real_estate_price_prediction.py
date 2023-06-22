# input values for one mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbours

x = [66, 5, 15, 2, 500]
c = [3000, 200 , -50, 5000, 100]     # coefficient values

prediction = c[0]*x[0] + c[1]*x[1] + c[2]*x[2] + c[3]*x[3] + c[4]*x[4]

def prediction(lista, coefficients = c):
    pred = lista[0]*coefficients[0] + lista[1]*coefficients[1] + lista[2]*coefficients[2] + lista[3]*coefficients[3] + lista[4]*coefficients[4]
    return pred

print(
    """
    What would the predicted price of a cabin be with the following details? Size: 85 m2, size of the sauna: 10m2, distance to a lake: 15m, number of indoor toilets: 1, distance to next door neighbor: 100m
    """,
    prediction([85, 10, 15, 1, 100])
)

print(
    """
    What would the predicted price of a cabin be with the following details? Size: 155m2, size of the sauna: 15m2, distance to a lake: 5m, number of indoor toilets: 1, distance to next door neighbor: 200m.
    """,
    prediction([155, 15, 5, 1, 200])
)

print(
    """
    Which increases the price of a cabin more? 
    + toilet + 10m the lake
    """,
    prediction([155, 15, 5, 2, 200]),prediction([155, 15, 15, 1, 200]),
)

print(
    """
    Which increases the price of a cabin more? 
    + 10 sqm + 100m distance from the neigbour
    """,
    prediction([165, 15, 5, 2, 300]),prediction([155, 15, 5, 2, 200]),
)