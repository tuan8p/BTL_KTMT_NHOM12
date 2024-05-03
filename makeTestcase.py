import random
import struct
import os

def generate_float():
    shift = random.uniform(-100, 100)  # Generate a random float number in range -100 to 100
    return struct.pack('f', shift)  # Convert the number to a 32-bit binary format

# Tạo các file test case
with open('FLOAT15.BIN', 'wb') as f:  # Mở tệp ở chế độ ghi nhị phân 'wb'
    for _ in range(15):
        binary_float = generate_float()
        f.write(binary_float)  # Write the binary float to the file

# Kiểm tra xem file có được ghi thành công hay không
if os.path.exists('FLOAT15.BIN'):
    print("File 'FLOAT15.BIN' was created successfully.")
else:
    print("Failed to create the file 'FLOAT15.BIN'.")

    
# Mở file .bin ở chế độ đọc nhị phân
with open('FLOAT15.BIN', 'rb') as f:
    while True:
        # Đọc 4 byte từ file
        data = f.read(4)
        if not data:
            break  # Thoát khỏi vòng lặp nếu không còn dữ liệu

        # Chuyển đổi 4 byte nhị phân thành số thực
        number = struct.unpack('f', data)[0]

        # In số thực với 2 chữ số sau dấu phẩy thập phân
        print(format(number))