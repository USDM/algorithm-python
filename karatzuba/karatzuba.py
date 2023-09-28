
def get_halves_of_number(number):
  half_position = len(number) // 2
  half_left = number[:half_position]
  half_right = number[half_position:]
  return int(half_left), int(half_right)

def karatzuba(x, y):
  try:
    n = len(str(abs(int(x))))
    if( n == 1 ): return int(x)*int(y)
    x_1, x_2 = get_halves_of_number(x)
    y_1, y_2 = get_halves_of_number(y)
    u = karatzuba(str(x_1), str(y_1))
    v = karatzuba(str(x_2), str(y_2))
    w = karatzuba(str(x_1-x_2), str(y_1-y_2))
    z = u + v - w
    p = (10**2)*u + (10**(n/2))*z +v 
    return p
  except Exception as e:
    print(x,y, e)
    pass

number_1 = "25"
number_2 = "30"

p = karatzuba(number_1, number_2)
print(p)