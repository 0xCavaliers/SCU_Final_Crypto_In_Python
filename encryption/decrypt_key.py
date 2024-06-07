from gmssl import sm2

def decrypt_key(encrypted_key_file, private_key, output_file):
    sm2_crypt = sm2.CryptSM2(private_key=private_key, public_key=None)
    encrypted_key = read_file(encrypted_key_file)
    key = sm2_crypt.decrypt(encrypted_key)
    write_to_file(output_file, key)
