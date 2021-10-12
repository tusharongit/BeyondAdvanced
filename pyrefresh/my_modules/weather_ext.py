# class and methods for extending weather data when it is windy or rainy

from weather import Weather


class WeatherExtended(Weather):
    def __init__(self, temp, desc, moreInfo):
        super().__init__(temp, desc)
        self.moreInfo = moreInfo


    def __str__(self):
        prn = super().__str__()
        if self.desc == 'rainy':
            prn += ' with a {}% chance of rain'.format(self.moreInfo)
        elif self.desc == 'snowy':
            prn += ' with a {}% chance of snow'.format(self.moreInfo)
        elif self.desc == 'windy':
            prn += ' with a windpeed of {} mph'.format(self.moreInfo)
        else:
            pass
        return prn



if __name__ == '__main__':
    we1 = WeatherExtended(15, 'rainy', 68)
    we2 = WeatherExtended(2, 'snowy', 80)
    we3 = WeatherExtended(12, 'windy', 20)
    print(we1)
    print(we2)
    print(we3)