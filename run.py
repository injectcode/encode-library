# -*- coding: utf-8 -*-
import sys

from EncodeText import EncodeText
from EncodeURL import EncodeURL
from EncodeAddress import EncodeAddress

class interface:
    def __init__(self):
        self.Text = EncodeText()
        self.URL = EncodeURL()
        self.Address = EncodeAddress()
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
        ex: python run.py "hacktheplanet<script>" -T -p
        displays-- hacktheplanet﹤script﹥
        text: the text being evaluated
        mode: the mode being used
        flags: parameters for the use
    The parameters have to go in this order. The additional
        flags are for altering the string, are referenced below.
        Order does matter for which way the flags are used.

    Modes supported:
    -U: URL encodings --defaults to Puncutation
    -T: ASCII to unicode trickery--defaults to puncutation
    -A: Address encoding --defaults to decimal
    -B: base encoding(under construction)

    Flags to use:
    -p: Puncutation(u,t)
    -c char: A single character(u,t)
    -k: Craziness; does the craziness thing possible(u,t)
    -s: Script mode for all characters(t)
    -a: Ticks on top of the characters(t)
    -1 char spot: Replaces the 'char' with in the 'spot'(t)
    -2 spot: Replaces the character with the URL encode(u)
    -o: octal mode for the ip address
    -d: decimal mode for the ip address
    -bi: binary mode for the ip address
        """
        return help_list

    def parse_input(self):
        """
        Parses all of the user inputs and flags.
        Note: Whichever command is used first, will be the character changed.
        """
        begin_text = self.encoded_text
        err = False
        # sample: python run.py 'hello world;' -t -p
        spot = 1
        while spot < len(self.args):

            arg = self.args[spot]

            if(arg == '-A'):
                self.setting = 2
            #url mode
            # '-u'
            elif(arg == '-U'):
                self.setting = 1
            # by default, text
            # '-t'
            elif(arg == '-T'):
                self.setting = 0

            #puncutation
            #'-p'
            elif(arg == '-p'):
                if(self.setting == 0):
                    self.encoded_text = self.Text.spoof_punc(self.encoded_text,0)
                elif(self.setting == 1):
                    self.encoded_text = self.URL.URL_spoof_punc(self.encoded_text)
                else:
                    print "Not supported for this mode"
            #for a single character
            # '-c char'
            elif(arg == '-c'):
                try:
                    #need to throw other errors here for not enough characters...
                    if(self.setting == 0):
                        self.encoded_text = self.Text.spoof_char(self.encoded_text,self.args[spot+1])
                        spot+=1
                    elif(self.setting == 1):
                        self.encoded_text = self.URL.URL_spoof_char(self.encoded_text, self.args[spot+1])
                        spot+=1
                    elif(self.setting == 2):
                        convert_t = 0
                        if(self.args[spot+1] == '-tt'):
                            convert_t = self.args[spot+2]
                            spot +=2

                        self.encoded_text = self.Address.convert_offset(self.encoded_text,self.args[spot+1], self.args[spot+2],self.args[spot+3],self.args[spot+4],ohb = convert_t)
                        spot+=4
                except IndexError:
                    print "Not enough values for the parameter... Do this right!"
                    err = True
            #just going wild!
            # '-k'
            elif(arg == '-k'):
                if(self.setting == 0):
                    self.encoded_text = self.Text.spoof_encode_crazy(self.encoded_text)
                elif(self.setting == 1):
                    self.encoded_text = self.URL.URL_spoof_all(self.encoded_text)
                elif(self.setting == 2):
                    self.encoded_text = self.Address.convert_offset(self.encoded_text,0,0,1,1)
                else:
                    print "Not supported for this mode"

            #a full script text look. Works on google!
            # '-s'
            elif(arg == '-s'):
                if(self.setting == 0):
                    self.encoded_text = self.Text.spoof_encode_script(self.encoded_text)
                elif(self.setting == 1):
                    print "Not supported for this mode"
            #ticks on top and bottom of the characters.
            # '-a'
            elif(arg == '-a'):
                if(self.setting == 0):
                    self.encoded_text = self.Text.spoof_encode_ticks(self.encoded_text)
                elif(self.setting == 1):
                    print "Not supported for this mode"
                else:
                    print "Not supported for this mode"

            # '-1 char spot'
            elif(arg == '-1'):
                if(self.setting == 0):
                    self.encoded_text = self.Text.change_spot(self.encoded_text,self.args[spot +1], self.args[spot+2])
                elif(self.setting == 1):
                    print "No setting for this yet..."
                else:
                    print "Not supported for this mode"
            # '-2 spot '
            elif(arg == '-2'):
                if(self.setting == 0):
                    print "Not supported for this mode"
                elif(self.setting == 1):
                    self.encoded_text = self.URL.URL_spoof_spot(self.encoded_text,self.args[spot+1])
            elif(arg == '-o'):
                if(self.setting == 0 or self.setting== 1):
                    print "Not supported for this mode"
                elif(self.setting == 2):
                    self.encoded_text = self.Address.convert_to_octal(self.encoded_text)
            elif(arg == '-d'):
                if(self.setting == 0 or self.setting== 1):
                    print "Not supported for this mode"
                elif(self.setting == 2):
                    self.encoded_text = self.Address.convert_to_decimal(self.encoded_text)
            elif(arg == '-bi'):
                if(self.setting == 0 or self.setting== 1):
                    print "Not supported for this mode"
                elif(self.setting == 2):
                    self.encoded_text = self.Address.convert_to_binary(self.encoded_text)
            elif(arg == '-dd'):
                self.encoded_text = self.URL.double_encode(self.encoded_text)
            else:
                print "Not a valid flag-- Continue"

            spot+=1

        if(self.encoded_text == begin_text and err == False):
            if(self.setting == 0):
                self.encoded_text = self.Text.spoof_punc(self.encoded_text,0)
            elif(self.setting == 1):
                self.encoded_text = self.URL.URL_spoof_punc(self.encoded_text)
            elif(self.setting == 2):
                self.encoded_text = self.Address.convert_to_decimal(self.encoded_text)
            else:
                pass

        return self.encoded_text

if __name__ == '__main__':
    I = interface()
    text = I.parse_input()
    print text
