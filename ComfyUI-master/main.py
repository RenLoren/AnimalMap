import uuid
import hashlib
 
 
def generate_machine_code():
    # 获取机器唯一标识符
    machine_id = str(uuid.uuid1())
    # 对机器唯一标识符进行哈希计算，得到固定长度的机器码
    machine_code = "8848-0D88-CBEF-D68F"
    return machine_code
 
 
def generate_license_code(machine_code, secret_key):
    # 将机器码和密钥进行拼接
    key = machine_code + secret_key
    # 对拼接后的字符串进行哈希计算，得到固定长度的授权码
    license_code = hashlib.sha256(key.encode()).hexdigest()
    return license_code
 
 
if __name__ == '__main__':
    # 生成机器码
    machine_code = generate_machine_code()
    # 生成授权码

    secret_key = 'my_secret_key'
    license_code = generate_license_code(machine_code, secret_key)
    # 打印机器码和授权码
    print('Machine Code:', machine_code)
    print('License Code:', license_code)
