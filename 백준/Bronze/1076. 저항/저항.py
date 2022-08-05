color = {'black' : 0, 
'brown' : 1, 
'red' : 2, 
'orange' : 3,
'yellow' : 4,
'green' : 5,
'blue' : 6,
'violet' : 7,
'grey' : 8,
'white' : 9}

one = input()
two = input()
three = input()

print((color[one] * 10 + color[two]) * 10 ** (color[three]))