#Breadth first search (only horizontal or vertical adjacent)
#in this practice, 1s which are horizontally or vertically adjacent to each other are called "river"
#using BFS to see how many "river" in a graph and what are their position

def breadth_first_search(graph):
    result = [] #storing the position of ALL river(adjacent 1)
    copy_graph = graph
    for index1,row in enumerate(copy_graph):
        for index2,column in enumerate(row):
            if column == 0:
                copy_graph[index1][index2] = False #indicate 0 in graph(not part of a river)/it has been evaluated
            else:
                copy_graph[index1][index2] = True #indicate 1 in graph(part of a river)/it has not been evalutaed

    directions = ((-1,0),(1,0),(0,-1),(0,1)) # up down left right
    for index1,row in enumerate(copy_graph):
        for index2, col in enumerate(row):
            if col == True:
                #start BFS
                copy_graph[index1][index2] = False
                pointer = (index1,index2) #for the starting point of the BFS
                queue = [] #in form of [(row,col),(row,col),(row,col)]
                output = [] #also [(row,col),(row,col)]
                output.append(pointer)
                for direction in directions: #search for all directions to see whether it is adjacent
                    dir_row = pointer[0] + direction[0]
                    dir_col = pointer[1] + direction[1]
                    if dir_row >= 0 and dir_row < len(graph) and dir_col >= 0 and dir_col < len(graph[0]):
                        if copy_graph[dir_row][dir_col] == True:
                            queue.append((dir_row,dir_col))
                            copy_graph[dir_row][dir_col] = False
                while len(queue)>0:
                    pointer = queue[0]
                    output.append(queue[0])
                    queue.pop(0)
                    for direction in directions: #search for all directions to see whether it is adjacent
                        dir_row = pointer[0] + direction[0]
                        dir_col = pointer[1] + direction[1]
                        if dir_row >= 0 and dir_row < len(graph) and dir_col >= 0 and dir_col < len(graph[0]):
                            if copy_graph[dir_row][dir_col] == True:
                                queue.append((dir_row,dir_col))
                                copy_graph[dir_row][dir_col] = False
                result.append(output)
    return result



    
        
            
        
                



if __name__ == '__main__':
    graph = ([0,0,0,0,0], #0 for walkable 1 for unwalkable e.g. wall
            [1,0,1,1,1],
            [1,0,0,0,1],
            [1,1,0,0,1],
            [0,0,0,0,0])
    result = breadth_first_search(graph)
    print(result)
    print(f"number of rivers is {len(result)}")

    
