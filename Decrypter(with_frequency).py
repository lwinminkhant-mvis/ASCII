import os
# os.system('cls')

letter_frequencies = {
    "a": 8.17,
    "b": 1.49,
    "c": 2.78,
    "d": 4.25,
    "e": 12.70,
    "f": 2.23,
    "g": 2.02,
    "h": 6.09,
    "i": 6.97,
    "j": 0.15,
    "k": 0.77,
    "l": 4.03,
    "m": 2.41,
    "n": 6.75,
    "o": 7.51,
    "p": 1.93,
    "q": 0.10,
    "r": 5.99,
    "s": 6.33,
    "t": 9.06,
    "u": 2.76,
    "v": 0.98,
    "w": 2.36,
    "x": 0.15,
    "y": 1.97,
    "z": 0.07
}
letter_frequencies_upper = {
    "A": 8.17,
    "B": 1.49,
    "C": 2.78,
    "D": 4.25,
    "E": 12.70,
    "F": 2.23,
    "G": 2.02,
    "H": 6.09,
    "I": 6.97,
    "J": 0.15,
    "K": 0.77,
    "L": 4.03,
    "M": 2.41,
    "N": 6.75,
    "O": 7.51,
    "P": 1.93,
    "Q": 0.10,
    "R": 5.99,
    "S": 6.33,
    "T": 9.06,
    "U": 2.76,
    "V": 0.98,
    "W": 2.36,
    "X": 0.15,
    "Y": 1.97,
    "Z": 0.07
}
common_word = "esiarntolc"
# sentence = input('Give an encrypted message: ')
sentence = 'k"nqxg"{qw'  # i love you
sentence = 'qu_lq}rmlgefr'  # Swans tonight shift -2
sentence = r"N῀{j%htsknwrji%ymj%xhwnuy%tsq~%pjjux%ymj%xnslqj%gjxy%hfsinifyj%wnlmy%st|3%N῀r%zuifynsl%ny%yt%htqqjhy%j{jw~%ijhtiji%xjsyjshj%|nym%nyx%xhtwj%fsi%ymjs%zxj%ymfy%xytwji%qnxy%yt%iwn{j%ymj%ytu2:%tzyuzy3"
total    = 0
real_senteece  = ''
shifted = 0
scored_sentences = []
for shift in range(1,95):
    temp_sentence = ''
    num = 0

    for letter in sentence:
        number = 32 + ((ord(letter) - 32 + shift) % 95)

        if number > 126:
            number = (32 - (127 - ord(letter))) + shift
            temp_sentence += chr(number)
        else:
            temp_sentence += chr(number)

    for letter in temp_sentence:
        if letter in common_word:
            num += 1

    scored_sentences.append({
        'sentence': temp_sentence,
        'score': num,
        'shift': shift,
    })
        
    if num > total:
        total = num
        real_senteece = temp_sentence
        shifted = shift

scored_sentences.sort(key=lambda item: item['score'], reverse=True)

best_match = scored_sentences[0]
total = best_match['score']
real_senteece = best_match['sentence']
shifted = best_match['shift']

shift_number = ord(sentence[:1]) - ord(real_senteece[:1])

print()
print("The top 5 most likely sentences:")
for i, item in enumerate(scored_sentences[:5], start=1):
    print(i, item['sentence'], f"(score: {item['score']}, shift: {item['shift']})")
    print('------------------------')

print()
print(f"The shift number is      : {shift_number}")
