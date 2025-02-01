import math
import time
# ~/.wakatime.cfg
# Morse Code
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def TheSecretOption():
    print("You're out of touch, im out of time")
    print("STAY WITH MEEEEEEEEEEEEEE")
    print("And one day she cried so much that the tears stopped. sara didnt cry after that. takayuki was right, tears brought failure. sara was to be no failure, for she")
    print("Sara had too much debt to afford it. she needed to be a moral, stable, and sucessful tengu warrior serving the raiden shogun whilst being of the kujou clan and defending inazuma.")
    print("And also third in command. She had no idea who second was.")
    print("Not very cool frfr like what the hell man hahahahhahahahhahahahahhahahahahahhahahahahhahahhahahahahhahahahhahahahahahahhhahahahhhahahhahahhahahhahahahahhahahhahhahhahahahhaha")
    print("weight of responsibilities and lack therof at tthe same time is what made kujou sara and sangonomiya kokomi so similar. they were one in the same, believe it or not. and honestly, she wouldnt have it any other way.")
    print("The General and The Priestess. Electro and Hydro, Electro-Charged. Defined by the scars, invisible and physical the same. definned by one task, one past, and the consequences. and they were both tired. so tired. and I loved you, my dear. my love, how could you leave me, with your matching scars and our intertwined lives.")
    print("And the fish and the bird cannot truly meet. the fish jumps to grab and drown the bird, and the bird swoops down to kill the fish. both end up dying. the fish is thrown at a ship and killed, and the bird's wing is too torn to do anything but float. ironic tragedy. hahahahahahahahhahahahaah")
    print ("and the small ones waited. they cried out in pain byt they waited. that was the important part. she waited yet held her temper and her tongue. a true warrior of mind and spirit and everything in between.")
    print("Mikey gasped at the sight of his own blood staining the bathtub red. red. red. it was everything, everywhere, and seemed to encompass everything. it was getting hard to get out of the water. he couldnt move. couldnt. he watched as he went under, how if he held his breath, he wouldnt drown. he forgot to. as the water got into his lungs, he oculd see the life he lived flashing past his eyes. this was it. he was going to die here. goodnight cruel world. ")
    print()



def MorseCode():
    
    morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}
    def to_morse_code(message):
        morse_code = ''
        for char in message.upper():
            if char in morse_dict:
                morse_code += morse_dict[char] + ''
            return morse_code
    def main():
        message = input("Enter Text:")
        print("Message: ", message, "\nMorse code sequence: ", to_morse_code(message))
        main()


# Caesar Cipher

def CaesarCipher():
    alphabet = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" # "zyxwvutsrqponmlkjihgfedcba"
    get_letter, keyword = 0, []
    text = str(input("Enter Text:"))
    key = int(input("Enter Key:"))
    if 0 < key <= 26:
        for letter in text:
            get_letter = alphabet.index(letter) + key
            keyword.append(alphabet[get_letter])
            print("".join(keyword) + " is the keyword!")
    else:
        print("Key must be between 1 and 26.")



# Encrypting

print("Pick a Cipher")
print("Caesar")
print("Morse")

cipher = input("Choose:")
if cipher == "Caesar":
    CaesarCipher()
if cipher == "Morse":
    MorseCode()




# if cipher == "Affine":
#    def affine(a: int, b: int, c: int, s: str):
#        import string
#        D = dict(enumerate(string.ascii_lowercase, start = 0))
#        E = {v: k for k, v in D.items()}
#        size = len(string.ascii_lowercase)
#        ret = ""
#        print(size)
#        for c in s:
#            N = E[c]
#            val = a * N + b
#            val = val % size
#            print(f"{c}({N}) -> {D[val]}(val)")
#            ret += D[val]
#            return ret
#    affine(7, 3, 'foobar')