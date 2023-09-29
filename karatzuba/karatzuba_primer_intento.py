def karatzuba(x, y, show=False):
  import math
  try:
    x,y = cast_numbers_to_pair_digits(x,y)
    n = get_number_digits(x)
    if( n == 1 ): return int(x)*int(y)
    x_1, x_2 = get_halves_of_number(x)
    y_1, y_2 = get_halves_of_number(y)
    d_x = int(x_1)-int(x_2)
    d_y = int(y_1)-int(y_2)
    u = karatzuba(x_1, y_1)
    v = karatzuba(x_2, y_2)
    w = karatzuba(str(d_x), str(d_y))
    z = u + v - w 
    n_over_two = math.ceil(n/2)
    p = (10**n)*u + (10**n_over_two)*z +v
    if( show ):
      pass
      print(x_1, x_2, "<====>", y_1, y_2)
      print("@PARAMETERS", u, v, w, z, n_over_two, n) 
      print("@SEGUNDA", (10**n)*u, (10**n_over_two)*z, v, (10**n)*u + (10**n_over_two)*z +v )
    return p
  except Exception as e:
    print(x,y, e)
    pass

def cast_numbers_to_pair_digits(x,y):
  orgi_x = x
  orig_y = y
  x, sign_x = getAndRemoveSign(x)
  y, sign_y = getAndRemoveSign(y)
  x_n = get_number_digits(x)
  y_n = get_number_digits(y)
  if( x_n == 1 and y_n == 1 ): return x,y
  if( x_n%2 == 0 and y_n%2 == 0 ): return x,y
  max_n = max([x_n%2,y_n%2])
  if( x_n != 1 ): x = add_left_zeros(x, max_n)
  if( y_n != 1 ): y = add_left_zeros(y, max_n)
  print("YO NO SE", x ," ",y, sign_x, sign_y, orgi_x, orig_y)
  return sign_x+x,sign_y+y

def add_left_zeros(value, number_zeros):
  for i in range(0,number_zeros):
    value = "0" + value
  return value

def get_halves_of_number(number):
  number,sign = getAndRemoveSign(number)
  half_position = len(number) // 2
  half_left = number[:half_position]
  half_right = number[half_position:]
  print(number, half_left, half_right)
  return sign+half_left, sign+half_right

def getAndRemoveSign(number):
  sign = number[0] if number[0] == "-" else "" 
  if( sign == "-" ):
    number = number[1:]
  return number, sign


def get_number_digits(number):
  return sum( 1 for el in number if el.isdigit() )

number_1 = "34342353253463463453523432242353463453"
number_2 = "34342353253463463453523432242353463453"

p = karatzuba(number_1, number_2, show=True)
print(p)