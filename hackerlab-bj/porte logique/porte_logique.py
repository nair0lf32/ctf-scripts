"""Brute-force de la clé d'un chiffrement simple"""
from itertools import product

# Les binaires donnés dans l'énoncé
binary_input = """
01101001 01101011 01101100 01010100 01010101 01010100 11010111 11110000 11100001
01010101 11110111 11100010 01111001 01010111 01110110 11010100 11100010 11111110
01010101 01110111 11100010 01010111 11111100 11111100 11010100 11010111 11110011
""".strip().split()

# Conversion binaire → entier
C_BYTES = [int(b, 2) for b in binary_input]


def rol(val, r_bits):
    """Rotate left on 8 bits"""
    return ((val << r_bits) & 0xFF) | (val >> (8 - r_bits))


def ror(val, r_bits):
    """Rotate right on 8 bits"""
    return ((val >> r_bits) | (val << (8 - r_bits))) & 0xFF


def decrypt_byte(c, key1, key2, key3, key4):
    """Déchiffre un octet avec les clés key1, key2, key3, key4"""
    tmp1 = c ^ key3 ^ key4
    tmp2 = ror(tmp1, 2)
    tmp3 = tmp2 ^ key2
    tmp4 = rol(tmp3, 3)
    return tmp4 ^ key1


# Bruteforce toutes les combinaisons possibles de clés sur 1 octet
for k1, k2, k3, k4 in product(range(256), repeat=4):
    try:
        M_BYTES = [decrypt_byte(c, k1, k2, k3, k4) for c in C_BYTES]
        M_STR = ''.join(chr(b) for b in M_BYTES)

        if "HLB2025{" in M_STR:
            print(f"Clés trouvées : K1={k1}, K2={k2}, K3={k3}, K4={k4}")
            print(f"Message : {M_STR}")
            break
    except ValueError:
        continue
