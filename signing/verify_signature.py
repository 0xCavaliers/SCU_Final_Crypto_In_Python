import binascii
from gmssl import sm2, sm3, func
from utils import file_operations

def verify_signature(signature, data, public_key_file):
    with open(public_key_file, 'r') as f:
        public_key = f.read().strip()
    
    sm2_crypt = sm2.CryptSM2(public_key=public_key, private_key='')

    hash_value = file_operations.read_file("hash_value.txt")
    
    # 将签名转换为字节数组
    signature_bytes = binascii.unhexlify(signature)
    
    # 将哈希值转换为字节数组
    hash_value_bytes = bytes.fromhex(hash_value)
    
    result = sm2_crypt.verify(signature_bytes.hex(), hash_value_bytes)
    
    return True^result

