import random
from karatzuba import karatzuba
import time

def multiplication_normal(number_1, number_2):
  return int(number_1) * int(number_2)

def test_function(function,number_1,number_2):
  start = time.time()
  result = function(number_1,number_2)
  end = time.time()
  print(start,end,end-start)
  return result

number_1 = "34342353253463463453523432242353463453343423532534634634535234322423534634533434235325346346345352343224235346345334342353253463463453523432242353463453"
number_2 = "34342353253463463453523432242353463453343423532534634634535234322423534634533434235325346346345352343224235346345334342353253463463453523432242353463453"

result_multi = test_function(multiplication_normal,number_1, number_2)
result_karatuzba = test_function(karatzuba,number_1, number_2)

if( not result_karatuzba == result_multi ):
  print("number 1 {} number 2 {} are equal {}".format(number_1, number_2, result_karatuzba == result_multi))

"""count = 0

ok = True
while ok:
  number_1 =  random.randint(1, 1000000)
  number_2 = random.randint(1, 100)
  result_multi = test_function(multiplication_normal,number_1, number_2)
  result_karatuzba = test_function(karatzuba,number_1, number_2)
  if( not result_karatuzba == result_multi ):
    print("number 1 {} number 2 {} are equal {}".format(number_1, number_2, result_karatuzba == result_multi))
    ok = False
  count += 1
  if( count == 100 ):
    print("SE PROCESARON {}", count)
    count = 0
  time.sleep(.3)

if ok: print("TODO BIEN")"""
