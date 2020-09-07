from quaraDB.queries import *
from datetime import datetime

def createset(user_id):
    # temperature = get_temperature(user_id)
    # options = getoptions(voting_id)
    # result = getresult(voting_id)

    health = get_health(user_id)
    dataset = []
    for i in health:
        #d.update({gettitleoptions(i):getresultbyoption(i)})
        dataset.append({'temperature':round(i.temperature), 'date':i.date.strftime("%m/%d/%Y, %H:%M:%S")})
        #dataset.append({'temperature':gettitleoptions(i), 'count':getresultbyoption(i)})

    print()
    print(dataset)
    print()
    dataset1=[
  {'ticket_class': 1, 'survived_count': 200, 'not_survived_count': 123},
  {'ticket_class': 2, 'survived_count': 119, 'not_survived_count': 158},
  {'ticket_class': 3, 'survived_count': 181, 'not_survived_count': 528}
]
    print()
    return(dataset)
