# Obfusicating Strings, IP addresses and URL's
## EncodeText -T(default)
Changing a string into different encodings.  
Changes characters from their regular ASCII encoding to unicode. This has a ton of ways to obfusicate it!  

## EncodeURL -U
Changes a the contents of the text into a URL encoding, with different settings of course.   
Good for attempting to bypass filters for URL's. Instead of manually changing the URL with the codes, this automagically does it for you.

## EncodeAddress -A
Changes the DNS or ip address given to the decimal format. <b> Firefox and Chrome </b> accept a format of IP address as a group of 4 octets or in decimal, octal or mixed So, This format could be good for bypassing filters. 

## How to use:

The general format is below:
```
python run.py "mystring" -type_wanted -settings
```

 
mystring is the string that the user wants to alter.  
typewanted: currently -T for text, -U for urls and -A for IP addresses.  
-settings: these are all the different flags that can be used. All of the flags are below:
A real example: `python run.py "hacktheplanet<script>" -T -p` will run the text obfusicator on all puncuatoin on hacktheplanet<script>. This results in `hacktheplanet﹤script﹥` 
```
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
    -dd: double encode a url  
```

It should be noted that the flags are done in the order that they are thrown into. For instance, if a punctuation, with the -p flag, is encoded, then it will only be encoded this one time. So, if a -k flag, for encoding all, is used, then nothing else will happen to the other characters.
