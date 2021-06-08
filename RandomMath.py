#!/usr/bin/env python3

from random import randrange
# Zenity (bash script)
十 = 10
百 = 100
千 = 1000
万 = 1_0000
億 = 1_0000_0000
兆 = 1_0000_0000_0000
京 = 1_0000_0000_0000_0000

level = 3

def _numberToKanji(number, response=""):
    
    if number >= 京:
        # Only needed this part if we need prefixes (ex: 二京)
        if number >= 2*京:
            response = _numberToKanji(number // 京, response)
        response += '京'
        number %= 京
    if number >= 兆:
        # Only needed this part if we need prefixes (ex: 二兆)
        if number >= 2*兆:
            response = _numberToKanji(number // 兆, response)
        response += '兆'
        number %= 兆
    if number >= 億:
        # Only needed this part if we need prefixes (ex: 二億)
        if number >= 2*億:
            response = _numberToKanji(number // 億, response)
        response += '億'
        number %= 億
    if number >= 万:
        # Only needed this part if we need prefixes (ex: 二万)
        if number >= 2*万:
            response = _numberToKanji(number // 万, response)
        response += '万'
        number %= 万
    if number >= 千:
        # Only needed this part if we need prefixes (ex: 二万)
        if number >= 2*千:
            response = _numberToKanji(number // 千, response)
        response += '千'
        number %= 千
    if number >= 百:
        # Only needed this part if we need prefixes (ex: 二百)
        if number >= 2*百:
            response = _numberToKanji(number // 百, response)
        response += '百'
        number %= 百
    if number >= 十:
        # Only needed this part if we need prefixes (ex: 二十)
        if number >= 2*十:
            response = _numberToKanji(number // 十, response)
        response += '十'
        number %= 十
    
    # Finally the single digits...
    if number == 9:
        response += '九'
    elif number == 8:
        response += '八'
    elif number == 7:
        response += '七'
    elif number == 6:
        response += '六'
    elif number == 5:
        response += '五'
    elif number == 4:
        response += '四'
    elif number == 3:
        response += '三'
    elif number == 2:
        response += '二'
    elif number == 1:
        response += '一'
    elif number == 0 and response == '': # Avoid trailing 零 on every number
        response += '零'
        
    return response

def printNumber(number):
    value = ''
    if number == 0:
        return '0'
    
    while number >= 万:
        value = '_' + str(number % 万).rjust(4, '0') + value
        number = number // 万
    value = str(number) + value
    return value
    
def kanjiThenNumberTest():
    number = randrange(9_9999_9999)
    print(_numberToKanji(number), end='')
    input('')
    print(printNumber(number))
    input('')
    
def numberThenKanjiTest():
    number = randrange(9_9999_9999)
    print(printNumber(number), end='')
    input('')
    print(_numberToKanji(number))
    input('')
    
def printSimpleMathProblemVertical(num1, operator, num2):
    kanji1 = _numberToKanji(num1)
    kanji2 = _numberToKanji(num2)
    lenKanji1 = len(kanji1)
    lenKanji2 = len(kanji2)
    longestLength = lenKanji1
    if lenKanji2 > longestLength:
        longestLength = lenKanji2
    half = longestLength // 2
    
    # Since we want o print them vertically side-by-side
    # we have t0 iterate through and calculate each line
    # Example:
    #三   四
    #百   百
    #八 + 九
    #十   十
    #六   三
    for i in range(longestLength, 0, -1):
        line = ''
        if lenKanji1 - i >= 0:
            line += kanji1[lenKanji1 - i]
        else:
            line += '　'
        line += ' '
        if i == half:
            line += operator
        else:
            line += ' '
        line += ' '
        if lenKanji2 - i >= 0:
            line += kanji2[lenKanji2 - i]
        else:
            line += '　'
        print(line)
    
def kanjiSimpleAdditionTestHorizontal():
    left = randrange(1000)
    right = randrange(1000)
    print(_numberToKanji(left) + "　+　" + _numberToKanji(right) + "　=　", end='')
    calculatedAnswerNumber = left + right
    userAnwer = input('').strip()
    if userAnwer == _numberToKanji(calculatedAnswerNumber):
        print('Correct')
    else:
        print('Incorrect, answer is: ' + _numberToKanji(calculatedAnswerNumber))
    input('')

def kanjiSimpleAdditionTestVertical():
    left = randrange(1000)
    right = randrange(1000)
    operator = randrange(2)
    if operator == 0:
        printSimpleMathProblemVertical(left, '+', right)
        calculatedAnswerNumber = left + right
    elif operator == 1:
        if right > left:
            temp = left
            left = right
            right = temp
        printSimpleMathProblemVertical(left, '-', right)
        calculatedAnswerNumber = left - right
    userAnwer = input('').strip()
    if userAnwer == _numberToKanji(calculatedAnswerNumber):
        print('Correct')
    else:
        print('Incorrect, answer is: ' + _numberToKanji(calculatedAnswerNumber))
    input('')
    
#print(_numberToKanji(2_3548_4812_5739_5729_1938))
#print(_numberToKanji(73_6428))

if level == 1:
    kanjiThenNumberTest()
elif level == 2:
    if randrange(10) > 5:
        kanjiThenNumberTest()
    else:
        numberThenKanjiTest()
elif level == 3:
    val = randrange(20)
    if val > 0:
        kanjiSimpleAdditionTestVertical()
    elif val > 9:
        kanjiSimpleAdditionTestHorizontal()
    elif val > 5:
        kanjiThenNumberTest()
    else:
        numberThenKanjiTest()
else:
    print('Not Ready')
