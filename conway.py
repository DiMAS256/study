# Игра "Жизнь"

import random
import time
import copy

width = 60  # ширина
height = 20  # высота

# Создание списка списков для клеток
nextcells = []
for x in range (width):
    column = []  # создание нового столбца
    for y in range (height):
        if random.randint (0, 1) == 0:
            column.append ('#')  # добаление живой клетки
        else:
            column.append(' ')  # добаление мертвой клетки
    nextcells.append(column)  #переменная nextcells содержит список столбцов

while True:  # Основной цикл программы
    print ('\n\n\n\n\n')  # отделим каждый шаг с помощью символов новой строки
    currentcells = copy.deepcopy (nextcells)
    
    # Вывод текущих клеток на экран
    for y in range (height):
        for x in range (width):
            print (currentcells[x][y], end = '')  #вывод решетки или пробела
        print()  # вывод символа новой строки в конце
        
    # Вычисление клеток на следующем шаге на основе клеток текущего шага
    for x in range (width):
        for y in range (height):
            # Получение соседних координат
            
            # Выражение '% width' гарантирует, что значение leftcoord всегда находится между 0 и width - 1
            leftcoord = (x - 1) % width
            rightcoord = (x + 1) % width
            abovecoord = (y - 1) % height
            belowcoord = (y + 1) % height
            
            # Вычисление количества живых соседних клеток 
            numneighbors = 0
            if currentcells [leftcoord][abovecoord] == '#':
                numneighbors += 1  # жива соседняя клетка слева сверху
            if currentcells[x][abovecoord] == '#':
                numneighbors += 1  # жива соседняя клетка сверху
            if currentcells [rightcoord][abovecoord] == '#':
                numneighbors += 1  # жива соседняя клетка сверху
            if currentcells[leftcoord][y] == '#':
                numneighbors += 1  # жива соседняя клетка слева
            if currentcells[rightcoord][y] == '#':
                numneighbors +=1  # жива соседняя клетка справа
            if currentcells [leftcoord][belowcoord] == '#':
                numneighbors += 1  # жива соседняя клетка слева снизу
            if currentcells[x][belowcoord] == '#':
                numneighbors += 1  # жива соседняя клетка снизу
            if currentcells [rightcoord][belowcoord] == '#':
                numneighbors += 1  # жива соседняя клетка справа снизу
                
            # Изменение клетки на основе правил игры "Жизнь"
            if currentcells[x][y] == '#' and (numneighbors == 2 or numneighbors == 3):
                
            
                # Живые клетки с двумя или тремя живыми соседями остаются живыми
                nextcells[x][y] = '#'
            elif currentcells[x][y] == ' ' and numneighbors == 3:
                # Мертвые клетки с тремя живыми соседями оживают
                nextcells[x][y] = '#'
            else:
                # Все остальные клетки умирают или остаются мертвыми
                nextcells[x][y] = ' '
    time.sleep(1)  #добавим секундную паузу, чтобы уменьшить мерцание
          