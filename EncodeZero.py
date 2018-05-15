
"""
All create goes to this man here! He's done a great job here!:
https://medium.com/@umpox/be-careful-what-you-copy-invisibly-inserting-usernames-into-text-with-zero-width-characters-18b4e6f17b66
"""
class EncodeZero:

    def __init__(self):
        self.space = u"\u200B"
        self.joiner = u"\u200C"

    """
    Adds a zero-width space every other character
    Args:
        text(string): plaintext
        returned(string): the plaintext with added zero-width characters.
    """
    def every_other(self,text):
        # adds the character every other spec
        returned = ""
        for i in range(0, len(text)):
            if(i % 2 == 1):
                returned += text[i] + self.space
            else:
                returned += text[i]
        return returned


    """
    Encrypts the given text into a zero width text.
    Args:
        text(string): the text to be encrypted.
    Returns:
        text(string): the zero-width encrypted data.
    """
    def encrypt(self,text):
        text = [self.pad_zeros((bin(ord(char)))[2:]) for char in text]
        return self.binary_to_zero_width(text)

    """
    Pads 0's until a complete ASCII character can be made out.
    Args:
        text(string): the binary representation of a character.
    Returns:
        text(string): the binary representated character, with the 0's padded.
    """
    def pad_zeros(self,text):
        while(len(text) != 8):
            text = '0' + text
        return text

    """
    Converts the the binary text into a zero-width encrypted text.
    1's turn into a zero-width space.
    0's turn into a zero-width joiner.
    Args:
        text(list): a list of binary represented characters.
    Returns:
        user(string): a zero width encoded string.
    """
    def binary_to_zero_width(self,text):
        user = ""
        for char in text:
            for bit in char:
                if(int(bit) == 1):
                    user += self.space
                else:
                    user += self.joiner
        return user

    """
    Decrypted the zero-width encoded text.
    Args:
        text(string): the text with the hidden info.
    Returns:
        text(string): the decrypted message.
    """
    def decrypt(self,text):
        return self.zero_width_to_text(text)

    """
    Converts the zero width text encoded string and gets the hidden text.
    Args:
        text(string): the text to find the hidden text in.
    Returns:
        plain_txt(string): the decrypted string's content.
    """
    def zero_width_to_text(self,text):
        plain_txt = ""
        total_zero = ""
        for char in text:
            if char == self.space:
                total_zero += '1'
            elif char == self.joiner:
                total_zero += '0'

            if(len(total_zero) == 8):
                plain_txt += chr(int(total_zero,2))
                total_zero = ""
        return plain_txt

    """
    Displays encrypted text. It displays the zero width space as a `
    and the zero width joiner as a |.
    """
    def show(self,text):
        new_text = ""
        for char in text:
            if char == self.space:
                new_text += "`"
            elif(char == self.joiner):
                new_text += '|'
            else:
                new_text += char
        return new_text
        
if __name__ == '__main__':
    E = EncodeZero()
    print "Examples: This uses ` and | to show the zero width characters..."
    print "Encrypt max ", E.show(E.encrypt("max"))
    print "Decrypt the text containing the encrypted string: ", E.decrypt(E.encrypt("max") + "more text!")
