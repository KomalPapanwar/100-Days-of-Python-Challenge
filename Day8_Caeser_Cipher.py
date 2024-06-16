alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cipher = 'yes'

while cipher == 'yes':
    cipher = input("Would you like to encode or decode a message using the Caeser Cipher? Type 'yes' or 'no'\n").lower()
    if cipher == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        
        def caesar(start_text, shift_value, direction_value):
            if direction_value == "encode":
                encrypted_word = ''
                for i in range(0, len(start_text)):
                    letter = start_text[i]
                    index = alphabet.index(letter)
                    new_index = index + shift_value
                    if new_index >= 26:
                        new_index = new_index-26
                    encrypted_word += alphabet[new_index]
                print(f"The ecnoded text is: {encrypted_word}")
            else:
                decrypted_word = ''
                for i in range(0, len(start_text)):
                    letter = start_text[i]
                    index = alphabet.index(letter)
                    new_index = index - shift_value
                    decrypted_word += alphabet[new_index]
                print(f"The decoded text is: {decrypted_word}")
                
        caesar(text, shift, direction)
    else:
        break
        
# def encrypt(text, shift):
#     #word = list(text)
#     encrypted_word = ''
#     for i in range(0, len(text)):
#         letter = text[i]
#         index = alphabet.index(letter)
#         new_index = index + shift
#         if new_index >= 26:
#             new_index = new_index-26
#         encrypted_word += alphabet[new_index]
#     print(f"The ecnoded text is: {encrypted_word}")
#     #return encrypted_word
    
# def decrypt(text, shift):
#     word = list(text)
#     decrypted_word = ''
#     for i in range(0, len(text)):
#         letter = text[i]
#         index = alphabet.index(letter)
#         new_index = index - shift
#         decrypted_word += alphabet[new_index]
#     print(f"The decoded text is: {decrypted_word}")


# if direction == "encode":
#   encrypt(text, shift)
# elif direction == "decode":
#   decrypt(text, shift)