class Converter:
    def __init__(self):
        self.__temperature = 0

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temp):
        if temp[-1] == 'C':
            # (1°C × 9/5) + 32 = 33.8°F
            self.__temperature = float(temp[:-1]) * 9 / 5 + 32
        elif temp[-1] == 'F':
            # (1°F − 32) × 5 / 9 = -17.22°C
            self.__temperature = (float(temp[:-1]) - 32) * 5 / 9
        else:
            self.__temperature = 'Wrong format!'


CtoF = Converter()
CtoF.temperature = '1C'
print(CtoF.temperature)
CtoF.temperature = '1F'
print(CtoF.temperature)
CtoF.temperature = '120'
print(CtoF.temperature)
