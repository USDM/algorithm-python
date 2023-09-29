def karatzuba(x, y, finish=0):
  #print(finish)
  if( finish == 7 ):
    print(x,y)
    #pass
    #return int(x)*int(y)
  import math
  try:
    x, sign_x = getAndRemoveSign(x)
    y, sign_y = getAndRemoveSign(y) 
    x,y = cast_numbers_to_pair_digits(x,y)
    n = get_number_digits(x)
    if( n == 1 ): return int(x)*int(y)
    x_1, x_2 = get_halves_of_number(x)
    y_1, y_2 = get_halves_of_number(y)
    d_x = int(x_1)-int(x_2)
    d_y = int(y_1)-int(y_2)
    u = karatzuba(x_1, y_1, finish+1)
    v = karatzuba(x_2, y_2, finish+1)
    w = karatzuba(str(d_x), str(d_y), finish+1)
    z = u + v - w 
    n_over_two = math.ceil(n/2)
    p = (10**n)*u + (10**n_over_two)*z +v
    return p
  except Exception as e:
    print(x,y, e)
    pass

def cast_numbers_to_pair_digits(x,y):
  x_n = get_number_digits(x)
  y_n = get_number_digits(y)
  if( x_n == 1 and y_n == 1 ): return x,y
  missing_zeros_n = max([x_n%2,y_n%2])
  m_n = max([x_n,y_n]) 
  x = add_left_zeros(x, missing_zeros_n+(m_n-x_n))
  y = add_left_zeros(y, missing_zeros_n+(m_n-y_n))
  return x,y

def add_left_zeros(value, number_zeros):
  for i in range(0,number_zeros):
    value = "0" + value
  return value

def get_halves_of_number(number):
  half_position = len(number) // 2
  half_left = number[:half_position]
  half_right = number[half_position:]
  return half_left, half_right

def getAndRemoveSign(number):
  sign = number[0] if number[0] == "-" else "+" 
  if( sign == "-" ):
    number = number[1:]
  return number, sign


def get_number_digits(number):
  return sum( 1 for el in number if el.isdigit() )
