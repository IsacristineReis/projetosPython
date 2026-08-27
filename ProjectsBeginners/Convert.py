print("==================================")
print("Convert Roman Numerals With Python")
print("==================================")

'''
1. I
2. II
3. III
4. IV
5. V
6. VI
7. VII
8. VIII
9. IX
10. X
50. L
100. C
500. D
1000. M
'''

num = input("Enter the roman numerals you want to converte: ").lower()

def roman_to_int(numeral):
    final_answer = 0
    for i in numeral:
        if i == "m":
            final_answer += 1000
        elif i == "d":
            final_answer += 500
        elif i == "c":
            final_answer += 100
        elif i == "l":
            final_answer += 50
        elif i == "x":
            final_answer += 10
        elif i == "ix":
            final_answer += 9
        elif i == "viii":
            final_answer += 8
        elif i == "vii":
            final_answer += 7
        elif i == "vi":
                final_answer += 6
        elif i == "v":
            final_answer += 5
        elif i == "iv":
            final_answer += 4
        elif i == "iii":
            final_answer += 3
        elif i == "ii":
            final_answer += 2
        elif i == "i":
            final_answer += 1
    print("The roman numerals you entered translates to: " + str(final_answer))

roman_to_int(num)
