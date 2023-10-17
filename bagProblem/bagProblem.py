class Item:
  def __init__(self, weight, profit, id):
    self.weight = weight
    self.profit = profit
    self.id = id

class BagProblem:

  def __init__(self):
    self._table = []
  
  def calculate_max_profit(self):
    items = [Item(0,0,0),Item(1,10,1),Item(2,15,2),Item(3,40,3)]
    total_items = len(items)
    bag_weight = 4
    self._table = self._get_table_with_zeros(total_items, bag_weight+1)
    params = {
      "bag_weight": bag_weight,
      "items": items
    }
    self._walk_horizontably_on_table(self.method, params)
    max_sub_set = self._determinate_max_sub_set(items)
    self._print_table(self._table)
    print(max_sub_set)
    pass

  def _determinate_max_sub_set(self, items):
    max_sub_set = []
    row_current = len(self._table) - 1
    column_current = len( self._table[row_current] ) - 1
    while True:
      item_current = items[row_current]
      current_profit = self._table[row_current][column_current]
      left_profit = self._table[row_current][column_current-1]
      top_profit = self._table[row_current-1][column_current]
      if current_profit != left_profit:
        column_current = column_current - item_current.weight
        row_current = row_current - 1
        max_sub_set.append(item_current.id)
      elif current_profit != top_profit:
        row_current = row_current - 1
      if column_current <= 0:
        column_current = len( self._table[row_current] ) - 1
      if row_current <= 0:
        break
    return max_sub_set

  def method(self, row, column, params):
    bag_weight = params["bag_weight"]
    items = params["items"]
    current_item = items[row]
    option_1 = self.get_option_1(row, column)
    option_2 = self.get_option_2(row, column, current_item)
    max_profit = max([option_1, option_2])
    self._table[row][column] = max_profit

  def get_option_1(self, row, column):
    return self._table[row-1][column]
  
  def get_option_2(self, row, column, current_item):
    option_2 = 0
    does_index_exist = column-current_item.weight
    if( does_index_exist >= 0 ):
      option_2 = current_item.profit + self._table[row-1][column-current_item.weight]
    return option_2

  def _walk_horizontably_on_table(self, method, params):
    total_rows = len(self._table)
    for row in range(0, total_rows ):
      total_columns = len(self._table[row])
      for column in range(0, total_columns):
        method( row, column, params )

  def _get_table_with_zeros(self, rows, columns):
    table = [[0 for _ in range(columns)] for _ in range(rows) ]
    return table
  
  def _print_table(self, table):
    print("================================================")
    for (i, row) in enumerate(table):
      for (j, column) in enumerate(row):
        print(column, " ", end="")
      print(" ")


bagProblem = BagProblem()
bagProblem.calculate_max_profit()
