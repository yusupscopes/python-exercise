allGuests = {
    'Alice' : {'apples' : 5, 'pretzels' : 12},
    'Bob'   : {'ham sandwiches' : 3, 'apples' : 3},
    'Carol' : {'cups' : 3, 'apple pies' : 1}
}

def totalBrough(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples        ' + str(totalBrough(allGuests, 'apples')))
print(' - Cups          ' + str(totalBrough(allGuests, 'cups')))
print(' - Cakes         ' + str(totalBrough(allGuests, 'cakes')))
print(' - Ham Sandwiches' + str(totalBrough(allGuests, 'ham sandwiches')))
print(' - Apple Pies    ' + str(totalBrough(allGuests, 'apple pies')))