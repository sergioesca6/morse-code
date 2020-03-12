#import re and sys
import re
import sys

def morse(text):
    #introduce all letters with their respected morse value.
    encrypt = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.==', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '.....'
    }
    #iterate encrypt elements to decrytp each morse code.
    decrypt = {value: key for key, value in encrypt.items()}

    #RegEx for input to check if we need to decrypt or encrypt
    if re.match(r'(\s|-|\.)+', text):
        return ''.join(decrypt[i] for i in text.split())
    return ' '.join(encrypt[i] for i in text.upper())

if __name__ == "__main__":
    print(morse(sys.argv[1]))