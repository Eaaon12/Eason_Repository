from Crypto.Cipher import AES

# 設置 AES 加密相關參數
blocksize = 16
plaintext = 'apple'  # 原始明文
key = b"jerry313jerry313"  
iv = b"jerry313jerry313"   

print(f"原始明文: {plaintext}")

# 將明文填充至 16 字節，使用 '\0' 進行填充
paddingdata = plaintext.ljust(blocksize, '\0')
print(f"填充後的明文: {paddingdata}")

# 加密過程
Cipher = AES.new(key, AES.MODE_CBC, iv)
a = Cipher.encrypt(paddingdata.encode('utf-8'))
hexdata = a.hex()  # 將加密結果轉為十六進制表示
print(f"加密後的密文 (Hex): {hexdata}")

# 解密過程
Cipherdecrypt = AES.new(key, AES.MODE_CBC, iv)
d = bytes.fromhex(hexdata)  # 將十六進制密文轉回 bytes
c = Cipherdecrypt.decrypt(d)

# 去除填充的 '\0' 並解碼成 UTF-8 字符串
e = c.rstrip(b'\0').decode('utf-8')
print(e)
