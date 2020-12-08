# ООП
#
# Плюсы:
# - Повторное использование кода
# - Повышение читаемости и гибкости кода
# - Ускорение процесса поиска ошибок и их исправления
# - Повышение безопасности проекта
# - Простота модификации проекта
#
# Минусы:
# - Необходимость хорошего понимания предметной области
# - Необходимость хорошего представления структуры приложения
# - Сложность в разбиение проекта на классы
#
# Области видимости
# - локальные
# - глобальные
#
# Модификаторы доступа
# - Публичный/открытый (public)
# - Защищенный: ограниченный на уровне соглашения, не стоит обращаться вне класса (protected). Например _password
# - Приватный/закрытый (private)
#
#
# Системные методы функций и дочерних классов
# __init__() - конструктор класса, срабатывает при создании объекто
# __del__()  - деструктор, срабатывает при удалении объекта
# __str__() - срабатывает при передаче объекта str() и print(), преобразует объект к строке
# __add__() - срабатывает при участии объекта в операции сложения в качестве операнда с левой стороны,
# обепечивает перегрузку оператора сложения
#
# __setattr__() - срабатывает при выполнении операции присваивания значения атрибуту объекта
# __getitem__() - срабатывает при извлечении элемента по индексу
# __call__() - срабатывает при обращении к экземпляру класса как к функции
#
# __gt__() - соответствует оператору ">"
# __lt__() - соответствует оператору "<"
# __ge__() - соответствует оператору ">=" (?)
# __le__() - соответствует оператору "<="
# __eq__() - соответствует оператору "=="
# __iadd__() - соответствует операции "Сложение и присваивание" +=
# __isub__() - соответствует операции "Вычитание и присваивание" -=
#
# Интерфейсы
#
#
#
# Декораторы
#
#
# Статические метода и методы класса
# @staticmethod - декторатор для метода класса, такой метода вызывается напрямую через имя класса (статический метод)
# ** не важно у какого класса вызывается
#
# @classmethod - декоратор для метода класса, такой метода получает класс в качестве первого аргумента
#
# __name__ - имя класса
# __module__ - имя модуля
# __dict__ - словарь с атрибутами класса
# __bases__ - кортеж с базовыми классами
# __doc__ - строка документации класса
# __class__ - объект-класс, экземпляром которого является данный инстанс
# __init__ - конструктор
# __del__ - деконструктор
# __hash__ - возвращает хещ-значение объекта, равное 32-битному числу
#
# ! Собственные исключения
#
#