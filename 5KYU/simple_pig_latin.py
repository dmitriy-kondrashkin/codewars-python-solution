def pig_it(text):
    return ' '.join([word[1:]+word[:1] + 'ay' if word.isalpha() 
                     else word for word in text.split()])

text_1 = 'Pig latin is cool'                # igPay atinlay siay oolcay
text_2 = 'Hello world !'                    # elloHay orldway ! 
text_3 = "Quis custodiet ipsos custodes ?"  # uisQay ustodietcay psosiay ustodescay ? 
print(pig_it(text_3))