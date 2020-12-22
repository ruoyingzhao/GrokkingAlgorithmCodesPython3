import time
#This is a kind of greedy algorithm!

#Dijkstra's algorithm only works for directed graphs with positive weights
#(cycles with positive weights are fine)

#First, we represent the graph using a dictionary
print('Implementing the graph...')
graph={}
#the entry for each node is another dictionary
#which shows its neighbors and the weight for the edge in between
graph['start']={}
graph['start']['a'] = 6
graph['start']['b'] = 2

#The neighbors of start
#print(graph['start'].keys())
#The weight of the edge between start and a, b
#print(graph['start']['a'])
#print(graph['start']['b'])

#Adding the rest of the nodes and their neighbors
#The node a only has one neighbor! because the graph is directed
graph['a']={}
graph['a']['fin'] = 1

graph['b']={}
graph['b']['a'] = 3
graph['b']['fin'] = 5

#The finish node doesn't have any neighbors
graph['fin'] ={}


time.sleep(1)
##########################
#A dictionary to store the costs for each node
#Cost: how long it takes to get to that node from the start
print('Implementing the costs dictionary...')

costs={}
costs['a'] = 6
costs['b'] = 2
#We can represent infinity in python
infinity=float('inf')
costs['fin'] = infinity

time.sleep(1)
###########################
#A dictionary for the parents of each node
print('Implementing the parents dictionary...')

parents = {}
parents['a']='start'
parents['b']='start'
parents['fin']= None

time.sleep(1)
###########################
#A list to keep track of the processed nodes
print('Implementing the processed list...')

processed = []

time.sleep(1)
###########################
#a function that finds the lowest cost node that is not procesed yet
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        if (costs[node] < lowest_cost) and (node not in processed):
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node


###########################
print('Starting the algorithm...')

node=find_lowest_cost_node(costs)
###########################
while node != None:
    cost = costs[node]
    #get the list of neighbors of node
    #(this is a dictionary storing the weights)
    neighbors = graph[node]

    #iterate through each neighbor of node
    for n in neighbors.keys(): 
        #neighbors[n] is the weight of the edge from node to n
        new_cost = cost + neighbors[n]
        #update the cost if it's lower than stored previously in the costs dictionary
        if costs[n] > new_cost:
            costs[n] = new_cost
            #update the parent of n to this node
            parents[n] = node
    #mark node as processed
    processed.append(node)

    #find the next node with the lowest cost
    node = find_lowest_cost_node(costs)


time.sleep(1)
###########################
#follow the parents list to find the shortest path
print('Processing the path...')

current_node = 'fin'
path = ['fin']
while current_node != 'start':
    path.append(parents[current_node])
    current_node = parents[current_node]


#reverses the list
path.reverse()

time.sleep(1)

print('The shortest path is:')
for node in path[:-1]:
    print(node)
    print('''
|
v
    ''')
print(path[-1])