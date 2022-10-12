from typing import List

def insertionSort(array) -> List[int]:
  for index in range(1, len(array)):
    key = array[index]    
    indexo = index - 1
    while indexo >= 0 and key < array[indexo]:
      array[indexo + 1] =  array[indexo]
      indexo -= 1
    array[indexo + 1] = key
  return array
