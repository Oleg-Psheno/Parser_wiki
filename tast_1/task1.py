def task(array):
    return 'OUT: ' + str(array.index('0'))


data = '111111111111111111111111100000000'

print(task(data))
# result
# OUT: 25

# Сложность этого алгоритма O(n)