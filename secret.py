import secrets

# 使用secrets模块的token_urlsafe()方法生成一个安全的URL安全的秘钥
secret_key = secrets.token_urlsafe(16)  # 参数16指的是生成的字节长度
print(secret_key)