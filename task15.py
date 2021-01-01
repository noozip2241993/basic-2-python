import random
positions = ['Husband','Wife','Father','Mother','Brother']
def shuffling_printitng(list):
    random.shuffle(list)
    return list
print(shuffling_printitng(positions))