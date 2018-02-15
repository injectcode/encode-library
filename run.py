# -*- coding: utf-8 -*-
import sys

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
        if len(sys.argv) <=1 or sys.argv[1] == '-h' or sys.argv[1] == '-H':
            print self.help_text()
            return 0
        lst = list()
        for arg in sys.argv:
            self.args.append(arg)
        self.encoded_text = self.args[1]
        self.args = self.args[1:]

    def help_text(self):
        """
        Returns:
            help(string): the instructional to the page.
        """
        help_list ="""
    Welcome to the Encoder!
    The last place you'll ever
    have to go in order to alter your text!

    Functionality:
    python run.py "text" -mode -flags
        ex: python run.py "hacktheplanet<script>" -t -p
        displays-- hacktheplanet﹤script﹥
        text: the text being evaluated
        mode: the mode being used
        flags: parameters for the use
    The parameters have to go in this order. The additional
        flags are for altering the string, are referenced below.
        Order does matter for which way the flags are used.

    Modes supported:
    -u: URL encodings
    -t: ASCII to unicode trickery
    -b: base encoding(under construction)

    Flags to use:
    -p: Puncutation(u,t)
    -c char: A single character(u,t)
    -k: Craziness; does the craziness thing possible(u,t)
    -s: Script mode for all characters(t)
    -a: Ticks on top of the characters(t)
    -1 char spot: Replaces the 'char' with in the 'spot'(t)
    -2 spot: Replaces the character with the URL encode(u)
        """
        return help_list

    def parse_input(self):
        """
        Parses all of the user inputs and flags.
        Note: Whichever command is used first, will be the character changed.
        """
        # sample: python run.py 'hello world;' -t -p
        for spot in range(len(self.args)):
            arg = self.args[spot]

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
