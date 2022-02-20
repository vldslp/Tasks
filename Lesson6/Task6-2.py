class Road:

    def asf_f(self, lenght, wight, high):
        self._lenght = lenght
        self._wight = wight
        self._high = high
        print(f'Нужно асфальта {round(lenght * wight * high * 25 / 1000, 3)} т')


Road().asf_f(2000, 12, 0.12)
