import uuid

def get_mac_address():
    """Restituisce l'indirizzo MAC della scheda di rete principale"""
    mac = uuid.getnode()
    mac_address = ':'.join(['{:02x}'.format((mac >> elements) & 0xff) 
                           for elements in range(0, 8*6, 8)][::-1])
    return mac_address

# Esempio di utilizzo
if __name__ == "__main__":
    mac = get_mac_address()
    print(f"Indirizzo MAC: {mac}")
    

