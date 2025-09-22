'''
I. Các loại lỗi
1. Lỗi cú pháp (Syntax Errors)

- Ý nghĩa: Lỗi cú pháp xảy ra khi viết mã không đúng cú pháp của Python, khiến Python không thể hiểu được mã. Đây là loại lỗi thường gặp nhất khi chưa tuân thủ đúng quy tắc về cấu trúc của chương trình.

2. Lỗi runtime (Runtime Errors)

Ý nghĩa: Lỗi runtime xảy ra khi chương trình đang chạy và gặp vấn đề trong quá trình thực thi, ví dụ như chia cho 0, truy cập phần tử ngoài phạm vi danh sách, hoặc khi không thể tìm thấy một biến.

Ví dụ:

x = 10 / 0  # Lỗi chia cho 0

Các loại lỗi runtime phổ biến:

ZeroDivisionError: Khi chia cho 0.

IndexError: Khi truy cập phần tử ngoài phạm vi danh sách.

ValueError: Khi thao tác với kiểu dữ liệu không hợp lệ.

TypeError: Khi thực hiện các phép toán không phù hợp với kiểu dữ liệu.

Cách khắc phục: Kiểm tra các điều kiện và dữ liệu trước khi thực hiện phép toán hoặc thao tác.

try:
    x = 10 / 0  # Kiểm tra lỗi chia cho 0
except ZeroDivisionError:
    print("Không thể chia cho 0.")

3. Lỗi logic (Logical Errors)

Ý nghĩa: Lỗi logic xảy ra khi mã chương trình không tạo ra kết quả như mong đợi, nhưng không có lỗi cú pháp hay runtime. Đây là lỗi do sai sót trong logic của chương trình, khiến kết quả cuối cùng sai hoặc không như mong muốn.

Ví dụ:

def add(a, b):
    return a - b  # Lỗi logic, phải là phép cộng chứ không phải phép trừ

print(add(2, 3))  # Kết quả sai

II. Cách bắt lỗi trong Python (Exception Handling)

Để xử lý lỗi trong Python, bạn có thể sử dụng cơ chế try...except, giúp chương trình tiếp tục chạy thay vì dừng lại khi gặp lỗi.

1. Câu lệnh try...except cơ bản

Cách sử dụng: Đặt đoạn mã có thể gây lỗi trong khối try, nếu xảy ra lỗi, Python sẽ chuyển tới khối except để xử lý lỗi đó.

Ví dụ:

try:
    x = 10 / 0  # Sẽ gây lỗi ZeroDivisionError
except ZeroDivisionError:
    print("Không thể chia cho 0.")  # Xử lý lỗi chia cho 0

2. Xử lý nhiều loại lỗi với nhiều except

Bạn có thể bắt nhiều loại lỗi khác nhau bằng cách sử dụng nhiều khối except. Mỗi khối except sẽ xử lý một loại lỗi cụ thể.

Ví dụ:

try:
    x = int(input("Nhập một số: "))  # Cố gắng chuyển đổi chuỗi thành số
    y = 10 / x  # Cố gắng chia cho số nhập vào
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
except ZeroDivisionError:
    print("Không thể chia cho 0.")

3. Dùng else để xử lý khi không có lỗi

Khối else chỉ được thực thi nếu không có lỗi xảy ra trong khối try.

Ví dụ:

try:
    x = int(input("Nhập một số: "))
    print("Bạn đã nhập số:", x)
except ValueError:
    print("Lỗi: Vui lòng nhập một số.")
else:
    print("Không có lỗi xảy ra.")

4. Dùng finally để thực hiện mã bất kể có lỗi hay không

Khối finally sẽ được thực thi dù có lỗi hay không, thích hợp để dọn dẹp tài nguyên như đóng file, kết nối mạng, v.v.

Ví dụ:

try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("Không tìm thấy file.")
finally:
    file.close()  # Đảm bảo đóng file dù có lỗi hay không

5. Tạo lỗi tùy chỉnh với raise

Bạn có thể tạo ra lỗi tùy chỉnh bằng cách sử dụng raise. Điều này cho phép bạn tạo ra các thông báo lỗi khi điều kiện nhất định không được thỏa mãn.

Ví dụ:

def check_positive_number(x):
    if x < 0:
        raise ValueError("Giá trị phải là số dương.")
    return x

try:
    check_positive_number(-5)
except ValueError as e:
    print(e)

'''