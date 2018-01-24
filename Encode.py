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

class Encode:
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
        self.URL_dict = self.URL_dict_create()
        self.spoof_dict = dict()
        self.setup_spoof()
    #*************
    #Need to add a bigger library here!
    #Also need to be able to accept special characters here like NULL and others.
    def URL_dict_create(self):
        """
        Gets the character to URL-character encoder chart.
        Needs to be in the form char "URL encoding"
        i.e.: X %58
        Returns:
            URL_dict(dict): key: character(string)
                            value: Encoding(string)
        """
        URLS = open("Resources/UTF.txt","r")
        URL_dict = dict()
        URL_dict[" "] = "%20"
        URL_dict[""] = "%00"
        for line in URLS:
            string = line.split(' ')
            URL_dict[string[0]] = string[1]
        return URL_dict


    def change_URL(self, char):
        """
        Changes the character from a character to a URL-encoded character
        Returns:
            URL-char(string): the conversion of the character into the URL encoding.
        """
        return self.URL_dict[char]

    def URL_string_change(self, string):
        """
        Changes the whole string into a URL-encoded string
        Args:
            string(string): the string to be encoded
        Returns:
            encoded(string): a string full of the URL encoded characters.
        """
        encoded = ""
        for char in string:
            try:
                encoded +=self.URL_dict[char]
            except KeyError:
                print("Warning..." + char + " is " + " not in the URL encoder library. Skipped " + char + "...")
        return encoded.replace('\n','')

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
                encode = self.replace_char(encode,char,self.spoof_dict[char][-1])
        return encode

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
                if(len(sub) > char_num):
                    encode += sub[char_num-1]
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

    def test(self):
        """
        A test that should be ran before this is ever pushed back up!
        This runs through all of the URL possible characters of the normal alphabet.
        """

        string = "abcdefghijklmnopqrstuvwxyz"
        check_string = """%61%62%63%64%65%66%67%68%69%6A%6B%6C%6D%6E%6F%70%71%72%73%74%75%76%77%78%79%7A"""
        assert(self.URL_string_change(string) == check_string)
        string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        check_string = "%41%42%43%44%45%46%47%48%49%4A%4B%4C%4D%4E%4F%50%51%52%53%54%55%56%57%58%59%5A"
        assert(self.URL_string_change(string) == check_string)
        string = "0123456789"
        check_string = "%30%31%32%33%34%35%36%37%38%39"
        assert(self.URL_string_change(string) == check_string)
        print('Tests have passed!')

def main():
    E = Encode()
    t = E.spoof_encode_crazy("How was your day?")
    print t

    #good example!
    #scripts tend to be evaluated the same, but have a different encoding than added marks.
    #print ("ｂ".decode("utf-8") == "ｂ".decode("utf-8"))


main()
