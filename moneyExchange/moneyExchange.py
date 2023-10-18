class Cell:
  
  def __init__(self, times):
    self.times = times

class Item:
  
  def __init__(self,value):
    self.value = value


class MoneyExchange:

  def __init__(self):
    self._table = []
    self._items = []
    self._total_exchange = 0
  
  def get_min_exchange(self):
    self._total_exchange = 9
    self._initialize_items()
    self._initialize_table()
    self._walk_horizontably_on_table(self.method)
    self._print_table(self._table)

  def _walk_horizontably_on_table(self, method, params={}):
    total_rows = len(self._table)
    for row in range(0, total_rows ):
      total_columns = len(self._table[row])
      for column in range(0, total_columns):
        method( row, column, params )

  def method(self, row, column, params):
    item_current = self._items[row]
    cell_current = self._table[row][column]
    while True:
      
    cell_current.value = 2

  def _initialize_items(self):
    self._items = [ Item(0), Item(1), Item(4), Item(6) ]
  
  def _initialize_table(self):
    total_rows = len(self._items)
    total_columns = self._total_exchange + 1
    self._table = self._get_table_with_zeros(total_rows, total_columns)

  def _get_table_with_zeros(self, rows, columns):
    table = [[Cell(0) for _ in range(columns)] for _ in range(rows) ]
    return table
  
  def _print_table(self, table):
    print("================================================")
    for (i, row) in enumerate(table):
      for (j, column) in enumerate(row):
        print(column.value, " ", end="")
      print(" ")


moneyExchange = MoneyExchange()
moneyExchange.get_min_exchange()