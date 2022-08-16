import json

# Load morse code alphabet
f = open('./morse-code.json')
morse_file = json.load(f)

print('\nLetters are separated by spaces and words by "/". If a letter cannot be translated a "#" will appear in the output.')

machine_is_on = True

while machine_is_on:
    
    user_input = input('\nType the text you want to convert into morse code: ').lower()
    text_in_morse = ''

    # Translate user input into morse code
    for letter in user_input:
        try: 
            text_in_morse += morse_file[letter] + ' '
        except:
            text_in_morse += '# '

    print('\nThe answer is: ' + text_in_morse)

    want_to_continue = input("\nDo you want to continue? Type 'yes' to continue or type 'no' to exit: ").lower()

    if want_to_continue != 'yes':
        machine_is_on = False