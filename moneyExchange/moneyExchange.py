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
    self._min_set_exchange = []
  
  def get_min_exchange(self):
    self._total_exchange = 9
    self._initialize_items()
    self._initialize_table()
    self._walk_horizontably_on_table(self.method)
    self._determinate_min_set_exchange()
    self._print_table(self._table)
    print(self._min_set_exchange)

  def _determinate_min_set_exchange(self):
    min_set_exchange = []
    row_current = len(self._table) - 1
    column_current = len(self._table[row_current]) - 1
    while True:
      item_current = self._items[row_current]
      cell_current = self._table[row_current][column_current]
      top_cell_current = self._table[row_current-1][column_current]
      if( cell_current.times != top_cell_current.times ):
        times_item = int( column_current/item_current.value ) if column_current != 0 else 0
        for _ in range(0,times_item): min_set_exchange.append(item_current.value)
        column_current = column_current - times_item*item_current.value
        row_current = row_current - 1
      else:
        row_current = row_current - 1
      if row_current <= 0:
        break
    self._min_set_exchange = min_set_exchange
  def _walk_horizontably_on_table(self, method, params={}):
    total_rows = len(self._table)
    for row in range(0, total_rows ):
      total_columns = len(self._table[row])
      for column in range(0, total_columns):
        method( row, column, params )

  def method(self, row, column, params):
    if( row == 0 or column == 0 ): return
    item_current = self._items[row]
    cell_current = self._table[row][column]
    options = []
    option_1 = self.get_option_1(row, column)
    option_2 = self.get_option_2(row, column, item_current)
    if option_1 != 0: options.append(option_1)
    if option_2 != 0: options.append(option_2)
    min_exchange = min(options)
    cell_current.times = min_exchange

  def get_option_1(self, row, column):
    return self._table[row-1][column].times
  
  def get_option_2(self, row, column, item_current):
    times = int( column / item_current.value ) if item_current.value != 0 else 0
    if times == 0: return 0
    column_jump = column - times * item_current.value
    return times + self._table[row-1][column_jump].times

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
        print(column.times, " ", end="")
      print(" ")


moneyExchange = MoneyExchange()
moneyExchange.get_min_exchange()