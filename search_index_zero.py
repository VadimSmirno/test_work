import random

def search_index_zero():
    list_unit = [1 for _ in range(random.randint(5, 10))]
    list_zero = [0 for _ in range(random.randint(5, 10))]
    list_unit_zero = [*list_unit, *list_zero]
    print(list_unit_zero)
    for index, number in enumerate(list_unit_zero):
        if number == 0:
            print(f'Индекс первого нуля {index}')
            break


if __name__ == '__main__':
    search_index_zero()