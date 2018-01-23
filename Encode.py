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
        self.get_letter('A')
        """

        #uppercase letters
        for spot in range(ord('A'),ord('Z')+1):
            self.get_letter(chr(spot))

        #lowercase letters
        for spot in range(ord('a'),ord('z')+1):
            self.get_letter(chr(spot))
        """
        #special characters
        # * + \ [] {} ' " : ; , . / \ | < >


    def get_letter(self,letter):
        """
        For a given character, it imports all of the similar looking letters into a dictionary.s
        Args:
            letter(string): the reference string for a file to be the key for the dictionary.
        """

        URLS = open("Resources/"+letter +".txt","r")
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


    def spoof_encode(self,string):
        pass


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
    E.test()
    
main()
