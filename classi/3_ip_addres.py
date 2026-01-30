class IPAdress():
    def __int__(self, ip, SubnetMusk ):
        #ip : una stringa
        # SubnetMusk è una stringa /24
        pass

    def networdAdress(self):
        #restitiusce l'indirizzo di rete 
        pass

    def broadcastAdress(self):
        #restitiusce lindirizzo broadcast
        pass
    
    def hostNumbr(self):
        #restitiusce il numero di host
        pass

    def main():
        pass
    
    if __name__ == "__main__":
     main()




class IPAddress():
    def __init__(self, ip, subnet):
        # ip: stringa come "192.168.1.1"
        # subnet: stringa come "/24" o "255.255.255.0"
        self.ip = ip
        self.ip_parts = [int(x) for x in ip.split('.')]
        
        if subnet.startswith('/'):
            # Formato CIDR come "/24"
            self.cidr = int(subnet[1:])
            # Calcola la subnet mask
            mask_num = 0xFFFFFFFF << (32 - self.cidr) & 0xFFFFFFFF
            self.mask = [
                (mask_num >> 24) & 255,
                (mask_num >> 16) & 255,
                (mask_num >> 8) & 255,
                mask_num & 255
            ]
        else:
            # Formato come "255.255.255.0"
            self.mask = [int(x) for x in subnet.split('.')]
            # Conta i bit 1 per avere il CIDR
            mask_bin = ''.join([bin(x)[2:].zfill(8) for x in self.mask])
            self.cidr = mask_bin.count('1')
    
    def network_address(self):
        """Calcola l'indirizzo di rete"""
        network = []
        for i in range(4):
            network.append(self.ip_parts[i] & self.mask[i])
        return ".".join([str(x) for x in network])
    
    def broadcast_address(self):
        """Calcola l'indirizzo broadcast"""
        network = [int(x) for x in self.network_address().split('.')]
        broadcast = []
        
        for i in range(4):
            # Wildcard = 255 - subnet mask
            wildcard = 255 - self.mask[i]
            broadcast.append(network[i] | wildcard)
        
        return ".".join([str(x) for x in broadcast])
    
    def host_number(self):
        """Calcola il numero di host disponibili"""
        # Formula: 2^(32 - cidr) - 2
        return (2 ** (32 - self.cidr)) - 2
    
    def __str__(self):
        """Rappresentazione leggibile"""
        return f"IP: {self.ip}\nRete: {self.network_address()}\nBroadcast: {self.broadcast_address()}\nHost: {self.host_number()}"


def main():
    # Test semplice
    print("=== ESEMPIO 1 ===")
    ip1 = IPAddress("192.168.1.100", "/24")
    print(ip1)
    
    print("\n=== ESEMPIO 2 ===")
    ip2 = IPAddress("192.168.1.100", "255.255.255.0")
    print(ip2)
    
    print("\n=== ESEMPIO 3 ===")
    ip3 = IPAddress("10.0.0.50", "/26")
    print(ip3)


if __name__ == "__main__":
    main()