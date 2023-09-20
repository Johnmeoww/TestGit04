def original_character_to_encrypt(original):
    """Encrypts the original string using a substitution table."""
    substitution_choice = {
        'aa': 'A', 'ab': 'B', 'ac': 'C', 'ad': 'D',
        'ba': 'E', 'bb': 'F', 'bc': 'G', 'bd': 'H',
        'ca': 'I', 'cb': 'J', 'cc': 'K', 'cd': 'L',
        'da': 'M', 'db': 'N', 'dc': 'O', 'dd': 'P'
    }
    reduced = ''

    for i in range(0, len(original), 2):
        pair = original[i:i + 2]
        if pair in substitution_choice:
            reduced += substitution_choice[pair]

    return reduced


def decoded_character(reduced):
    """Decrypts the reduced string back to the original."""
    substitution_choice = {
        'A': 'aa', 'B': 'ab', 'C': 'ac', 'D': 'ad',
        'E': 'ba', 'F': 'bb', 'G': 'bc', 'H': 'bd',
        'I': 'ca', 'J': 'cb', 'K': 'cc', 'L': 'cd',
        'M': 'da', 'N': 'db', 'O': 'dc', 'P': 'dd'
    }
    original = ''

    for char in reduced:
        if char in substitution_choice:
            original += substitution_choice[char]

    return original


# Example usage:
def run():
    original_text = "abcbdbcbdbcadcbdcadcbdcadcbdacdbcdacdc"
    reduced_text = original_character_to_encrypt(original_text)
    converted_text = decoded_character(reduced_text)

    print("Original Answer:", original_text)
    print("Encrypted:", reduced_text)
    print("Decrypted Answer:", converted_text)


