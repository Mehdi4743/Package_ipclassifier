
def get_ip_class(ip: str) -> str:
  
    try:
        # Valider l'adresse IP et extraire le premier octet
        octets = ip.split(".")
        if len(octets) != 4 or not all(o.isdigit() for o in octets):
            return "Invalid IP"

        first_octet = int(octets[0])
        if first_octet < 0 or first_octet > 255:
            return "Invalid IP"

        # Identifier la classe de l'IP
        if 1 <= first_octet <= 126:
            return "Class A"
        elif 128 <= first_octet <= 191:
            return "Class B"
        elif 192 <= first_octet <= 223:
            return "Class C"
        elif 224 <= first_octet <= 239:
            return "Class D (Multicast)"
        elif 240 <= first_octet <= 255:
            return "Class E (Experimental)"
        else:
            return "Invalid IP"
    except Exception as e:
        return f"Error: {e}"
