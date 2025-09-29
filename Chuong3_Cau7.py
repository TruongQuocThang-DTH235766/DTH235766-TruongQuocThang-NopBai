import datetime

def nhap_ngay():
    try:
        ngay = int(input("Nhập ngày: "))
        thang = int(input("Nhập tháng: "))
        nam = int(input("Nhập năm: "))
        date = datetime.date(nam, thang, ngay)
        ngay_ke_tiep = date + datetime.timedelta(days=1)
        print("Ngày kế tiếp là: {}/{}/{}".format(
            ngay_ke_tiep.day, ngay_ke_tiep.month, ngay_ke_tiep.year
        ))
    except ValueError:
        print("Ngày không hợp lệ. Vui lòng nhập đúng định dạng và giá trị ngày hợp lý.")
nhap_ngay()