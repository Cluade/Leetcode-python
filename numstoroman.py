class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman =[]
        temp = []
        ge = num%10
        if ge <4:
            while ge >0:
                roman.append('I')
                ge -= 1 
        elif ge == 4:
            roman.append('IV')
        elif ge < 9 :
            roman.append('V')
            while ge-5 > 0:
                roman.append('I')
                ge -= 1
        elif ge ==9:
            roman.append('IX')
        shi = int((num%100 -num%10)/10)
        if shi <4:
            temp =[]
            while shi >0:
                temp.append('X')
                shi -= 1
            roman = temp + roman
        elif shi ==4:
            roman.insert(0,'XL')
        elif shi <9 :
            temp = ['L']
            while shi - 5 >0:
                temp.append('X')
                shi -= 1
            roman = temp + roman
        elif shi == 9:
            roman.insert(0,'XC')
        bai = int((num%1000 -num%100)/100) 
        if bai <4:
            temp =[]
            while bai >0:
                temp.append('C')
                bai -= 1
            roman = temp + roman
        elif bai ==4:
            roman.insert(0,'CD')
        elif bai <9 :
            temp = ['D']
            while bai - 5 >0:
                temp.append('C')
                bai -= 1
            roman = temp + roman
        elif bai == 9:
            roman.insert(0,'CM')
        qian = int((num%10000 -num%1000)/1000) 
        if qian<4:
            temp =[]
            while qian >0:
                temp.append('M')
                qian -= 1
            roman = temp + roman
        return ''.join(roman)

test = Solution()
print(test.intToRoman(900))
