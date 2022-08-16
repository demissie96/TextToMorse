import json

f = open('./morse-code.json')
morse_file = json.load(f)

print('\nLetters are separated by spaces and words by "/". If a letter cannot be translated a "#" will appear in the output.\n')
user_input = input('Type the text you want to convert into morse code: ').lower()

text_in_morse = ''

for letter in user_input:
    try: 
        text_in_morse += morse_file[letter] + ' '
    except:
        text_in_morse += '# '

print('The answer is: ' + text_in_morse)

