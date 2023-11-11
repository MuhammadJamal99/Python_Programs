wordsNum = 3
with open('InputFile.txt', 'r') as f:
    data = f.read().split()

formatted_data = []
for i, item in enumerate(data):
    if i % wordsNum == 0:
        formatted_data.append('(')
    if item.isnumeric():
        formatted_data.append(item)
    else:
        formatted_data.append("'" + item + "'")
    if (i+1) % wordsNum == 0 or (i+1) == len(data):
        if (i+1) == len(data): # if this is last word
            formatted_data.append(')')
        else:
            formatted_data[-1] += ')' # add closing bracket to last element of list

    elif (i+1) % wordsNum != 0: #if current word is not end of 4 word group
        formatted_data.append(',')

formatted_data_str = ''.join(formatted_data)
formatted_data_str = formatted_data_str.replace(')(', '),-(')

tuples = [eval(x) for x in formatted_data_str.split('-')]

with open('OutputFile.txt', 'w') as f:
    for t in tuples:
        f.write(','.join(str(x) for x in t) + ',\n')