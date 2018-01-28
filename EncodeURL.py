class EncodeURL:

    def __init__(self):
        """
        Intializer
        """
        self.URL_dict = self.URL_dict_create()

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

    def URL_spoof_all(self, string):
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

    def URL_spoof_punc(self,string):
        """
        Changes all puncutation into a URL code
        Args:
            string: the string to be altered.
        Returns:
            a string with all puncutation altered with a URL code.
        """

        encoded = ""
        for char in string:
            if(char.isdigit() == False and char.isalpha() == False):
                try:
                    encoded +=self.URL_dict[char]
                except KeyError:
                    print("Warning..." + char + " is " + " not in the URL encoder library. Skipped " + char + "...")
            else:
                encoded += char
        return encoded.replace('\n','')

    def URL_spoof_spot(self,string,spot):
        """
        Changes one character into a URL string
        Args:
            string: the string being altered
            spot(int): the spot, starting from 1, on the string to be changed.
        Returns:
            a string with a single new URL encoding.
        """

        encoded = ""
        iteration = 1
        for char in string:
            if(int(spot) == iteration):
                try:
                    encoded +=self.URL_dict[char]
                except KeyError:
                    encoded += char
                    print("Warning..." + char + " is " + " not in the URL encoder library. Skipped " + char + "...")
            else:
                encoded += char
            iteration+=1
        return encoded.replace('\n','')

    def URL_spoof_char(self,string,change):
        """

        """
        encoded = ""
        iteration = 1
        for char in string:
            if(char == change ):
                try:
                    encoded +=self.URL_dict[char]
                except KeyError:
                    encoded += char
                    print("Warning..." + char + " is " + " not in the URL encoder library. Skipped " + char + "...")
            else:
                encoded += char
            iteration+=1
        return encoded.replace('\n','')
if __name__ == '__main__':

    U = EncodeURL()
    print U.URL_spoof_all("how's your day?")
    print U.URL_spoof_punc("how's your day?")
    print U.URL_spoof_spot("how's your day?",1)
    print U.URL_spoof_char("how's your day?","y")
