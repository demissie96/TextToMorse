import json

print('********************')

f = open('./morse-code.json')
morse_file = json.load(f)
print(json.dumps(morse_file, indent=4, sort_keys=False))





print('********************')