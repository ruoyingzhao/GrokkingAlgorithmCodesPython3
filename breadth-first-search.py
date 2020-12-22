import time
from collections import deque

#This is a kind of greedy algorithm!

print('Implementing the graph...')

graph={}
#each key is mapped to an array of all its neighbors
graph["douzi"]=["alice", "bob", "claire"]
graph["bob"]=["anuj","peggy"]
graph["alice"]=["peggy"]
graph["claire"]=["thom","jonny"]
graph["anuj"]=[]
graph["peggy"]=[]
graph["thom"]=[]
graph["jonny"]=[]

#a function that checks if someone is a mango seller
def mango_seller(name):
    sellers=["thom", "jonny"]
    return name in sellers

time.sleep(1)

#creates a new queue
search_queue=deque()
#add all my neighbors to the search queue
search_queue += graph["douzi"]

def find_mango_seller(queue):
    already_searched=[]
    #while the queue isn't empty
    while queue:
        #grabs the first person off the queue
        person = queue.popleft()
        print(person,' is off the queue now.')
        
        #check if we've already search this person
        #important! so we don't risk ending up in an infinite loop
        if not person in already_searched:
            print('Checking if ', person, ' is a mango seller.')
            time.sleep(1)
            if mango_seller(person):
                print(person, " is a mango seller!")
                print('Yay! We can stop searching now.')
                return True
            else:
                #add all their friends to the queue
                queue += graph[person]
                print(person, ' is not a mango seller.')
                print('Just added', person,'\'s friends to the queue!')
                already_searched.append(person)
            time.sleep(1)
        else:
            print('We\'ve already checked this person.')
        print('--------\n')
    #if we reach here, no one in the queue is a mango seller
    return False

print('Implementing the algorithm...')
time.sleep(1)

ans=find_mango_seller(search_queue)
print(ans)