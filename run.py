import sys
"""
Tags:
    -u: URL Mode
    -s: spoof Mode
    -p: puncutation
    -i: enables interactive interface
    -c letter: obfusicate it using this character
    -a: obfusicate the whole string
"""

from EncodeText import EncodeText
from EncodeURL import EncodeURL
class interface:
    def __init__(self):
        self.Text = EncodeText()
        self.URL = EncodeURL()
        self.args = list()
        self.encoded_text = ""
        self.setup_args()
        self.setting = 0




    def setup_args(self):
        """
        Sets all of the command line arguements into a list.
        """

        lst = list()
        for arg in sys.argv:
            self.args.append(arg)
        self.encoded_text = self.args[1]
        self.args = self.args[1:]

    def parse_input(self):
        """
        Parses all of the user inputs and flags.
        Note: Whichever command is used first, will be the character changed.
        """

        for spot in range(len(self.args)):
            arg = self.args[spot]
            print arg

            #url mode
            # '-u'
            if(arg == '-u'):
                self.setting = 1
            # by default, text
            # '-t'
            elif(arg == '-t'):
                self.setting = 0

            #puncutation
            #'-p'
            elif(arg == '-p'):
                if(self.setting == 0):
                    self.encoded_text = self.Text.spoof_punc(self.encoded_text,0)
                elif(self.setting == 1):
                    self.encoded_text = self.URL.URL_spoof_punc(self.encoded_text)
            #for a single character
            # '-c char'
            elif(arg == '-c'):
                if(self.setting == 0):
                    self.encoded_text = self.Text.spoof_char(self.encoded_text,self.args[spot+1])
                elif(self.setting == 1):
                    self.encoded_text = self.URL.URL_spoof_char(self.encoded_text, self.args[spot+1])
            #just going wild!
            # '-k'
            elif(arg == '-k'):
                if(self.setting == 0):
                    self.encoded_text = self.Text.spoof_encode_crazy(self.encoded_text)
                elif(self.setting == 1):
                    self.encoded_text = self.URL.URL_spoof_all(self.encoded_text)
            #a full script text look. Works on google!
            # '-s'
            elif(arg == '-s'):
                if(self.setting == 0):
                    self.encoded_text = self.Text.spoof_encode_script(self.encoded_text)
                elif(self.setting == 1):
                    print "No setting for this yet..."
            #ticks on top and bottom of the characters.
            # '-a'
            elif(arg == '-a'):
                if(self.setting == 0):
                    self.encoded_text = self.Text.spoof_encode_ticks(self.encoded_text)
                elif(self.setting == 1):
                    print "No setting for this yet..."
            # '-1 char spot'
            elif(arg == '-1'):
                if(self.setting == 0):
                    self.encoded_text = self.Text.change_spot(self.encoded_text,self.args[spot +1], self.args[spot+2])
                elif(self.setting == 1):
                    print "No setting for this yet..."
            # '-2 spot '
            elif(arg == '-2'):
                if(self.setting == 0):
                    print "No setting for this yet..."
                elif(self.setting == 1):
                    self.encoded_text = self.URL.URL_spoof_spot(self.encoded_text,self.args[spot+1])

        return self.encoded_text

if __name__ == '__main__':
    I = interface()
    text = I.parse_input()
    print text
