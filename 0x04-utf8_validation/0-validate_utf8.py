#!/usr/bin/python3
"""
Determines if a given data is a valid UTF-8
"""

def validUTF8(data):
    """
    valid UTF-8 encoding
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    
    # Masks to check the most significant bits
    # Mask for 1 byte: 0xxxxxxx (0x80 = 10000000, 0x00 = 00000000)
    mask1 = 0x80
    # Mask for 2 bytes: 110xxxxx (0xE0 = 11100000)
    mask2 = 0xE0
    # Mask for 3 bytes: 1110xxxx (0xF0 = 11110000)
    mask3 = 0xF0
    # Mask for 4 bytes: 11110xxx (0xF8 = 11111000)
    mask4 = 0xF8
    # Mask for continuation bytes: 10xxxxxx (0xC0 = 11000000)
    mask_cont = 0xC0
    # Continuation byte should be 10xxxxxx
    mask_cont_value = 0x80

    for byte in data:
        if num_bytes == 0:
            if byte & mask1 == 0:
                continue
            elif byte & mask2 == 0xC0:
                num_bytes = 1
            elif byte & mask3 == 0xE0:
                num_bytes = 2
            elif byte & mask4 == 0xF0:
                num_bytes = 3
            else:
                return False
        else:
            if byte & mask_cont != mask_cont_value:
                return False
            num_bytes -= 1
    return num_bytes == 0