import sys
from encryption.generate_key import generate_random_key
from encryption.encrypt_file import encrypt_file
from encryption.decrypt_file import decrypt_file
from encryption.decrypt_key import decrypt_key
from hashing.calculate_hash import calculate_hash
from signing.sign_hash import sign_hash
from signing.verify_signature import verify_signature
from utils.file_operations import write_to_file, read_file, write_hex_to_file, read_hex_file
from validation.check_consistency import check_consistency
import os
import random
import string

def generate_random_data(size_in_mb, output_file):
    size_in_bytes = size_in_mb * 1024 * 1024
    with open(output_file, 'w') as f:
        while f.tell() < size_in_bytes:
            f.write(''.join(random.choices(string.ascii_letters + string.digits, k=1024)))
            f.write('\n')

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [options]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'generate_key':
        key = generate_random_key()
        write_hex_to_file('encryption_key.txt', key)
    
    elif command == 'generate_data':
        generate_random_data(5, 'target_data.txt')
    
    elif command == 'encrypt_file':
        if len(sys.argv) != 5:
            print("Usage: python main.py encrypt_file <input_file> <output_file> <key_file>")
            sys.exit(1)
        input_file = sys.argv[2]
        output_file = sys.argv[3]
        key_file = sys.argv[4]
        key = read_hex_file(key_file)
        encrypted_data = encrypt_file(input_file, key)
        write_hex_to_file(output_file, encrypted_data)
    
    elif command == 'decrypt_file':
        if len(sys.argv) != 5:
            print("Usage: python main.py decrypt_file <encrypted_file> <output_file> <key_file>")
            sys.exit(1)
        encrypted_file = sys.argv[2]
        output_file = sys.argv[3]
        key_file = sys.argv[4]
        key = read_hex_file(key_file)
        encrypted_data = read_hex_file(encrypted_file)
        decrypted_data = decrypt_file(encrypted_data, key)
        write_to_file(output_file, decrypted_data.decode('utf-8'))
    
    elif command == 'calculate_hash':
        if len(sys.argv) != 3:
            print("Usage: python main.py calculate_hash <input_file>")
            sys.exit(1)
        input_file = sys.argv[2]
        hash_value = calculate_hash(input_file)
        write_to_file('hash_value.txt', hash_value)
    
    elif command == 'sign_hash':
        if len(sys.argv) != 4:
            print("Usage: python main.py sign_hash <hash_file> <private_key_file>")
            sys.exit(1)
        hash_file = sys.argv[2]
        private_key_file = sys.argv[3]
        hash_value = read_file(hash_file).strip()  # 确保 hash_value 内容没有多余的空白字符
        signature = sign_hash(hash_value, private_key_file)
        write_to_file('signature.txt', signature)
    
    elif command == 'verify_signature':
        if len(sys.argv) != 5:
            print("Usage: python main.py verify_signature <signature_file> <data_file> <public_key_file>")
            sys.exit(1)
        signature_file = sys.argv[2]
        data_file = sys.argv[3]
        public_key_file = sys.argv[4]
        signature = read_file(signature_file).strip()  # 确保 signature 内容没有多余的空白字符
        data = read_file(data_file).encode('utf-8')
        result = verify_signature(signature, data, public_key_file)
        print(result)
    
    elif command == 'check_consistency':
        if len(sys.argv) != 4:
            print("Usage: python main.py check_consistency <file1> <file2>")
            sys.exit(1)
        file1 = sys.argv[2]
        file2 = sys.argv[3]
        result = check_consistency(file1, file2)
        print(result)
    
    else:
        print("Unknown command")
        sys.exit(1)

if __name__ == "__main__":
    main()
