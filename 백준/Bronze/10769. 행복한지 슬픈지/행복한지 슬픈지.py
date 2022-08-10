sen = input()

happy = sen.count(':-)')
sad = sen.count(':-(')

if happy == 0 and sad == 0:
    print('none')
elif happy > sad:
    print('happy')
elif happy == sad:
    print('unsure')
elif sad > happy :
    print('sad')
