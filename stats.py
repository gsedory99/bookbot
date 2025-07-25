def get_num_words(string):
   word_list = string.split()
   return len(word_list)

def character_counter(string):
   char_dict = {}
   for char in string:
      if char.lower() not in char_dict:
         char_dict[char.lower()] = 1
      else:
         char_dict[char.lower()] += 1
   return char_dict

def sort_counts(char_dictionary):
   list_of_values = []
   for key, value in char_dictionary.items():
       if key.isalpha():  # Only include alphabetic characters
         list_of_values.append({
               "char": key,
               "num": value,
         })
   def sort_on(items):
      return items["num"]
   sorted_list_of_values = sorted(list_of_values, reverse=True, key=sort_on)
   return sorted_list_of_values
