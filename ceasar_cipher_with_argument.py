import argparse


def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print(f'Decoded text: "{text}"')

info = "Reads file then decodes it via ceasar cipher."
parser = argparse.ArgumentParser(info)
parser.add_argument("-f", "--file", help="I need a file to decode!")
parser.add_argument("-r", "--rotation", default=-13, type=int,
                    help="Rotation can be either positive or negative number.")
args = parser.parse_args()
filename = args.file

if(args.file):
    with open(args.file) as f:
        encoded_text = f.read()
        decode_Caesar_cipher(encoded_text, args.rotation)
else:
    print("I need a file to decode!")
