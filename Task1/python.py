# ОПАСНЫЙ КОД - может сломаться!
def dangerous_function():
    try:
        number = int(input("Введите число: "))  # Что если введут текст?
        result = 10 / number  # Что если введут 0?
        print(result)
    except Exception as e:
        print(f"{e} - Так нельзяб пробуй еще")
    else:
        print("qwefgr235354")


# Если пользователь введёт "hello" или 0 - программа УМРЁТ
dangerous_function()
