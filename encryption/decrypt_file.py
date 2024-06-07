from gmssl import sm4

def decrypt_file(encrypted_data, key):
    sm4_cipher = sm4.CryptSM4()
    sm4_cipher.set_key(key, sm4.SM4_DECRYPT)
    
    iv = b'0000000000000000'  # 初始向量
    plaintext = sm4_cipher.crypt_cbc(iv, encrypted_data)
    
    # 去除PKCS7填充
    pad = plaintext[-1]
    plaintext = plaintext[:-pad]
    
    return plaintext
