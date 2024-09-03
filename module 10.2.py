from threading import Thread
from time import sleep
import random

class Knight(Thread):
    def __init__(self, name, power):
         super().__init__()
         self.name = name
         self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')
        day = 0
        enemies = 100
        while True:
            sleep(1.0)
            enemies -= self.power
            day += 1
            if enemies <= 0:
                break
            sleep(random.randint(0,3))
            print(f'{self.name} сражается {day} дней, осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {day}дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')

