###
# Return the color that occurs most frequently. In case of a tie
# return the most frequent colors sorted alphabatically.
###


from collections import Counter
import collections

def top_color(_item_list):
  _flat = []
  _top_colors = []

  # flatten array of arrays 
  for _items in _item_list:
    for _each_items in _items:
      _flat.append(_each_items)
  print("_flat:", _flat)

  # counts occurances of words
  _counted = Counter(_flat)
  print("_couted:", _counted)

  # finds keys with max occurances
  for _max_values in [max(_counted.values())]:
      for key,val in _counted.items():
        if val == _max_values:
          _top_colors.append(key)

  return sorted(_top_colors)
  
  
def main():
  image1 = [
    ['red', 'red', 'green'],
    ['black', 'blue', 'black'],
    ['red', 'yellow', 'yellow']
  ]

  image2 = [
    ['red', 'green', 'green'],
    ['black', 'blue', 'black'],
    ['red', 'yellow', 'yellow']
  ]

  print("_top_colors:", top_color(image1))

if __name__ == "__main__":
  main()
