def jumpGame(a, i):
  if i > len(a) - 1:
    return False
  if i == len(a) - 1:
    return True
  reached = False
  for j in range(1, a[i] + 1):
    if i + j < len(a):
      reached = jumpGame(a, i + j)
    if reached:
      return True
  return reached

print(jumpGame([2, 3, 1, 1, 4], 0))
True
False