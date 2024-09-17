# Домашнее задание по теме "Множественное наследование".
# Задача "Мифическое наследование"

# объявление класса Horse с атрибутами
class Horse:

    def __init__(self):
        # атрибуты класса:
        self.x_distance =  0    # пройденный путь
        self.sound = 'Frrr' # звук, издаваемый лошадью
        # функция, которая позволяет обращаться к классу следующему в цепочке наследования (Eagle)
        super().__init__()

    # метод run, изменение дистанции, увеличивает x_distance на dx
    def run(self, dx):
        self.x_distance += dx
        return self.x_distance  # возврат нового местоположения x_distance

# объявление класса Eagle с атрибутами
class Eagle:

    def __init__(self):
        # атрибуты класса:
        self.y_distance = 0 # высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл

    # метод fly, изменение дистанции, увеличивает y_distance на dy
    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance  # возврат нового местоположения y_distance

# объявление класса Pegasus. Наследуется от Horse и Eagle в том же порядке
class Pegasus(Horse, Eagle):
    # инициализация объектов класса
    def __init__(self):
        super().__init__()  # обращение к родительскому классу в порядке иерархии (Horse, Eagle)

    # метод move изменения дистанции. запускаются наследованные методы run и fly соответственно.
    def move(self, dx: int, dy: int):
        super().run(dx) # запуск метода run родительского класса Horse
        super().fly(dy) # запуск метода fly родительского класса Eagle

    # метод get_pos, возвращает текущее положение пегаса в виде кортежа (x_distance, y_distance)
    def get_pos(self):
        return (self.x_distance, self.y_distance)   # возврат текущей новой позиции Пегаса

    # метод voice, печатает значение унаследованного атрибута sound
    def voice(self):
        print(self.sound)   # печать унаследованного звука

# исходные данные и вывод результатов
p1 = Pegasus()
# вывод положения
print(p1.get_pos())
# перемещение объекта
p1.move(10, 15)
# вывод положения
print(p1.get_pos())
# перемещение объекта
p1.move(-5, 20)
# вывод положения
print(p1.get_pos())
# вывод звука объекта
p1.voice()
