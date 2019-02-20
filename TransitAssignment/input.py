"""
1. Input graph
2. I manually input the graph data
3. You can write more general input function for large network and realistic application
"""
from graph import bus_line_class,node_class,link_class,graph_class

LARGE_FRE_DELTA  = 1000.0 # a large number for the frequency on the walking link
# class bus_line_class():
#     def __init__(self,name,id,fre):
#         self.name = name
#         self.id = id
#         self.fre = fre
#         self.stops = []
#     pass
# class node_class():
#     def __init__(self, node_name, node_id):
#         self.id = node_id
#         self.name = node_name
#         self.out_links = []
#         self.in_links = []
#         self.lines = []
#     pass
# class link_class():
#     def __init__(self,link_name,link_id,cost):
#         self.id = link_id
#         self.name = link_name
#         self.tail_node = []  
#         self.head_node = []
#         self.cost = cost
#         self.lines = []
#         self.fre = -1.0
#     pass
# class graph_class():
#     def __init__(self):
#         self.links = []
#         self.nodes = []
#         self.lines = []
#     pass


def input_network():
    """
        input the netework of spiess network
    """
    # create graph
    graph = graph_class()
    # add lines 
    graph.lines.append(bus_line_class("G1",0, 1/6))
    graph.lines.append(bus_line_class("G2",1, 1/6))
    graph.lines.append(bus_line_class("G3",2, 1/15))
    graph.lines.append(bus_line_class("G4",3, 1/3))
    graph.lines.append(bus_line_class("Walk",4,LARGE_FRE_DELTA))

    # input nodes
    graph.nodes.append(node_class("A",0))
    graph.nodes.append(node_class("X2",1))  
    graph.nodes.append(node_class("Y",2))  
    graph.nodes.append(node_class("B",3))        
    graph.nodes.append(node_class("X",4))  
    graph.nodes.append(node_class("Y3",5))  
    # input node demand 
    graph.nodes[0].demand = 1

    # input links
    graph.links.append(link_class("A-B",0))
    graph.links[0].lines.append(graph.lines[0])
    graph.links[0].cost = 25
    graph.links.append(link_class("A-X2",1))
    graph.links[1].lines.append(graph.lines[1])
    graph.links[1].cost = 7
    graph.links.append(link_class("X2-Y",2))
    graph.links[2].lines.append(graph.lines[4])
    graph.links[2].cost = 6
    graph.links.append(link_class("Y-B",3))
    graph.links[3].lines.append(graph.lines[3])
    graph.links[3].cost = 10
    graph.links.append(link_class("X2-X",4))
    graph.links[4].lines.append(graph.lines[4])
    graph.links[4].cost = 0
    graph.links.append(link_class("X-X2",5))
    graph.links[5].lines.append(graph.lines[1])
    graph.links[5].cost = 0
    graph.links.append(link_class("X-Y3",6))
    graph.links[6].lines.append(graph.lines[2])
    graph.links[6].cost = 4
    graph.links.append(link_class("Y-Y3",7))
    graph.links[7].lines.append(graph.lines[2])
    graph.links[7].cost = 0
    graph.links.append(link_class("Y3-Y",8))
    graph.links[8].lines.append(graph.lines[4])
    graph.links[8].cost = 0
    graph.links.append(link_class("Y3-B",9))
    graph.links[9].lines.append(graph.lines[4])
    graph.links[9].cost = 4

    # input tail and head for links
    ## "AB"
    graph.links[0].tail_node.append(graph.nodes[0])
    graph.links[0].head_node.append(graph.nodes[3])
    ## "A-X2"
    graph.links[1].tail_node.append(graph.nodes[0])
    graph.links[1].head_node.append(graph.nodes[1])
    ## "X2-Y"
    graph.links[2].tail_node.append(graph.nodes[1])
    graph.links[2].head_node.append(graph.nodes[2])
    ## "Y-B"
    graph.links[3].tail_node.append(graph.nodes[2])
    graph.links[3].head_node.append(graph.nodes[3])
    ## "X2-X"
    graph.links[4].tail_node.append(graph.nodes[1])
    graph.links[4].head_node.append(graph.nodes[4])
    ## "X-X2"
    graph.links[5].tail_node.append(graph.nodes[4])
    graph.links[5].head_node.append(graph.nodes[1])
    ## "X-Y3"
    graph.links[6].tail_node.append(graph.nodes[4])
    graph.links[6].head_node.append(graph.nodes[5])
    ## "Y-Y3"
    graph.links[7].tail_node.append(graph.nodes[2])
    graph.links[7].head_node.append(graph.nodes[5])
    ## "Y3-Y"
    graph.links[8].tail_node.append(graph.nodes[5])
    graph.links[8].head_node.append(graph.nodes[2])
    ## "Y3-B"
    graph.links[9].tail_node.append(graph.nodes[5])
    graph.links[9].head_node.append(graph.nodes[3])


    # input outgoing/incoming links for nodes 
    ## node A
    graph.nodes[0].out_links.append(graph.links[0])
    graph.nodes[0].out_links.append(graph.links[1])
    ## node X2
    graph.nodes[1].out_links.append(graph.links[2])
    graph.nodes[1].out_links.append(graph.links[4])
    graph.nodes[1].in_links.append(graph.links[5])
    graph.nodes[1].in_links.append(graph.links[1])
    ## node Y
    graph.nodes[2].out_links.append(graph.links[3])
    graph.nodes[2].out_links.append(graph.links[7])
    graph.nodes[2].in_links.append(graph.links[8])
    graph.nodes[2].in_links.append(graph.links[2])
    ## node B
    graph.nodes[3].in_links.append(graph.links[0])
    graph.nodes[3].in_links.append(graph.links[3])
    graph.nodes[3].in_links.append(graph.links[9])
    ## node X    
    graph.nodes[4].out_links.append(graph.links[5])
    graph.nodes[4].out_links.append(graph.links[6])
    graph.nodes[4].in_links.append(graph.links[4])
    ## node Y3
    graph.nodes[5].out_links.append(graph.links[8])
    graph.nodes[5].out_links.append(graph.links[9])
    graph.nodes[5].in_links.append(graph.links[7])
    graph.nodes[5].in_links.append(graph.links[6])

    # TODO: print and check then network structure

    # ' node, outlink, link tail, head, cost, fre'

    with open ('network.csv', 'w+') as f:
        """
            output to check the network 
        """
        pass
        print("Node,OutLink,LinkTime,LinkTail,LinkHead,LinkLine,Fre", file=f)
        for node in graph.nodes:
            for link in node.out_links:
                print("{0},{1},{2},{3},{4},{5},{6}".format(node.name,link.name,link.cost,link.tail_node[0].name,link.head_node[0].name,link.lines[0].name,link.lines[0].fre),file=f)

        print("Node,InLink,LinkTime,LinkTail,LinkHead,LinkLine,Fre", file=f)
        for node in graph.nodes:
            for link in node.in_links:
                print("{0},{1},{2},{3},{4},{5},{6}".format(node.name,link.name,link.cost,link.tail_node[0].name,link.head_node[0].name,link.lines[0].name,link.lines[0].fre),file=f)
       

    return graph
