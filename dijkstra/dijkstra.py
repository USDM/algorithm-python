
BIGGEST_NUMBER = 9999999999999

class Way:

  def __init__(self, path=[], weight=BIGGEST_NUMBER):
    self.path = path
    self.weight = weight

  def add_node_to_path(self, node):
    self.path.append(node)

  def set_weight(self, weight):
    self.weight = weight

class Connection:

  def __init__(self, end_node, weight=0, start_node=None):
    self.start_node = start_node
    self.end_node = end_node
    self.weight = weight

  def set_start_node(self, start_node):
    self.start_node = start_node

class Node:

  def __init__(self, id="" , connections=[], isInitial=False, isFinal=False, shortest_way= Way() ):
    self.id = id
    self.connections = connections
    self.isInitial = isInitial
    self.isFinal = isFinal
    self.list_shortest_way = [shortest_way]

  def add_shortest_way(self, way):
    self.list_shortest_way.append(way)

  def get_minimum_weight_way(self):
    current_shorest_way = self.get_minimum_shortest_way()
    return current_shorest_way.weight
  
  def get_minimum_path_way(self):
    current_shorest_way = self.get_minimum_shortest_way()
    return current_shorest_way.path
  
  def get_minimum_shortest_way(self):
    length = len(self.list_shortest_way)
    return self.list_shortest_way[length-1]

  def initialize_connections(self, connections):
    for connection in connections: connection.set_start_node(self)
    self.set_connections(connections)

  def set_connections(self, connections):
    self.connections = connections

class Graph:

  def __init__(self, nodes):
    self.nodes = nodes

  def get_initial_node(self):
    for node in self.nodes:
      if(node.isInitial): return node
    return False
  

class Dijkstra:

  def __init__(self):
    self._graph = []
    self._connection = {}
    self._analyzed_nodes = []

  def determine_shortest_way(self, list_nodes):
    self._graph = Graph(list_nodes)
    node_current = self._graph.get_initial_node()
    while(True):
      self._calculate_minimum_ways_around_node(node_current)
      if( node_current.isFinal ): break
      new_node_current, does_exist_new = self._get_node_with_shortest_way()
      if( does_exist_new ): node_current = new_node_current
      if( node_current not in self._analyzed_nodes): self._analyzed_nodes.append(node_current)
    path = [el.id for el in node_current.get_minimum_path_way()]
    weight = node_current.get_minimum_weight_way()
    return path, weight

  def _get_node_with_shortest_way(self):
    all_nodes_not_analyzed = [ node for node in self._graph.nodes if node not in self._analyzed_nodes  ]
    if( len(all_nodes_not_analyzed) == 0 ): return None,False
    node_with_shortest_way = all_nodes_not_analyzed[0]
    for node in all_nodes_not_analyzed:
      possible_minimun_weight = node.get_minimum_weight_way()
      current_minimun_weight = node_with_shortest_way.get_minimum_weight_way()
      is_there_smaller_one = possible_minimun_weight < current_minimun_weight
      if is_there_smaller_one: node_with_shortest_way = node
    return node_with_shortest_way,True

  def _calculate_minimum_ways_around_node(self, node):
    for connection in node.connections:
      self._connection = connection
      first_option_way_weight = self._get_first_option_way_weight()
      second_option_way_weight = self._get_second_option_way_weight()
      does_exist_new_minimum_way = second_option_way_weight <= first_option_way_weight
      if(does_exist_new_minimum_way): self._create_new_minimum_way(second_option_way_weight)

  def _get_first_option_way_weight(self):
    return self._connection.end_node.get_minimum_weight_way()
  
  def _get_second_option_way_weight(self):
    return self._connection.start_node.get_minimum_weight_way() + self._connection.weight

  def _create_new_minimum_way(self, new_weight):
    minimum_shortest_way = self._connection.start_node.get_minimum_shortest_way()
    new_minimum_way = Way(path=minimum_shortest_way.path[:], weight=new_weight)
    if( self._connection.start_node not in new_minimum_way.path ):
      new_minimum_way.add_node_to_path(self._connection.start_node)
    self._connection.end_node.add_shortest_way(new_minimum_way)


_nodes_weight_table = [
  # 1  2  3  4  5  6 
  [ 0, 4, 7, "", "", 3 ], #1 
  [-4, 0, 3, "", 1, "" ], #2 
  [-7,-3, 0, 1, 1, "" ], #3 
  ["","",-1, 0,-4, "" ], #4 
  ["",-1,-1, 4, 0,-3 ], #5 
  [-3, "", "", "", 3, 0 ], #6 
]


node_1 = Node(id="1", isInitial=True, shortest_way=Way(weight=0))
node_2 = Node(id="2", shortest_way=Way(path=[]))
node_3 = Node(id="3", shortest_way=Way(path=[]))
node_4 = Node(id="4", isFinal=True, shortest_way=Way(path=[]))
node_5 = Node(id="5", shortest_way=Way(path=[]))
node_6 = Node(id="6", shortest_way=Way(path=[]))

node_1.initialize_connections( [ Connection(node_2,4), Connection(node_3,7) , Connection(node_6,3) ] )
node_2.initialize_connections( [ Connection(node_5,1), Connection(node_3,3) ] )
node_3.initialize_connections( [ Connection(node_4,1), Connection(node_5,1) ] )
node_4.initialize_connections( [ Connection(node_4,0)])
node_5.initialize_connections( [ Connection(node_4,4) ] )
node_6.initialize_connections( [ Connection(node_5,3) ] )

nodes = [
  node_1,
  node_2,
  node_3,
  node_4,
  node_5,
  node_6,
]

dijkstra = Dijkstra()
path, weight = dijkstra.determine_shortest_way(nodes)
print(path, weight)