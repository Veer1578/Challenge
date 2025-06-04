class int2rman:
    def __init__(self):
        self.valuemap = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    def convert(self, num):
        rman_num = ''
        for value, symbol in self.valuemap:
            while num >= value:
                rman_num += symbol
                num -= value
        return rman_num
    
converter = int2rman()
print(converter.convert(1994))