def write_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def write_hex_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data.hex())

def read_hex_file(filename):
    with open(filename, 'r') as f:
        hex_data = f.read()
    return bytes.fromhex(hex_data)
