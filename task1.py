def check_name(name):
    
    if name != name.strip():
        return False
    
    emoji_ranges = [
        (0x1F600, 0x1F64F),  # Emoticons
        (0x1F300, 0x1F5FF),  # Miscellaneous Symbols and Pictographs
        (0x1F650, 0x1F67F),  # Ornamental Dingbats
        (0x1F680, 0x1F6FF),  # Transport and Map Symbols
        (0x1F700, 0x1F77F),  # Alchemical Symbols
        (0x1F780, 0x1F7FF),  # Geometric Shapes Extended
        (0x1F800, 0x1F8FF),  # Supplemental Arrows-C
        (0x1F900, 0x1F9FF),  # Supplemental Symbols and Pictographs
        (0x1FA00, 0x1FA6F),  # Chess Symbols
        (0x1FA70, 0x1FAFF),  # Symbols and Pictographs Extended-A
        (0x2500, 0x2BEF),   # Miscellaneous Symbols
        (0x2600, 0x26FF),   # Constellations and Weather Symbols
        (0x2700, 0x27BF),   # Decorative Symbols
        (0xFE00, 0xFE0F),   # Variation Selectors
        (0x1F000, 0x1F02F), # Mahjong Symbols
        (0x200D, 0x200D),   # Zero Width Joiner
    ]

    for char in name:
        code_point = ord(char)
        if any(start <= code_point <= end for start, end in emoji_ranges):
            return False

    
    if not name.isprintable():
        return False
    
    return True

        

def check_name_len(name):
    return len(name) <= 20

def check_sid_len(name):
    
    str_sid = str(name)
    return (
        len(str_sid) == 10
        and str_sid.isdigit()
        and str_sid.startswith('1155')
    )
