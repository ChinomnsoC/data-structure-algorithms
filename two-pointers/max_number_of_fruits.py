# For every fruit at index right, increment its count in fruit_dict.
# While len(fruit_dict) > 2, decrement count for fruits[left]. 
# If count reaches zero, remove it from the dictionary. Move left forward.
# Always update output = max(output, right - left + 1) after processing.

from collections import defaultdict

def total_fruit(fruits):
  # Initialise a left and right pointer both at index 0
  left, right = 0, 0
  fruit_dict = defaultdict(int)
  output = -1
  for i in range(len(fruits) - 1):
    if len(fruit_dict) < 2 and i not in fruit_dict:
      print("fruits[right]", fruits[right])
      fruit_dict[fruits[i]] += 1
      output = right - left + 1
      right += 1
      continue
      print("fruits[right]", fruits[i])
      print("first", output)
    elif len(fruit_dict) >= 2 and i not in fruit_dict:
      fruit_dict[fruits[i]] -= 1
      right += 1
      left += 1
      output = right - left + 1
      print("second", output)
    elif len(fruit_dict) >= 2 and i in fruit_dict:
      fruit_dict[fruits[i]] += 1
      right += 1
      output = right - left + 1
      print("third", output)
  return output



from collections import defaultdict

def total_fruit(fruits):
  # Initialise a left and right pointer both at index 0
  left, right = 0, 0
  fruit_dict = defaultdict(int)
  output = -1
  for i in range(len(fruits) - 1):
    if len(fruit_dict) < 2 and fruits[i] not in fruit_dict:
      fruit_dict[fruits[i]] += 1
      right += 1
      output = right - left + 1
      print("fruits[right]", fruits[i])
      print("first", output)
    elif len(fruit_dict) >= 2 and fruits[i] not in fruit_dict:
      fruit_dict[fruits[i]] -= 1
      right += 1
      left += 1
      output = right - left + 1
      print("second", output)
    elif len(fruit_dict) >= 2 and fruits[i] in fruit_dict:
      fruit_dict[fruits[i]] += 1
      right += 1
      output = right - left + 1
      print("third", output)
  return output