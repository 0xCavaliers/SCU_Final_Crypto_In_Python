from gmssl import sm3, func

def calculate_hash(input_file):
    with open(input_file, 'r') as f:
        data = f.read().encode('utf-8')
    
    hash_value = sm3.sm3_hash(func.bytes_to_list(data))
    return ''.join(hash_value)
