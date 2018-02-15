import socket

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


if __name__ == '__main__':
    E = EncodeAddress()
    print "Decimal IP address for facebook.com: ",
    print E.convert_to_decimal("facebook.com")
