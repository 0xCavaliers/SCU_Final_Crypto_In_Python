from gmssl import sm2

def sign_hash(hash_value, private_key_file):
    with open(private_key_file, 'r') as f:
        private_key = f.read().strip()
    sm2_crypt = sm2.CryptSM2(private_key=private_key, public_key='')
    hash_value_bytes = bytes.fromhex(hash_value)  # 将hash_value转换为字节串
    signature = sm2_crypt.sign(hash_value_bytes, '12345678')
    return signature
