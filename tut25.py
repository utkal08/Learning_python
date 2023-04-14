from collections import namedtuple

color = namedtuple('color',['red','green','blue'])

dict_color =  {'red':55, 'green': 155,'blue':255}


color = color(55,155,255)
#white = color(255,255,255)


print(dict_color['blue'])