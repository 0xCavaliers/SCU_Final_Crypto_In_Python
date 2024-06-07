from gmssl import sm4

def encrypt_file(input_file, key):
    sm4_cipher = sm4.CryptSM4()
    sm4_cipher.set_key(key, sm4.SM4_ENCRYPT)
    
    with open(input_file, 'r') as f:
        plaintext = f.read().encode('utf-8')
    
    # 添加PKCS7填充
    pad = 16 - len(plaintext) % 16
    plaintext += bytes([pad] * pad)
    
    iv = b'0000000000000000'  # 初始向量，可以根据需要更改
    ciphertext = sm4_cipher.crypt_cbc(iv, plaintext)
    
    return ciphertext
