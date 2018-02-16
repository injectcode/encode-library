import socket

#Maxwell Dulin
#ILY!

class EncodeAddress:
    """
    The goal of this file to is encode a URL with the decimal
    conversion of it.
    Given a Domain name or an IP address
    """

    def calc_decimal(self,DNS):
        """
        Converts the DNS into a decimal IP address
        Args:
            DNS: The ip address(x.x.x.x) in hex or the domain name
        Returns:
            decimal_ip(int): the decimal value of the ip address
        """
        #parses the input
        DNS = self.fix_address(DNS)
        #gets the IP of the domain_name, if it's a domain name
        ip = self.get_ip(DNS)

        #converts to decimal
        ip = ip.split(".")
        decimal_ip = 0
        iteration = 3
        for spot in ip:
            decimal_ip = decimal_ip + int(spot)*(256**iteration)
            iteration-=1

        return decimal_ip

    def calc_hex(self,domain_name):
        """
        Converts the domain name into an hexidecimal ip address
        Args:
            domain_name(string): the DNS or ip address to be converted
        Returns:
            address(string): the hexidecimal IP address
        """
        DNS = self.fix_address(domain_name)
        ip = self.get_ip(DNS)
        return ip

    #inspiration
    #https://superuser.com/questions/75930/open-websites-using-binary-ip-address
    def calc_octal(self,domain_name):
        """
        Converts the domain name into an octal ip address
        Args:
            domain_name(string): the DNS or ip address to be converted
        Returns:
            address(string): the octal IP address
        """

        #parses the input
        DNS = self.fix_address(domain_name)
        #gets the IP of the domain_name, if it's a domain name
        ip = self.get_ip(DNS)
        ip = ip.split(".")
        ip_list = list()
        for spot in ip:
            ip_list.append(str((oct(int(spot)).zfill(4))))

        ip_address = ""
        for bi in ip_list:
            ip_address += bi
            ip_address+="."
        return ip_address[:-1]

    def calc_binary(self,domain_name):
        """
        Converts the domain name into a binary ip address
        Args:
            domain_name(string): the DNS or ip address to be converted
        Returns:
            address(string): the binary IP address
        """

        #parses the input
        DNS = self.fix_address(domain_name)
        #gets the IP of the domain_name, if it's a domain name
        ip = self.get_ip(DNS)
        ip = ip.split(".")
        ip_list = list()
        for spot in ip:
            ip_list.append(str((bin(int(spot))[2:].zfill(8))))

        ip_address = ""
        for bi in ip_list:
            ip_address += bi
            ip_address+="."

        return ip_address[:-1]

    def fix_address(self,domain_name):
        """
        Strips out all http and https parameters
        Args:
            domain_name(string): the ip address or domain name
        Retuns:
            dm(string): a parsed version of the ip/domain name
        """

        dm = domain_name.replace("https://","")
        dm = dm.replace("http://","")
        return dm

    def convert_to_decimal(self,domain_name):
        """
        Converts a domain name or ip address to the decimal format
        Args:
            domain_name(string): the domain name or ip to convert
        Returns:
            address(string): the decimal converted IP address
        """
        return "http://" + str(self.calc_decimal(domain_name))

    def convert_to_octal(self,domain_name):
        """
        Converts a domain name or ip address to the octal format
        Args:
            domain_name(string): the domain name or ip to convert
        Returns:
            address(string): the decimal converted IP address
        """
        return "http://" + str(self.calc_octal(domain_name))

    #Note***:
    #Doesn't work on most browsers
    def convert_to_binary(self,domain_name):
        """
        Converts a domain name or ip address to the binary format
        Args:
            domain_name(string): the domain name or ip to convert
        Returns:
            address(string): the decimal converted IP address
        """
        return "http://" + str(self.calc_binary(domain_name))

    def get_ip(self, domain_name):
        """
        Gets the IP address of the domain name
        Args:
            domain_name(string): the name of the DNS server
        Returns:
            address(string): the IP address associated with the domain_name
        """

        try:
            #works for both domain names and ip addresses
            return socket.gethostbyname(domain_name)
        except:
            print "Either no connection or invalid DNS"
            return -1


    def grab_ip_section(self,ip1,ip2,spots):
        """
        Changes the ivp4 address into a combination of octal and hexidecimal
        Args:
            ip1(string): ip address
            ip2(string): ip address
            spots(list): a 4 spot list with 1's and 0's
        Returns:
            text(string): Returns the new ip address
        """

        text = ""
        ip1 = ip1.split('.')
        ip2 = ip2.split('.')
        for i in range(len(spots)):
            if spots[i] == 0:
                text+=ip1[i]
                text+="."
            else:
                text+=ip2[i]
                text+="."

        return text[:-1]

    def convert_offset(self,domain_name,spot1,spot2,spot3,spot4, ohb = 1):
        """
        Converts the ip address to a hex and octal combination
        Args:
            domain_name(string): the domain of the ip address
            spot1-4(int): represent a spot on the ipv4 call
            ohb(int): 1 for octal and hex, 2 for octal and binary, 3 for binary and hex
        Returns:
            An ip address
        """

        #sets up the mode
        if(ohb ==1):
            ip1 = self.calc_octal(domain_name)
            ip2= self.calc_hex(domain_name)
        elif(ohb == 2):
            ip1 = self.calc_octal(domain_name)
            ip2= self.calc_binary(domain_name)
        elif(ohb == 3):
            ip1 = self.calc_binary(domain_name)
            ip2 = self.calc_hex(domain_name)
        else:
            return -1

        #sets up the change in ip
        set_up = list()
        set_up.append(spot1)
        set_up.append(spot2)
        set_up.append(spot3)
        set_up.append(spot4)

        #gets the new ip address
        text = self.grab_ip_section(ip1,ip2,set_up)
        return text

if __name__ == '__main__':
    E = EncodeAddress()
    print "Addresses for google.com: "
    print "Decimal: ",E.convert_to_decimal("google.com")
    print "Octal: ", E.convert_to_octal("google.com")
    print "Binary: ", E.convert_to_binary("google.com")
    print "Mix up--Octal for octet 1,2. Hex for octet 3,4"
    print E.convert_offset("google.com",0,0,1,1)
