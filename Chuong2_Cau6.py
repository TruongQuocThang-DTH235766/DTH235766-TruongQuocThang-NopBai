'''
1. Toán tử chia (/)

Ý nghĩa: Toán tử / dùng để thực hiện phép chia giữa hai số, kết quả trả về là một số thực (floating-point).

Ví dụ:

x = 10 / 3  # Kết quả là 3.3333333333333335

2. Toán tử chia lấy phần nguyên (//)

Ý nghĩa: Toán tử // thực hiện phép chia và lấy phần nguyên (làm tròn xuống) của kết quả, tức là phần nguyên của phép chia.

Ví dụ:

x = 10 // 3  # Kết quả là 3 (lấy phần nguyên)

3. Toán tử lấy phần dư (%)

Ý nghĩa: Toán tử % được sử dụng để tìm phần dư của phép chia. Kết quả trả về là phần dư của phép chia giữa hai số.

Ví dụ:

x = 10 % 3  # Kết quả là 1 (phần dư khi chia 10 cho 3)

4. Toán tử lũy thừa (**)

Ý nghĩa: Toán tử ** thực hiện phép tính lũy thừa, nghĩa là "mũ" trong toán học. Nếu a ** b, thì kết quả là 
a^b

Ví dụ:

x = 2 ** 3  # Kết quả là 8 (2 mũ 3)

5. Toán tử and

Ý nghĩa: Toán tử and là toán tử logic, trả về True chỉ khi cả hai điều kiện đều đúng (True). Nếu một trong hai điều kiện sai (False), kết quả sẽ là False.

Ví dụ:

x = True and False  # Kết quả là False
y = True and True   # Kết quả là True

6. Toán tử or

Ý nghĩa: Toán tử or là toán tử logic, trả về True nếu ít nhất một trong các điều kiện là đúng (True). Nếu cả hai điều kiện đều sai, kết quả mới là False.

Ví dụ:

x = True or False  # Kết quả là True
y = False or False # Kết quả là False

7. Toán tử is

Ý nghĩa: Toán tử is kiểm tra sự tương đồng giữa hai đối tượng trong Python. Nó sẽ trả về True nếu hai đối tượng có cùng vị trí trong bộ nhớ (tức là chúng là một đối tượng duy nhất), ngược lại sẽ trả về False.

Ví dụ:

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is b)  # Kết quả là False, vì a và b là hai đối tượng khác nhau
print(a is c)  # Kết quả là True, vì a và c là cùng một đối tượng


Tóm lại:

/ là chia bình thường, trả về số thực.

// là chia lấy phần nguyên, trả về số nguyên.

% là lấy phần dư.

** là tính lũy thừa.

and, or là các toán tử logic.

is dùng để kiểm tra xem hai đối tượng có phải là một hay không.
'''