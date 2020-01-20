def dfs(G, I, F):
    pathMap = {} #map to track order of visited nodes

    visited = {} #map of vertex to bool set to false
    for vertex in G:
        visited[vertex] = False

    stack = [] #stack tracks traversal order of vertices for the dfs
    stack.append(I) #push initial vertex

    print("vertices are being visited in this order")

    while stack:
        current = stack.pop()
        print(current)
        if current == F: return pathMap #once final vertex  is found return the path

        if(visited[current]): continue #if node is already visited skip rest of loop
        visited[current] = True #set current node to visited

        for neighbor in G[current]: #for all vertices adjacent to current vertex
            if not visited[neighbor] : 
                stack.append(neighbor)
                pathMap[neighbor] = current #update the current path from the starting point

    return False #final vertex was not found



adjList = {} #dictionary to act as adjacency list

with open("connections.txt", 'r') as f:
    for line in f:
        if 'END' in line:
          break

        line = line.strip('\n') #remove newline
        li = list(line.split(" ")) #convert each line of the file to a list
        adjList[li[0]] = sorted(li[2:], reverse = True) #map the vertex to its adjacent vertices

       
#print dictionary for testing
for key in adjList:
    print(key, ':', adjList[key])


#I = input("Enter the initial vertex\n")
#F = input("Enter the final vertex\n")
I = "A1"
F = "G1"

print("The initial vertex is: " + I + " and the final vertex is: " + F)

pathMap = dfs(adjList, I, F)

print("The path map: ")
for vertex in pathMap:
    print(vertex, ':', pathMap[vertex])


if pathMap != False: #if dfs succeeded
    curr = F #start at the target node
    output = [] #the path will be backwards so store in a list first
    while (curr != I):
        output.append(curr)
        curr = pathMap[curr] #and use the path map to trace back the steps taken
    output.append(I) #add the starting point separately
else: exit("A path to the final vertex was not found")

print("The path from", I, "to", F, "is:")
for vertex in reversed(output):
    print(vertex)





