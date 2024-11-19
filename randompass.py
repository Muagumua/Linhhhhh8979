import random
import string

# In banner (giả sử bạn đã có banner)
banner = """
██████╗ ███████╗██╗  ██╗██╗████████╗ ██████╗ ██████╗ 
██╔══██╗██╔════╝██║  ██║██║╚══██╔══╝██╔══██╗██╔══██╗
██████╔╝█████╗  ███████║██║   ██║   ██████╔╝██████╔╝
██╔═══╝ ██╔══╝  ██╔══██║██║   ██║   ██╔══██╗██╔══██╗
██║     ███████╗██║  ██║██║   ██║   ██║  ██║██║  ██║
╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
"""
# In ra banner
for char in banner:
    print(char, end='', flush=True)
    
# Hàm random mật khẩu
def random_password(length, mode):
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    number_chars = string.digits
    symbol_chars = string.punctuation

    password = ''
    
    for _ in range(length):
        if mode == 1:
            password += random.choice(lowercase_chars)
        elif mode == 2:
            password += random.choice(uppercase_chars)
        elif mode == 3:
            password += random.choice(number_chars)
        elif mode == 4:
            password += random.choice(symbol_chars)
        elif mode == 5:
            random_mode = random.randint(1, 4)
            if random_mode == 1:
                password += random.choice(lowercase_chars)
            elif random_mode == 2:
                password += random.choice(uppercase_chars)
            elif random_mode == 3:
                password += random.choice(number_chars)
            elif random_mode == 4:
                password += random.choice(symbol_chars)
        else:
            return 'Vui Lòng Chọn Lại'

    return password

# Vòng lặp nhập dữ liệu
while True:
    print(f"\nNhập số lượng kí tự muốn random: ", end='')
    soluong = int(input())  # Nhập số lượng ký tự
    length = soluong
    print(f"\nNhập [1] để random chữ thường")
    print(f"Nhập [2] để random chữ hoa")
    print(f"Nhập [3] để random số")
    print(f"Nhập [4] để random kí tự đặc biệt")
    print(f"Nhập [5] để random tất cả")
    print(f"Mời lụa chọn: ", end='')
    chatluong = int(input())  # Chọn chế độ random

    print(f"Password là: {random_password(length, chatluong)}")