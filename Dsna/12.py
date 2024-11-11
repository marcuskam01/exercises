class Solution:
    def intToRoman(self, num: int) -> str:
        ir_dict = {
        "M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,
        "L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}

        # key is roman letter, value is int
        # for roman in ir_dict:
        #     print(roman, ir_dict[roman])
        
        res = ""
        for roman in ir_dict:
            place_val = num // ir_dict[roman]
            if place_val > 0:
                res += (place_val*roman)
                num = num % ir_dict[roman]

        return res 