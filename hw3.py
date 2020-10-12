from collections import defaultdict  

vert , edges = list(map(int,input().split(' '))) #handle the input...n = vertices, m = edges

graph = defaultdict(list)#store graph in dict (defaultdict for handling "type" error)

for i in range(edges):
    a , b = list(map(int,input().split(' ')))#(map to handle "type" error)
    graph[a].append(b)

    
def dfs(graph,node,visited,visited_list):

    visited[node]=1     #set 1 to mark its visited
    
    for i in graph[node]:
        if visited[i]==0:  #if not visited, run dfs on neighbors
            dfs(graph,i,visited,visited_list)

    visited_list.append(node)#add node to the visited list

def dfs2(graph,node,visited,visited_list):  #run in reverse now on new graph

    visited[node]=1 #first node visted
    visited_list=[]
    for neighbor in graph[node]: #check remaining nodes
        if visited[neighbor] == 0:
            dfs2(graph,neighbor,visited,visited_list)
    visited_list.append(node)
            
def Transposed(graph,node):
 
    transpose_graph = defaultdict(list) #new transpose graph
  

    for x in range(1,node+1): 
        for y in graph[x]:
         transpose_graph[y].append(x)    #check all edges and reverse

    return transpose_graph

def SCC(graph,node):  #strongly connected components in directed graph

    visited_list = []

    visited=[0]*(node+1) #mark all as not visited

    for nodes in range(1,node+1): #run dfs on all unvisted nodes
        if visited[nodes]==0:
            dfs(graph,nodes,visited,visited_list)

    graph_reverse = Transposed(graph,node) #reverse the graph
  

    visited=[0]*(node+1)#mark all as not visited

    SCCcounter = 0

    while len(visited_list)!=0: #go through list again and revisit

        last = visited_list.pop()#check if last was visited

        if visited[last] == 0:
            SCCcounter += 1
            dfs2(graph_reverse,last,visited,visited_list)

    return SCCcounter #return SCC count





print(SCC(graph,vert))#print SCC in graph
