"""
Реализовать базовый класс "Светофор", с таймером переключения цветов
"""


from time import sleep


class TrafficLight:
    colors = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}

    def running(self):
        for key, value in self.colors.items():
            count = value
            print(f'Загорелся {key} свет светофора. Ожидание {value} сек')
            while count != 0:
                print(count, end='')
                sleep(1)
                count -= 1
                print('\r', end='')


a = TrafficLight()
a.running()

