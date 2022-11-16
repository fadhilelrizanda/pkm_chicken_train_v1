import os

with open('./training.txt', 'w') as out:
    for img in [f for f in os.listdir('./training/train/Chicken') if f.endswith('png')]:
        out.write('chickenv1/training/train/Chicken' + img + '\n')


with open('./testing.txt', 'w') as out:
    for img in [f for f in os.listdir('./training/val/Chicken') if f.endswith('png')]:
        out.write('chickenv1/training/val/Chicken' + img + '\n')
