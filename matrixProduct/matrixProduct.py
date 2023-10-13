class Position:
  def __init__(self):
    self.column = 0
    self.row = 0

class MatrixProduct:

  def __init__(self):
    self._table_operations = []
    self._table_optimal_k = []
    self._result = ""
  
  def _walk_matrix_on_diagonal(self, matrix, method, params={}):
    total_rows = len(matrix) - 1
    total_periods = 0
    position = Position()
    while True:
      method(position.row, position.column, params)
      position.row+=1
      position.column+=1
      if( position.row > total_rows-total_periods ):
        total_periods+=1
        position.row = 0
        position.column = total_periods
      if( position.column > total_rows and position.row == 0):
        break
  
  def __calculate_product(self, start_matrix, end_matrix):
    if( start_matrix == end_matrix ): return start_matrix
    k = self._table_optimal_k[start_matrix][end_matrix]
    result_1 = self.__calculate_product(start_matrix, k)
    result_2 = self.__calculate_product(k+1, end_matrix)
    result = "({}{})".format(result_1,result_2)
    return result

  def calculate_product(self, matrices=[]):
    dimensions = [30,35,15,5,10,20,25]
    p_0 = dimensions.pop(0)
    amount_elements = len(dimensions)
    self._table_operations = self._get_table_with_zeros(amount_elements)
    self._table_optimal_k = self._get_table_with_zeros(amount_elements)
    params = {"dimensions": dimensions, "p_0":p_0 }
    self._walk_matrix_on_diagonal(self._table_operations, self.calculate_optimal_products, params )
    self.__calculate_product(0, len(dimensions)-1)
    print(self._result)
    print("================================================")
    for (i, row) in enumerate(self._table_operations):
      for (j, column) in enumerate(row):
        print(column, " ({},{})".format(i,j), end="")
      print(" ")
    print("================================================")
    for (i, row) in enumerate(self._table_optimal_k):
      for (j, column) in enumerate(row):
        print(column, " ", end="")
      print(" ")

  def calculate_optimal_products(self,i,j,params):
    dimensions = params["dimensions"]
    p_0 = params["p_0"]
    result = {"total_cost": 0, "k": i } 
    list_sub_operations = []
    if(i != j):
      for k in range(i,j):
        left_sub_operations = self._table_operations[i][k]
        right_sub_operations = self._table_operations[k+1][j]
        p_i = dimensions[i-1] if i!=0 else p_0
        p_k = dimensions[k]
        p_j = dimensions[j]
        interval_operations = p_i*p_k*p_j 
        total_cost = left_sub_operations + right_sub_operations + interval_operations
        current_sub_operation = {"total_cost": total_cost, "k": k } 
        list_sub_operations.append(current_sub_operation)
      result = sorted(list_sub_operations, key=lambda x: x["total_cost"])[0] if len(list_sub_operations) > 0 else result
    self._table_operations[i][j] = result["total_cost"]
    self._table_optimal_k[i][j] = result["k"]
      
  def _get_table_with_zeros(self, n):
    table = [[0 for _ in range(n)] for _ in range(n) ]
    return table

matrixProduct = MatrixProduct()
matrixProduct.calculate_product()