class GiaoDich:
    def __init__(self, maGD, ngayGD, donGia, soLuong):
        self.maGD = maGD
        self.ngayGD = ngayGD
        self.donGia = donGia
        self.soLuong = soLuong
    def get_maGD(self):
        return self.maGD
    def get_ngayGD(self):
        return self.ngayGD
    def get_donGia(self):
        return self.donGia
    def get_soLuong(self):
        return self.soLuong
    def ThanhTien(self):
        pass
    def __str__(self):
        return f"Mã GD: {self.maGD}, Ngày GD: {self.ngayGD}, Đơn giá: {self.donGia}, Số lượng: {self.soLuong}"
class GiaoDichVang(GiaoDich):
    def __init__(self, maGD, ngayGD, donGia, soLuong, loaiVang):
        super().__init__(maGD, ngayGD, donGia, soLuong)
        self.loaiVang = loaiVang
    def get_loaiVang(self):
        return self.loaiVang
    def ThanhTien(self):
        return self.soLuong * self.donGia
    def __str__(self):
        return super().__str__() + f", Loại vàng: {self.loaiVang}, Thành tiền: {self.ThanhTien()}"
class GiaoDichTienTe(GiaoDich):
    def __init__(self, maGD, ngayGD, donGia, soLuong, loaiTien, loaiGD):
        super().__init__(maGD, ngayGD, donGia, soLuong)
        self.loaiTien = loaiTien
        self.loaiGD = loaiGD
    def get_loaiTien(self):
        return self.loaiTien
    def get_loaiGD(self):
        return self.loaiGD
    def ThanhTien(self):
        if self.loaiGD.lower() == "mua":
            return self.soLuong * self.donGia
        else:
            return (self.soLuong * self.donGia) * 1.05
    def __str__(self):
        return super().__str__() + f", Loại tiền: {self.loaiTien}, Loại GD: {self.loaiGD}, Thành tiền: {self.ThanhTien()}"
tong_TongTienVang = 0
tong_SoLuongTien = 0
tong_TongTienTienTe = 0
gdv = []
n = int(input("Nhap vao so luong giao dich vang: "))
for i in range(n):
    print(f"Nhap vao thong tin giao dich vang thu {i+1}: ")
    maGD = input("Ma GD: ")
    ngayGD = input("Ngay GD (dd/mm/yyyy): ")
    donGia = float(input("Don gia: "))
    soLuong = int(input("So luong: "))
    loaiVang = input("Loai vang (24K/18K/9999): ")
    gdv.append(GiaoDichVang(maGD, ngayGD, donGia, soLuong, loaiVang))
gdtt = []
m = int(input("Nhap vao so luong giao dich tien te: "))
for i in range(m):
    print(f"Nhap vao thong tin giao dich tien te thu {i+1}: ")
    maGD = input("Ma GD: ")
    ngayGD = input("Ngay GD (dd/mm/yyyy): ")
    donGia = float(input("Don gia: "))
    soLuong = int(input("So luong: "))
    loaiTien = input("Loai tien (USD/VND/EUR): ")
    loaiGD = input("Loai GD (mua/ban): ")
    gdtt.append(GiaoDichTienTe(maGD, ngayGD, donGia, soLuong, loaiTien, loaiGD))
gd = gdv + gdtt
print("Danh sach giao dich: ")
for giaoDich in gd:
    print(giaoDich)

tong_SoLuongVang = sum(gd.get_soLuong() for gd in gdv)
tong_TongTienVang = sum(gd.ThanhTien() for gd in gdv)

tong_SoLuongTien = sum(gd.get_soLuong() for gd in gdtt)
tong_TongTienTienTe = sum(gd.ThanhTien() for gd in gdtt)

print(f"Tong so luong vang: {tong_SoLuongVang}")
print(f"Tong tien vang: {tong_TongTienVang}")
print(f"Tong so luong tien te: {tong_SoLuongTien}")
print(f"Tong tien tien te: {tong_TongTienTienTe}")