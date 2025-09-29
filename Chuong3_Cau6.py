def doc_so(n):
    hang_chuc = ["", "Mười", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
    hang_don_vi = ["", "mốt", "hai", "ba", "bốn", "lăm", "sáu", "bảy", "tám", "chín"]
    
    if n < 0 or n > 99:
        return "Số không hợp lệ. Vui lòng nhập số từ 0 đến 99."
    
    if n == 0:
        return "Không"
    if n < 10:
        return ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"][n]

    a = n // 10
    b = n % 10
    
    if a == 1:
        if b == 0:
            return "Mười"
        elif b == 5:
            return "Mười lăm"
        else:
            return "Mười " + ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"][b]
    else:
        result = hang_chuc[a] + " mươi"
        if b == 0:
            return result
        elif b == 1:
            return result + " mốt"
        elif b == 5:
            return result + " lăm"
        else:
            return result + " " + hang_don_vi[b]
try:
    n = int(input("Nhập một số nguyên từ 0 đến 99: "))
    print("Cách đọc:", doc_so(n))
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")

