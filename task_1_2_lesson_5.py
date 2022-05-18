"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например
# """
def get_odd_numbers(num):
    yield (array for array in range(1, num + 1, 2))

"""
Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
"""
def get_odd_numbers_no_yield(num):
    return (array for array in range(1, num + 1, 2))

if __name__ == "__main__":
    result = get_odd_numbers(100)
    result_no_yield = get_odd_numbers_no_yield(100)

    print(type(result))
    print(type(result_no_yield))
    result = get_odd_numbers(100)
    for el in range(100):
        print(next(result))
