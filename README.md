# Obfuscating Strings, IP addresses and URL's
## EncodeText -T(default)
Changing a string into different encodings.  
Changes characters from their regular ASCII encoding to unicode. This has a ton of ways to obfuscate it!   
hacktheplanet<script> could turn into `hacktheplanet﹤script﹥` or `𝖍ǎ𝕔𝔨ţ𝖍ȩ𝖕ℓǎ𝖓ȩţ`  
 
## EncodeURL -U
Changes a the contents of the text into a URL encoding, with different settings of course.     
Good for attempting to bypass filters for URL's. Instead of manually changing the URL with the codes, this automagically does it for you.  
By changing all y's to URL encode 'how's your day' turns into `how's %79our da%79`   
Also supports double encoding of URL's.  

## EncodeAddress -A
Changes the DNS or ip address given to the decimal format. <b> Firefox and Chrome </b> accept a format of IP address as a group of 4 octets or in decimal, octal or mixed So, This format could be good for bypassing filters. 
Google.com(74.125.135.139)in different forms:  
Decimal: http://1249740645   
Octal:  http://0112.0175.0207.0161  
Binary: http://01001010.01111101.10000111.10001011  
Mix-up: Octal for 1,2 and normal octets for 3,4  
https://0112.0175.135.102  

Note: Binary does not work on Chrome and Firefox, haven't checked any other browsers. But, sometimes the mix-up throws insecure ip address errors. 

## How to use:
1. Download this repository with `git clone https://github.com/mdulin2/encode-library`  
2. In the same directory, run `cd ./encode-library`  
3. Run the python script! This is shown below.

The general format is below:
```
python run.py "mystring" -type_wanted -settings
```
<br/>

mystring is the string that the user wants to alter.  
typewanted: currently -T for text, -U for urls and -A for IP addresses.   
-settings: these are all the different flags that can be used. All of the flags are below:  
A real example: `python run.py "hacktheplanet<script>" -T -p` will run the text obfuscater on all punctuation on hacktheplanet<script>.   This results in `hacktheplanet﹤script﹥`  
 
 ## Flags
 Below are the flags supported for the functionality.    
 First, the flag is shown with any needed parameters: -c char  
 Second, a description of the flag.  
 Third, where it can be used. u for URL, T for text mode and A for IP address mode.  
```
    Modes supported:  
    -U: URL encodings --defaults to punctuation
    -T: ASCII to unicode trickery--defaults to punctuation 
    -A: Address encoding --defaults to decimal  
    -B: base encoding(under construction)  

    Flags to use:  
    -p: punctuation(u,t)  
    -c char: A single character(u,t)  
    -c -tt # # # #: the mixing of the IP address type. 0 for octal, 1 for normal octets(a)
    -k: Craziness; does the craziness thing possible(u,t)  
    -s: Script mode for all characters(t)  
    -a: Ticks on top of the characters(t)  
    -1 char spot: Replaces the 'char' with in the 'spot'(t)  
    -2 spot: Replaces the character with the URL encode(u)  
    -dd: double encode a url(u)
    -o: octal mode for the ip address(a)
    -d: decimal mode for the ip address(a) 
    -bi: binary mode for the ip address(a)

```

It should be noted that the flags are done in the order that they are thrown into. For instance, if a punctuation, with the -p flag, is encoded, then it will only be encoded this one time. So, if a -k flag, for encoding all, is used, then nothing else will happen to the other characters.   

## Closing Thoughts:
Let me know what you think about it, if you find a bug or want to help out on it! I'd love to add some other features to this.   
I plan on packaging this to be installed with pip in the future, but we'll see.   
`Email: mdulin2@zagmail.gonzaga.edu `
