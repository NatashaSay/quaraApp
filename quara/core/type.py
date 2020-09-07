from datetime import datetime

def createparameter(initial, distanse, quantity, time, type):

    initial_par = initial
    distanse_par = distanse / 100 * 2
    quantity_par = quantity / 2.5
    time_par = str(time)

    types = [
        {'shop': 0.1 },
        {'cinema': 0.15 },
        {'pool': 0.3},
        {'university': 0.2},
        {'school': 0.25}
    ]

    parameter = initial_par + (distanse_par*types[0]['shop']*quantity_par)

    if parameter>100:
        return '100'


    return str(parameter)


print(createparameter(3.2,200,20,1,0))
