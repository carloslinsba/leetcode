class Solution(object):
    num =0
    s=""
    
    def int_Roman_char(self, n , roman_char):
        for num in range (n):
            self.s+= roman_char

    def divides(self, dividing_for, roman_char): 
        a:int = self.num /dividing_for
        if a>=1:
            self.int_Roman_char(int(self.num/dividing_for), roman_char=roman_char)
            return True
        return False

    def operation_thousands(self):
            if self.divides(1000, 'M'):
                new_number = str (self.num)[1:]
                self.num = int(new_number)

    def operation_hundreds(self):
        if self.divides(900, 'CM'):
            self.num = self.num - 900
        if self.divides(500, 'D'):
            self.num = self.num - 500
        if self.divides(400, 'CD'):
            self.num = self.num - 400
        if self.divides(100, 'C'):
            new_number = str (self.num)[1:]
            self.num = int(new_number)
        
    def operation_decimals(self):
        if self.divides(90, 'XC'):
            self.num = self.num - 90
        if self.divides(50, 'L'):
            self.num = self.num - 50
        if self.divides(40, 'XL'):
            self.num = self.num - 40
        if self.divides(10, 'X'):
            new_number = str (self.num)[1:]
            self.num = int(new_number)

    def operation_singles(self):
        if self.divides(9, 'IX'):
            self.num = self.num - 9
        if self.divides(5, 'V'):
            self.num = self.num - 5
        if self.divides(4, 'IV'):
            self.num = self.num - 4
        if self.divides(1, 'I'):
            self.num = 0
        
    
    def intToRoman(self, num:int):
        self.num = num
        self.operation_thousands()
        self.operation_hundreds()
        self.operation_decimals()
        self.operation_singles()

        return self.s
