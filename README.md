# 川大《应用密码学》课程综合实践：简易安全数据传输系统

<font color=red>**制作不易，如果能帮上你，可以的话花费你几秒钟的时间帮作者点上一颗闪亮的小心心，好人一生平安谢谢喵~**</font>

## 1. 环境配置（在Linux环境下运行）

### 1.1 配置pip指令

命令行键入：sudo apt-get install python-pip python3-pip

### 1.2 使用pip指令安装相关包

pip install gmssl

pip install ecdsa

*(如果项目报错其他包安装问题，没有包都可以使用pip install指令)*



## 2. 项目框架

simple_safe_data_transfer_system/
│
├── README.md
├── main.py 
│
├── encryption/
│   ├── __init__.py
│   ├── generate_key.py
│   ├── encrypt_file.py
│
├── hashing/
│   ├── __init__.py
│   ├── calculate_hash.py
│
├── signing/
│   ├── __init__.py
│   ├── sign_hash.py
│
└── utils/
    ├── __init__.py
    ├── file_operations.py

**README.md文件包括了安装依赖和运行教程，主函数main.py命令行公式为 python main.py ~ **



## 3. 项目运行顺序（以下均在终端键入）

### 3.1 生成5MB随机数据文件

python main.py generate_data

### 3.2 生成加密密钥

python main.py generate_key

### 3.3 加密文件（会运行一段时间，不会很快结束）

python main.py encrypt_file target_data.txt encrypted_data.txt encryption_key.txt

**生成encrypted_data.txt文件**

### 3.4 解密文件（会运行一段时间，不会很快结束）

python main.py decrypt_file encrypted_data.txt decrypted_data.txt encryption_key.txt

**生成decrypted_data.txt文件**

### 3.5 计算哈希值（会运行一段时间，不会很快结束）

python main.py calculate_hash target_data.txt

**生成hash_value.txt文件**

### 3.6 生成数字签名的公钥与私钥

python generate_sm2_keypair.py

**生成sm2_private_key.txt文件和sm2_public_key.txt文件**

### 3.7 签名哈希值

python main.py sign_hash hash_value.txt sm2_private_key.txt

**生成signature.txt文件**

### 3.8 验证签名

python main.py verify_signature signature.txt decrypted_data.txt sm2_public_key.txt

**正常情况都是输出True**

### 3.9 检查数据一致性

python main.py check_consistency target_data.txt decrypted_data.txt

**正常情况都是输出success**

<font color=red>**制作不易，如果能帮上你，可以的话花费你几秒钟的时间帮作者点上一颗闪亮的小心心，好人一生平安谢谢喵~**</font>
