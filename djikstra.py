#!/usr/local/bin/python

#Djikstra's Algorithm

#Problem: Given a graph, a source vertex and a destination vertex, 
#          find the shortest distance between the source vertex and destination
#          vertex

#Assumptions: 
#       Bi-directional graph, i.e. if vertex A is connected to vertex B,
#       vertex B is also connected to vertex A.

#Algorithm:
#1. Create a Shortest Path Tree (SPT) which is basically an array of 
#   "shortest distances"
#   from the source to other points in the graph. Initially set a distance of 
#   0 for the source node and Infinite for all others
#
#2. Taking the closest node (from the source), add it to the visited list
#   Then 
#   

import sys;

class Edge:
    '''
    An edge in a graph. An edge has an origin, an end and 
    is of a particular length.
    Ex. (2,4,6) - where 2 is the origin vertex, 4 is the end vertex 
    and 6 is the length of the edge
    '''
    def __init__(self, originVertex, endVertex, length):
        self.m_oVertex = originVertex;
        self.m_eVertex = endVertex;
        self.m_length = length;


class Graph:
    '''
    Graph which has a node map and the number of vertices in the
    graph.

    The node map is a mapping from a vertex to an array which
    consists of all the edges it is a part of.
    Ex. in a graph with edges (0,1,4), (0,2,5), (1,3,2), the node
    map will look something like:
    {
       0  -> [ (0,1,4), (0,2,5) ]
       1  -> [ (1,0,4), (1,3,2) ]
       2  -> [ (2,0,5) ]
       3  -> [ (3,1,2) ]
    }
    '''
    def __init__(self):
        self.m_numVertices = 0;
        self.m_nodeMap = {};

    def addEdge(self,origin,end,length):
        edge = Edge(origin, end, length);

        if origin in self.m_nodeMap:
            self.m_nodeMap[origin].append(edge);
        else:
            self.m_nodeMap[origin] = [edge];

        if end in self.m_nodeMap:
            self.m_nodeMap[end].append(edge);
        else:
            self.m_nodeMap[end] = [edge];

    def printGraph(self):
        for node, edgeList in self.m_nodeMap.iteritems():
            for edge in edgeList:
                print "{}  {}  {}".format(edge.m_oVertex, edge.m_eVertex, edge.m_length);

def getClosestNode(sptArray, visited):
    least = float('inf');
    x = 0;
    size = len(sptArray);
    for index in range(0, size):
        dist = sptArray[index];
        if ( (dist < least) and (index not in visited) ):
            least = dist;
            x = index;
    return x;

def runDjikstraSPAlgo(graph, source, dest, visited, sptArray):
    '''
    Djikstra's Algorithm: 
    1. find least dist in spt array
    2. add it to visited?
    3. update its neighbours
    Repeat 1,2 and 3. Stop when you hit the destination
    '''
    closestNode = getClosestNode(sptArray, visited);
    visited.add(closestNode);
    distanceFromSource = sptArray[closestNode];
    if ( closestNode == dest ) :
        print 'Shortest Dist from source: {}'.format(sptArray[closestNode]);
        return;

    for edge in graph.m_nodeMap[closestNode]:
        dS = distanceFromSource + edge.m_length;
        if dS < sptArray[edge.m_eVertex]:
            sptArray[edge.m_eVertex] = dS;
        
    runDjikstraSPAlgo(graph,source,dest,visited,sptArray);


def findLeastDistance(graph, source, destination):
    '''
    Given a graph, a source vertex and a destination vertex,
    find the shortest distance between the source and 
    destination
    '''
    # Shortest path Tree, which is basically a table
    # that stores the distance of each vertex from
    # the source.
    # Ex. If there are 3 vertices numbered 0,1 and 2,
    # with the source being vertex 1 being the source,
    # sptArray will be initialized to ['inf',0,'inf']
    sptArray = [];
    for x in range(0, graph.m_numVertices):
        sptArray.append(float('inf'));
    sptArray[source] = 0;

    # Set of visited vertices
    visited = set();

    runDjikstraSPAlgo(graph, source, destination, visited, sptArray);


def readInput(graph):
    args = sys.argv;
    if len(args) < 2:
        print "Error";
        return;
    f = open(sys.argv[1], 'r');
    firstLine = True;
    for line in f:
        tupl = line.split();
        # print tupl;
        if firstLine == True:
            firstLine = False;
            graph.m_numVertices = int(tupl[0]);
        else:
            graph.addEdge(int(tupl[0]),int(tupl[1]),float(tupl[2]));


if __name__ == '__main__':
    graph = Graph();
    readInput(graph);
    findLeastDistance(graph,2,5);
