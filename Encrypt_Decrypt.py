alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def Encrypt(text,shift):
  cipher_text=""
  for letter in text:
    pos=alphabet.index(letter)
    new_pos=pos+shift
    new_letter=alphabet[new_pos]
    cipher_text+=new_letter
    print(f"the encoded message is {cipher_text}")

Encrypt(text="loki",shift=2)
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 




#decrypt
def decrypt(cipher_text,shift_amount):
  decrypt_text=""
  for letter in cipher_text:
    position=alphabet.index(letter)
    new_position=position-shift
    decrypt_text+=alphabet[new_position]
    print(f"The encoded text is {decrypt_text}")

if direction=="encode":
  encrypt(plain_text=text, shift_amount=shift)
else:
  decrypt(cipher_text=text,shift_amount=shift)
