def test_function():
    def inner_function():
        print("Я в области видимости test_fuction")
    inner_function()

test_function()    # ВЫзываем основную функцию, которая вызывает вложенную функцию. После проверки все прекрасно работает.

# Теперь пробуем вызвать вложенную функцию вне основной функции.

#inner_function()

# В результате вызова вложенной функции возникает ошибка, так как вложенная функция находится и существует только внутри основной функции.



