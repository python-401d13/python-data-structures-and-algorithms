def insert_shift_array(lst, el):
  if len(lst) % 2 == 0:
    i = len(lst) // 2
  else:
    i = len(lst) // 2 + 1
  
  lst = lst[:i] + [el] + lst[i:]

  return lst