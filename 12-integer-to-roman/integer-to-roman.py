class Solution:
    def intToRoman(self, num: int) -> str:
        roman_series = [
            ("M",1000),
            ("CM",900),
            ("D",500),
            ("CD",400),
            ("C",100),
            ("XC",90),
            ("L",50),
            ("XL",40),
            ("X",10),
            ("IX",9),
            ("V",5),
            ("IV",4),
            ("I",1)
        ]

        r  = ""
        for symbol,value in roman_series:
            while num >= value:
                r += symbol
                num -=  value
        return r
        
        # roman = {
        #     'M': 1000,
        #     'D': 500,
        #     'C': 100,
        #     'L': 50,
        #     'X': 10,
        #     'V': 5,
        #     'I': 1
        # }

        # roman = {
        #     "M": 1000,
        #     "CM": 900,
        #     "D": 500,
        #     "CD": 400,
        #     "C": 100,
        #     "XC": 90,
        #     "L": 50,
        #     "XL": 40,
        #     "X": 10,
        #     "IX": 9,
        #     "V": 5,
        #     "IV": 4,
        #     "I": 1
        # }

        # s = ''
        # curr = num
        # for S , V in roman.items():
        #     while curr >= V :
        #         s += S
        #         curr -= V

        # s = s.replace('IIII','IV')
        # s = s.replace('VIV','IX')
        # s = s.replace('XXXX','XL')
        # s = s.replace('LXL','XC')
        # s = s.replace('CCCC','CD')
        # s = s.replace('DCD','CM')
        # return s
        
        
        