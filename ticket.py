def main():
    while True:
        try:
            count_tickets = int(input('Введите количество билетов, которые желаете приобрести: '))
            if count_tickets <= 0:
                print('\nОшибка! Введите значение большее, чем ноль.')
            else:
                break
        except ValueError:
            print('\nОшибка! Укажите значение цифрой.')
    i = 0
    result = []
    while i != count_tickets:
        while True:
            try:
                current_age = int(input('Введите возраст посетителя для {}-го билета: '.format(i + 1)))
                if current_age <= 0:
                    print('\nОшибка! Введите значение большее, чем ноль.')
                else:
                    result.append(current_age)
                    i += 1
                    break
            except ValueError:
                print('\nОшибка! Укажите значение цифрой.')

    sum_for_pay = 0
    for i in result:
        if i < 18:
            pass
        elif 18 <= i < 25:
            sum_for_pay += 990
        elif i >= 25:
            sum_for_pay += 1390

    if len(result) > 3:
        sum_for_pay = int(sum_for_pay * 0.9)

    print('Итого к оплате: ', sum_for_pay)

main()