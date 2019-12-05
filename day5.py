import math

def file_reader(filename):
  with open(filename) as f:
    return list(map(int, f.readline().split(',')))


def solve(intcode, verb):
  program_output = None

  # initialize cur to start
  cur = 0

  while True:
    op = intcode[cur]
    mode1 = digit(op, 2)
    mode2 = digit(op, 3)
    mode3 = digit(op, 4)

    op = op % 100

    if op == 99:
      break

    # Addition
    if op == 1:
      val1 = get(intcode, cur, 1, mode1)
      val2 = get(intcode, cur, 2, mode2)
      put(intcode, cur, 3, val1 + val2)
      cur +=4

    # Multiply
    elif op == 2:
      val1 = get(intcode, cur, 1, mode1)
      val2 = get(intcode, cur, 2, mode2)
      put(intcode, cur, 3, val1 * val2)
      cur +=  4

    # Take input
    elif op == 3:
      put(intcode, cur, 1, verb)
      cur += 2

    # Output
    elif op == 4:
      program_output = get(intcode, cur, 1, False)
      cur += 2

    # Jump-if-true: If the first param is non-zero, set instruction cur
    # to the value of the second param, else do nothing
    elif op == 5: 
      val1 = get(intcode, cur, 1, mode1)
      val2 = get(intcode, cur, 2, mode2)
      if val1 != 0:
        cur = val2
      else:
        cur +=3
    
    # jump-if-false
    elif op == 6:
      val1 = get(intcode, cur, 1, mode1)
      val2 = get(intcode, cur, 2, mode2)
      if val1 == 0:
        cur = val2
      else:
        cur +=3

    # Check less than
    elif op == 7:  # less than
      val1 = get(intcode, cur, 1, mode1)
      val2 = get(intcode, cur, 2, mode2)
      put(intcode, cur, 3, 1 if val1 < val2 else 0)
      cur += 4
    
    # Check equality
    elif op == 8:
      val1 = get(intcode, cur, 1, mode1)
      val2 = get(intcode, cur, 2, mode2)
      put(intcode, cur, 3, 1 if val1 == val2 else 0)
      cur += 4
    else:
      raise Exception(f'ERROR: the value at {cur} is {op}, it should be 0!!!')
  return program_output

# get the values of the parameter, shifting from the pointer
# that points to the opcode. Also takes in a flag for immediate mode
def get(intcode, cur, param, imode):
  pos = cur + param
  if imode:
    return intcode[pos]
  else:
    return intcode[intcode[pos]]

# Write the values to the tape
def put(intcode, cur, param, value):
  pos = cur + param
  intcode[intcode[pos]] = value

# 
def digit(number, n):
  return number // 10**n % 10


intcode1 = file_reader('day5.in')
intcode2 = file_reader('day5.in')

print("Part 1: " + str(solve(intcode1, 1)))
print("Part 2: " + str(solve(intcode2, 5)))