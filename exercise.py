def draw_shape(options):
  shape = ""

  for r in range(options['rows']):
    for c in range(options['cols']):
      shape += options['char']

    shape += "\n"
    

  return shape

my_var = {'rows': 4, 'cols': 4, 'char': '*'}

print(draw_shape(my_var))

my_var2 = {'rows': 3, 'cols':10, 'char': '0'}

print(draw_shape(my_var2))
#This assginment had the wrong date