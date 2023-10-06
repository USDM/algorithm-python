class HeapSort:
  
  def sort(self, array):
    print(array)
    n = len(array)
    for i in range(n //2 -1 , -1, -1):
      self.heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        self.heapify(array, i, 0)
    print(array)

  def heapify(self, array, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if( self.evaluate_side(array, left, largest, n) ):
      largest = left
    if( self.evaluate_side(array, right, largest, n) ):
      largest = right
    is_not_i_largest = largest!= i
    if(is_not_i_largest):
      array[i], array[largest] = array[largest], array[i]
      self.heapify(array, n, largest)
    pass

  def evaluate_side(self, array, side, largest, n):
    is_side_on_array = side < n 
    if( not is_side_on_array ): return False
    is_side_more_than_largest = array[side] > array[largest]
    return is_side_on_array and is_side_more_than_largest    
  
  



array = [1,4,5,7,5,10]
heapSort = HeapSort()
heapSort.sort(array)