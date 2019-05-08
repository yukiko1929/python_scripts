import psutil

class CPU:
    def __init__(self, core, temp):
        self.core = core
        self.temp = temp

    def __str__(self):
        return  'cpi_temp(core:%s, temp:%s)' % (self.core, self.temp)
