def game_core_v3(number: int = 1) -> int:
    """Находим случайное число по принципу бинарного поиска.
       Функция принимает загаданное число и возвращает число попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    import random   
    # Обозначаем переменную для подсчета попыток
    count = 0 
    # Задаем диапазон чисел  
    low = 1  
    right = 100  
      
    # Инициализация случайных чисел.  
    random.seed()  
      
    # Генерируем число, которое нужно угадать  
    number = random.randint(low, right)  
    while True:  
        count += 1  
        # Используем подход бинарного поиска  
        mid = (low + right) // 2   
        if mid == number:  
            break  
        elif mid < number:  
            low = mid + 1  
        else:  
            right = mid - 1  
   
    # Ваш код заканчивается здесm
    return count

print(f'Количество попыток: {game_core_v3()}')
