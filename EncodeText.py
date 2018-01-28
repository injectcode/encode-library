# -*- coding: utf-8 -*-

#Maxwell Dulin
#ILY!
# http://www.utf8-chartable.de/unicode-utf8-table.pl?utf8=dec



"""
Modes for the spoofer:
The normal mode:
    This will use pretty normal characters, but different enough.
Crazy mode:
    This will use obscure characters to confuse the data reader.

different modes for different types?
1 for scripts, tricks google
2 for added characters
3 for craziness?
#scripts tend to work
better in google, rather than accent marks and other things.
Tags:
    -u: URL Mode
    -s: spoof Mode
    -p: puncutation
    -i: enables interactive interface
    -c letter: obfusicate it using this character
    -a: obfusicate the whole string
"""

class EncodeText:
    """
    Used to encode a string of text, from the choosen user, into a specified type.
    Changes specified character into a "look-a-like" of it.
    Includes:
    URL encoding:
        ASCII
    Base 64:
    Base N:
    """

    def __init__(self):
        """
        Intializer
        """
        self.spoof_dict = dict()
        self.setup_spoof()

    def convert_to_base_64(self, string):
        pass

    def convert_to_base_62(self,string):
        pass

    def convert_to_base_32(self, string):
        pass


    def insert_obs(self, category, char):
        """
        Inserts a single instance into the dictionary
        Args:
            category(string): is a single character used to describe a basic ASCII code
            char(string): is a single character, which will likely be un unicode, that represents
                a look-alike of the category.
        """

        if category not in self.spoof_dict:
            self.spoof_dict[category] = [char.encode("utf-8")]
        else:
            array = self.spoof_dict[category]
            array.append(char.encode("utf-8"))
            self.spoof_dict[category] = array

    def setup_spoof(self):
        """
        Sets up the character swaps for every normal character.
        """

        file_dict = self.setup_file_dict()
        for char in file_dict:
            self.get_letter(char,file_dict[char])

    def setup_file_dict(self):
        """
        Gets the file names to be used for the spoof_dict
        Returns
            file_call_dict(dictionary): key-char value-file_name
        """

        RLS = open("punc.txt","r")
        file_call_dict = dict()

        #numbers and puncutation
        for line in RLS:
            character = line.split(" ")
            file_call_dict[character[0]] = character[1].strip("\n")

        #uppercase letters
        for spot in range(ord('A'),ord('Z')+1):
            character = chr(spot)
            file_call_dict[character] = character
        #lowercase
        for spot in range(ord('a'),ord('z')+1):
            character = chr(spot)
            file_call_dict[character] = character

        return file_call_dict

    def get_letter(self,letter,file_name):
        """
        For a given character, it imports all of the similar looking letters into a dictionary.s
        Args:
            letter(string): the reference string for a file to be the key for the dictionary.
        """

        URLS = open("Resources/"+file_name+".txt","r")
        #need an exception list here for puncutation and integers
        for line in URLS:
            if(line != " " and line != '\n'):
                self.insert_obs(letter,line.strip('\n').decode("utf-8"))


    def replace_char(self, text, char, replace):
        """
        Changes the character in the string into the the obfusicated version of it.
        Args:
            text(string): the characters being acted on.
            char(string): the individual character to be changed.
            replace(string): the individual characer that is being swapped for the orginal one.
        Returns:
            alter(string): the obfusicated string.
        """
        return text.replace(char,replace)

    def change_spot(self, string, character, char_num):
        """
        Changes a particular character based on a spot in the file.
        Args:
            string(string): the text being altered.
            character(string): the character to be changed.
            char_num(int): the character to be used(starting with 1)
        Returns:
            encode(string): the altered string.
        """
        encode = ""
        for char in string:
            if(char == character):
                sub = self.spoof_dict[character]
                if(len(sub) > int(char_num)):
                    encode += sub[int(char_num)-1]
                else:
                    print("Character number doesn't not exist...\nAdded last item.")
                    encode+= sub[-1]
            else:
                encode += char
        return encode

    def is_legal(self,char):
        """
        The dictionary doesn't want to evaluate certain charaters.
        Args:
            char(string): the character being evaluated
        Returns:
            true: if the string is valid
            false: if the string is not valid
        """

        if(char != ' ' and char != '\t' and char != '\n'):
            return True
        return False

    def spoof_encode_crazy(self, string):
        """
        Adds the craziest version of each character to the version of the number.
        Args:
            string(string): the string to be encoded
        Returns:
            encode(string): the encoded string
        """
        encode = string
        for char in string:
            if(self.is_legal(char)):
                try:
                    encode = self.replace_char(encode,char,self.spoof_dict[char][-1])
                except Exception, e:
                    pass
        return encode

    def spoof_encode_script(self,string):
        """
        Adds the script meaning of a string. Works on google as a test
        Args:
            string(string): the string to be encoded
        Returns:
            encode(string): the encoded string
        """
        encode = string
        for char in string:
            if(self.is_legal(char)and char.isalpha()):
                try:
                    encode = self.replace_char(encode,char,self.spoof_dict[char][0])
                except Exception, e:
                    pass

        return encode

    def spoof_encode_ticks(self,string):
        """
        Adds all the letters with a single tick or addition to the string.
        Args:
            string(string): the string to be encoded
        Returns:
            encode(string): the encoded string
        """
        encode = string
        for char in string:
            if(self.is_legal(char) and char.isalpha()):
                try:
                    encode = self.replace_char(encode,char,self.spoof_dict[char][1])
                except Exception, e:
                    pass

        return encode

    def spoof_punc(self,string,spot):
        encode = string
        for char in string:
            if(self.is_legal(char) and (char.isalpha() == False and char.isdigit()==False)):
                try:
                    encode = self.replace_char(encode,char,self.spoof_dict[char][spot])
                except Exception, e:
                    pass

        return encode

    def spoof_char(self,string,char):
        """
        """
        return self.replace_char(string,char,self.spoof_dict[char][0])

if __name__ == '__main__':
    E = EncodeText()
    #E.get_letter('s','s')
    t = E.spoof_encode_script("How was your day?")
    print t
    t = E.spoof_encode_ticks("How was your day?")
    print t
    t = E.spoof_encode_crazy("How was your day?")
    print t
    print E.spoof_punc("OR 1=1",0)


    #good example!
    #scripts tend to be evaluated the same, but have a different encoding than added marks.
    print ("ｂ".decode("utf-8") == "b".decode("utf-8"))
