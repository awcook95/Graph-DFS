def dfs(G, I, F):
    list = [] #list to track order of visited nodes

    visited = {} #map of vertex to bool set to false
    for vertex in G:
        visited[vertex] = False

    stack = [] #stack tracks order of vertices to visit
    stack.append(I) #push initial vertex

    while stack:
        current = stack.pop()
        if(visited[current]): continue #if node is already visited skip rest of loop
        visited[current] = True #set current node to visited

        adjacents = G[current]

        for vertex in adjacents:
            stack.append(vertex)





adjList = {} #dictionary to act as adjacency list

with open("connections.txt", 'r') as f:
    for line in f:
        if 'END' in line:
          break

        li = list(line.split(" ")) #convert each line of the file to a list
        adjList[li[0]] = li[2:] #map the vertex to its adjacent vertices

       
#print dictionary for testing
for key in adjList.keys():
    print(key, ':', adjList[key])


I = input("Enter the initial vertex\n")
F = input("Enter the final vertex\n")
print("The initial vertex is: " + I + " and the final vertex is: " + F)

#dfs(adjList, I, F)