class Road:
    def __init__(self, lenght=0, wight=0, high=0.0):
        self._lenght = lenght
        self._wight = wight
        self._high = high


    def asf_f(self):
        print(f'Нужно асфальта {round(self._lenght * self._wight * self._high * 25 / 1000, 3)} т')


a= Road(2000, 12, 0.12)
a.asf_f()
