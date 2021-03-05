array = []
while len(array) < 7:
    imput = input('Upisi kilazu: ')
    array.append(float(imput))

def med(list):
    bot_to_top = sorted(list)
    length = len(bot_to_top)
    median = bot_to_top[int(length/2)]
    print('the median is: ', median)

def avg(list):
    avrage = sum(list)/len(list)
    print('the avrage is: ',avrage)

if len(array) == 7:
    med(array)
    avg(array)

mainloop()
