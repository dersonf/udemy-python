#!/usr/bin/python3.6
class Carro:
    def __init__(self, vmax, vmin=0, delta=5):
        self.vmax = vmax
        self.vmin = vmin
        self.delta = delta


    def __str__(self):
        return f'max={self.vmax}, min={self.vmin}, delta={self.delta}'


    def acelerar(self, delta):
        self.vmin = self.vmin + delta
        if self.vmin > self.vmax:
            self.vmin = self.vmax
        return self.vmin 


    def frear(self, delta):
        self.vmin = self.vmin - delta
        if self.vmin < 0:
            self.vmin = 0
        return self.vmin


if __name__ == '__main__':
    c1 = Carro(180)

    print('Acelerando')
    for _ in range(25):
        print(c1.acelerar(8))


    print('Freando')
    for _ in range(10):
        print(c1.frear(delta=20))
