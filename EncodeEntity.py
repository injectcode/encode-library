class EncodeEntity:
    def __init__(self):
        """
        Intializer
        """
        self.spoof_dict = dict()
        self.setup_file_dict()

    def setup_file_dict(self):
        """
        Gets the file names to be used for the spoof_dict
        Returns
            file_call_dict(dictionary): key-char value-file_name
        """

        RLS = open("entity.txt","r")
        RLS_string = ""
        for line in RLS:
            if(line[0] != '#'):
                RLS_string+= line
        RLS = RLS_string.split("\n")
        RLS = RLS[:-1]

        #add the nbsc
        self.spoof_dict[" "] = ["&#nbsp"]
        self.spoof_dict["\n"] = ["&#10"]
        self.spoof_dict["\t"] = ["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        #adds the nontradionals
        for elt in RLS:
            new_set = elt.split(" ")
            self.spoof_dict[new_set[0]] = [new_set[1]]

        #adds regular characters
        for i in range(32,127):
            char = chr(i)
            encoding = '&#' + str(i)
            if(char in self.spoof_dict):
                self.spoof_dict[char].append(encoding)
            else:
                self.spoof_dict[char] = [encoding]

    def spoof_all(self,string, trust = True):
        """
        Spoofs every single character
        Args:
            string(str): the string being obfusicated
        Returns:
            the obfusicated string
        """
        spot = 0
        encode = string
        for char in string:
            try:
                if(len(self.spoof_dict[char])>1 and trust == True):
                    encode = self.replace_char(encode,char,self.spoof_dict[char][1])
                else:
                    encode = self.replace_char(encode,char,self.spoof_dict[char][0])
            except Exception, e:
                encode+=char
        return encode

    def spoof_punc(self,string,spot):
        """
        Encodes all non-alphanumberic characters
        Args:
            string(str): the string being obfusicated
            spot(int): Placeholder, will also be 1.
        Returns:
            The obfusicated string
        """
        encode = string
        for char in string:
            if((char.isalpha() == False and char.isdigit()==False)):
                try:
                    encode = self.replace_char(encode,char,self.spoof_dict[char][spot])
                except Exception, e:

                    encode+=char

        return encode

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

if __name__ == '__main__':
    EE = EncodeEntity()
    print EE.spoof_punc("Max<     ",0)
