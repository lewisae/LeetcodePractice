#13: convert roman numeral strings to an integer
numerals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
subtractChars = [("I","V"), ("I","X"), ("X","L"), ("X","C"), ("C","D"), ("C","M")]

def romanToInt(s: str) -> int:
    prevChar = ''
    intSum = 0
    for i in s:
        print(i)
        if (prevChar, i) in subtractChars:
            intSum -= 2*numerals[prevChar]
        intSum += numerals[i]
        prevChar = i
    return intSum

print(romanToInt("III"))
print(romanToInt("XIV"))
