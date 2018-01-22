

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

    #*************
    #Need to add a bigger library here!
    #Also need to be able to accept special characters here like NULL and others.d
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


    def change_URL(self,char):
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

def main():
    E = Encode()
    print E.URL_string_change("hackers unite8!")

main()
