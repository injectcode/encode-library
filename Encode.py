#Maxwell Dulin
#ILY!

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
        URLS = open("UTF.txt","r")
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
        print("Successful!")
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
            self.spoof_dict[category] = [char]
        else:
            array = self.spoof_dict[category]
            array.append(char)
            self.spoof_dict[category] = array
        print self.spoof_dict

    def setup_spoof(self):
        """
        Sets up the character swaps for every normal character.
        """
        pass

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

    def spoof_encode(self,string):
        pass

def main():
    E = Encode()
    print u'\u00B2'.encode("utf-8")
main()
