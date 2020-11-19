# Задание 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


# Вариант 1. Запуск скрипта через import (параметры заданы вручную)
# Здесь нужно указать путь до места, где размещен файл Task04_01_func
import os
import sys

from Lesson_04.Tasks.Task04_01_func import get_salary

print(f"ЗП: {get_salary(300, 2, 10)}")

# Вариант 2. Запуск отдельного скрипта с параметрами
path_script = f"{os.path.dirname(sys.argv[0])}\\Task04_01_func.py"
os.system(f"python {path_script} 10 20 30")
