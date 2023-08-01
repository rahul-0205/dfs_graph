def dfs_graph(graph,start):
  print(start)
  if (len(graph[start]==0):
    return
  for i in graph[start]:
    dfs_graph(graph,i)
  
graph={10:[20,30,40,50],
        20:[],
        30:[],
        40:[],
        50:[100],
        60:[70],
70:[],
100:[]

}
print(dfs_graph(graph,start))
