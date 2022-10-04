
sum = 0
numbers = [0] * 5
for i in range(5):
    numbers[i] = int(input('Enter the number: '))
    if i == 0:
        min = max = numbers[i]
    else:
        if (min > numbers[i]):
            min = numbers[i]
        elif (max < numbers[i]):
            max = numbers[i]
    sum += numbers[i]
sum = sum - min - max
# print ('Total : ', sum, 'Average: ', sum / 5.0)
print(sum)
#
#