# Напишите функцию, которая будет принимать список чисел и проверять, является ли каждое число больше
# суммы всех предыдущих чисел. Если все числа в списке успешно пройдут проверку, функция
# должна вернуть True, в противном случае — False.
# Примечание: первое число в списке всегда проходит проверку.
# Примеры:
# greater_than_sum([2, 3, 7, 13, 28]) ➞ True
# # 3 > 2 = True
# # 7 > 2 + 3 = True
# # 13 > 2 + 3 + 7 = True
# # 28 > 2 + 3 + 7 + 13 = True
# greater_than_sum([1, 2, 4, 6, 13]) ➞ False
# # 2 > 1 = True
# # 4 > 1 + 2 = True
# # 6 > 1 + 2 + 4 = False
# # 13 > 1 + 2 + 4 + 6 = False


def greater_than_sum(lst):
    sum = 0
    for i in range(len(lst) - 1):
        sum = sum + lst1[i]
        if lst1[i + 1] > sum:
            print(f" {lst1[i+1]} > {sum} = True")
        else:
            print(False)


lst1 = [1, 3, 7, 15, 27]
greater_than_sum(lst1)
