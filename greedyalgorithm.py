import time

#a list of states that we want to cover
#turn it into a set to eliminate duplications
print('Implementing the states we need to cover...')
states_needed = set(['mt','wa','or','id','nv','ut','ca','az'])
time.sleep(1)

#a dictionary of stations that we can choose from
print('Implementing the stations to choose from...')
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])
time.sleep(1)

#a dictionary to hold the final set of stations we'll use
final_stations = set()

##################################
print('Implementing the greedy algorithm...')
#as long as not all states are covered:
while states_needed:
    #first, find the best station we can choose
    #one that covers the most uncovered states
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        #find the intersection of the two sets
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    #add the best station to the final list of stations
    final_stations.add(best_station)
    #update the list of states we need to cover
    #using set difference
    states_needed -= states_covered

time.sleep(1)
#show the result
print('An approximation of the best choices is:')
print(final_stations)