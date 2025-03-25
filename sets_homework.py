def check_pangram(input):
 global str_input

 str_input = input.upper()

 str_input = set(str_input)
 return str_input

str_input = input("please enter the pangram")
dist_list = [ char for char in str_input.lower() if ord(char) in range(ord('a')+1, ord('z')+1)]
str_input = set(str_input)
if len(str_input) == 26:
  print('String is a Pangram')
else:
   print('String is not a Pangram')



check_pangram(str_input)