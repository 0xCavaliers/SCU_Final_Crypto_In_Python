from gmssl import sm2, func
from ecdsa import SigningKey, NIST256p

def generate_sm2_keypair():
    private_key = func.random_hex(64)  # 生成64个字符的16进制私钥
    sk = SigningKey.from_string(bytes.fromhex(private_key), curve=NIST256p)
    public_key = sk.verifying_key.to_string().hex().upper()
    return private_key, '04' + public_key  # '04' 表示未压缩格式

private_key, public_key = generate_sm2_keypair()

print("Private Key:", private_key)
print("Public Key:", public_key)

# 保存密钥到文件
with open('sm2_private_key.txt', 'w') as f:
    f.write(private_key)

with open('sm2_public_key.txt', 'w') as f:
    f.write(public_key)
