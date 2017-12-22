import re

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print(f'searching for {pat}')
        print(re.findall(pat, phrase))
        print('\n')

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_patterns = ['sd+']

multi_re_find(test_patterns, test_phrase)
