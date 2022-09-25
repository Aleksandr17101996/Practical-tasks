def sort_list(list_nums):
    n = 1
    while n < len(list_nums):
        for i in range(len(list_nums) - n):
            if list_nums[i] > list_nums[i + 1]:
                list_nums[i], list_nums[i + 1] = list_nums[i + 1], list_nums[i]
        n += 1
    return list_nums
    

def binary_search(list_nums, start, end, number):
    while end > start + 1:
        middle = (start + end) // 2
        if list_nums[middle] > number:
            end = middle
        else:
            start = middle
    return start    


def main(list_nums, numb):
    list_nums = sort_list(list_nums)
    if numb >= list_nums[-1]:
        print('Число больше, либо равно максимальному в списке!')
    elif numb <= list_nums[0]:
        print('Число меньше, либо равно минимальному в списке')
    else:
        print('Номер позиции элемента:', binary_search(list_nums, -1, len(list_nums), numb))


if __name__ == '__main__':
    while True:
        try:
            list_of_num = input('Введите через пробел числовую последовательность: ').split()
            list_of_num = [float(i) for i in list_of_num]
            break
        except ValueError:
            print('\nВ числовой последовательности не все данные - числа!\nПопробуйте заново!\n')
    
    while True:
        try:
            number = float(input('Введите число: '))
            break
        except ValueError:
            print('\nВы ввели не число!\nПопробуйте заново!\n')
    
    main(list_of_num, number)

        
