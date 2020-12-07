#!/usr/bin/python
import sys

def open_as_binary(filename, n_bytes=16):
    split_lines = [] 
    try:  
        with open(filename, 'rb') as f: 
            lines = b''.join(f.readlines())
            for i in range(0, len(lines), n_bytes):
                split_lines.append(lines[i:i+n_bytes])
    except FileNotFoundError:
        print("File Not Found")
    return split_lines

# encode bytes to hex
def encode_hex(byte_block):
    hex_ = []
    for x in byte_block:
        hex_.append(f"{x:02x}")
    hex_ = list(zip(hex_[::2], hex_[1::2]))
    bytes_to_hex = ""
    for x in hex_:
        bytes_to_hex += f"{x[0]}{x[1]} "
    return bytes_to_hex

# decode btye to string
def decode_bytes(data):
    str_from_hex = ""
    for x in data:
        if x > 31 and x < 127:
            str_from_hex += chr(x)
        else:
            str_from_hex += "."
    return str_from_hex


def xxd(lines: list):
    for index, line in enumerate(lines):
        print(f"{(index*16):08x} {encode_hex(line)} : {decode_bytes(line)}")


if __name__ == "__main__":
    try:
        filename = sys.argv[1] 
        lines = open_as_binary(filename)
        xxd(lines)
    except IndexError:
        print(f"[ERR] NO FILENAME SUPPLIED")