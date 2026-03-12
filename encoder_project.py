# Simple Encoder / Decoder (Caesar Cipher)

def encode(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decode(text, shift):
    return encode(text, -shift)

if __name__ == "__main__":
    message = input("Enter message: ")
    shift = int(input("Enter shift number: "))

    encoded = encode(message, shift)
    print("Encoded message:", encoded)

    decoded = decode(encoded, shift)
    print("Decoded message:", decoded)
