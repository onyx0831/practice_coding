def base26_to_decimal(s):
    s = s.upper()
    result = 0
    for i, char in enumerate(reversed(s)):
        value = ord(char) - ord('A') + 1
        result += value * (26 ** i)
    return result

base26 = input()
decimal = base26_to_decimal(base26)
print(decimal)
