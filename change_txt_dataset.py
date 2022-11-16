import os

with open('chicken/data/chicken3/training.txt', 'w') as out:
    for img in [f for f in os.listdir("chicken/data/chicken3" + '/train') if f.endswith('jpg')]:
        out.write('chicken/data/chicken3/train/' + img + '\n')


with open('chicken/data/chicken3/valid.txt', 'w') as out:
    for img in [f for f in os.listdir('chicken/data/chicken3' + '/valid') if f.endswith('jpg')]:
        out.write('chicken/data/chicken3/valid/' + img + '\n')
