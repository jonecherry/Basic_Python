import networkx as nx
import matplotlib.pyplot as plt
def dfs(graph,node_start,max_step=10):

    assert max_step>=0 and node_start in graph.nodes()
    res_graph=nx.DiGraph()
    cur_step=0
    stack_list=[]
    visited={}
    print node_start
    visited[node_start]='1'
    stack_list.append(node_start)
    while len(stack_list)>0:
        cur_node=stack_list[-1]
        next_nodes=graph[cur_node].keys()
        if len(next_nodes)==0:#叶子节点要回退
            stack_list.pop()
            cur_step=cur_step-1
        else:
            if (len(set(next_nodes)-set(visited.keys()))==0 or cur_step>=max_step):
            #如果都被访问过 要回退
                stack_list.pop()
                cur_step=cur_step-1
            else:
                for i in next_nodes:
                    res_graph.add_edge(cur_node,i)
                    if i not in visited:
                        print i
                        visited[i]='1'
                        stack_list.append(i)
                        cur_step=cur_step+1
                        break
    return res_graph
dfs()