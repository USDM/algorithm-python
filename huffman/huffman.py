
LEFT_SIDE = "0" 
RIGHT_SIDE = "1"

class Node:
  def __init__(self, character="", frequency="", left_child=None, right_child=None, father=None ,symbol=""):
    self.character = character
    self.frequency = frequency
    self.father = father
    self.set_right_child(right_child)
    self.set_left_child(left_child)
    self.symbol = symbol

  def set_right_child(self, right_child):
    self.right_child = right_child
    if( self.right_child is not None ): 
      self.right_child.set_father(self)
      self.right_child.set_symbol(RIGHT_SIDE)

  def set_left_child(self, left_child):
    self.left_child = left_child
    if( self.left_child is not None ): 
      self.left_child.set_father(self)
      self.left_child.set_symbol(LEFT_SIDE)

  def set_symbol(self, symbol):
    self.symbol = symbol

  def set_father(self, father):
    self.father = father

class Huffman:
  def __init__(self):
    self._text = ""
    self._characters_informations = {}
    self._root_of_combinations_tree = None

  def descompress(self, compressed_text):
    descompressed_text = ""
    node_current = self._root_of_combinations_tree
    for character_current in reversed(compressed_text):
      if( character_current == LEFT_SIDE ):
        node_current = node_current.left_child
      if( character_current== RIGHT_SIDE ):
        node_current = node_current.right_child
      is_node_current_a_leaf = node_current.left_child == None and node_current.right_child == None
      if( is_node_current_a_leaf ):
        descompressed_text = node_current.character + descompressed_text
        node_current = self._root_of_combinations_tree
    return descompressed_text

  def compress(self,text):
    self._text = text
    self._determinate_characters_information()
    self._generate_root_of_combinations_tree()
    self._determinate_characters_combinations(self._root_of_combinations_tree)
    compressed_text = self._replace_characters_by_combinations()
    return compressed_text

  def _replace_characters_by_combinations(self):
    compressed_text = ""
    for character in self._text:
      compressed_text += self._characters_informations[character]["combination"]
    return compressed_text

  def _determinate_characters_combinations(self, node, combination=""):
    if( node.left_child == None and node.right_child == None): 
      self._characters_informations[node.character]["combination"] = combination
      print(node.character, combination)      
      return 
    self._determinate_characters_combinations( node.left_child, node.left_child.symbol+combination )
    self._determinate_characters_combinations( node.right_child, node.right_child.symbol+combination )
  
  def _generate_root_of_combinations_tree(self):
    sorted_characters_frequencies = self._get_sorted_characters_frequencies()
    nodes = [ Node( character=el["character"], frequency=el["frequency"]) for el in sorted_characters_frequencies ]
    while len(nodes) > 1:
      nodes = sorted( nodes, key=lambda x: x.frequency  )
      left_child = nodes.pop(0)
      right_child = nodes.pop(0)
      sum_frequencies = left_child.frequency + right_child.frequency
      new_node = Node(frequency=sum_frequencies, left_child=left_child, right_child=right_child)
      nodes.append(new_node)
    self._root_of_combinations_tree = nodes[0]

  def _determinate_characters_information(self):
    characters_information = {}
    for character in self._text:
      if character in characters_information:
        characters_information[character]["frequency"] += 1
      else:
        characters_information[character] = {
          "frequency":1,
          "combination" :""
        }
    self._characters_informations = characters_information

  def _get_sorted_characters_frequencies(self):
    sorted_characters_frequencies = [ {"character":key, "frequency": el["frequency"]} for key, el in self._characters_informations.items() ]
    sorted_characters_frequencies = sorted(sorted_characters_frequencies, key=lambda x: x['frequency'], reverse=True)
    return sorted_characters_frequencies

text = "AQUI PUEDE HABER MAS TEXTO Y ENTONCES LA APP VA A COMPRIMIR EL TEXTO EN ALGO MAS\nlalala"

huffman = Huffman()

compress_text=  huffman.compress(text)

print(compress_text)

descompress_text = huffman.descompress(compress_text)

print(descompress_text)