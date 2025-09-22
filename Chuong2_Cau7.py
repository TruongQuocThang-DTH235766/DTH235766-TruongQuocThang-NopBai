'''
1. Dùng input() để nhập dữ liệu chuỗi

Cách sử dụng: Hàm input() cho phép người dùng nhập dữ liệu từ bàn phím. Dữ liệu nhập vào luôn được coi là chuỗi (string), kể cả khi bạn nhập số.

Ví dụ:

name = input("Nhập tên của bạn: ")  # Dữ liệu nhập sẽ được gán vào biến name
print("Xin chào, " + name)


Lưu ý: Mặc dù người dùng có thể nhập số, nhưng giá trị trả về từ input() vẫn là chuỗi, nếu cần số, bạn phải chuyển đổi (ví dụ dùng int() hoặc float()).

2. Chuyển đổi dữ liệu nhập từ chuỗi sang kiểu dữ liệu khác

Nếu bạn muốn nhập số nguyên hoặc số thực từ bàn phím, bạn cần chuyển đổi kiểu dữ liệu từ chuỗi sang int hoặc float.

Ví dụ:

age = input("Nhập tuổi của bạn: ")
age = int(age)  # Chuyển chuỗi thành số nguyên
print("Tuổi của bạn là: ", age)


Hoặc sử dụng trực tiếp trong input():

age = int(input("Nhập tuổi của bạn: "))  # Nhập và chuyển đổi ngay


Ví dụ với số thực:

height = float(input("Nhập chiều cao của bạn (m): "))  # Nhập và chuyển thành số thực
print("Chiều cao của bạn là: ", height)

3. Nhập nhiều giá trị cùng một lúc

Nếu bạn muốn nhập nhiều giá trị trên cùng một dòng, có thể sử dụng input() kết hợp với hàm split() để tách các giá trị ra thành các phần tử trong một danh sách.

Ví dụ:

numbers = input("Nhập ba số cách nhau bởi dấu cách: ").split()
a, b, c = map(int, numbers)  # Chuyển từng phần tử thành kiểu int
print("Ba số bạn nhập là:", a, b, c)


Ở đây, input() lấy chuỗi, split() chia chuỗi thành danh sách các phần tử, và map(int, numbers) chuyển từng phần tử thành số nguyên.

4. Nhập dữ liệu với vòng lặp (cho trường hợp nhập liên tiếp)

Đôi khi bạn cần nhập nhiều giá trị một cách liên tục trong một vòng lặp, ví dụ như nhập nhiều số và dừng lại khi người dùng nhập một giá trị đặc biệt.

Ví dụ:

while True:
    number = input("Nhập một số (hoặc 'exit' để kết thúc): ")
    if number == "exit":
        break
    else:
        print(f"Số bạn nhập là: {number}")


Trong ví dụ này, khi người dùng nhập "exit", vòng lặp sẽ kết thúc.

5. Nhập số và xử lý lỗi (dùng try...except)

Khi người dùng nhập dữ liệu, có thể nhập sai kiểu (ví dụ nhập chữ thay vì số), bạn có thể xử lý lỗi bằng cách dùng try...except.

Ví dụ:

try:
    number = int(input("Nhập một số nguyên: "))
    print(f"Số bạn nhập là: {number}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")


Khi người dùng nhập không phải số nguyên, chương trình sẽ bắt lỗi và thông báo cho người dùng.
'''