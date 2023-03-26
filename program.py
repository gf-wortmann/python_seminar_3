points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'XJ', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = input('Enter the word: ').upper()
print (word)
wordPrice = 0
lettercount = 0


for letter in word:
    for letterPrice in points_en:
        if letter in points_en[letterPrice]:
            wordPrice += letterPrice
            lettercount +=1
    if lettercount == 0:
        for letterPrice in points_ru:
            if letter in points_ru[letterPrice]:
                wordPrice += letterPrice

print(wordPrice)
