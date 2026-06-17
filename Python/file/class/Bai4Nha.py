class GiaoDich:
    def __init__(self, maGD, ngay, dongia, soluong):
        self.maGD = maGD
        self.ngay = ngay
        self.dongia = dongia
        self.soluong = soluong
    def get_maGD(self):
        return self.maGD
    def get_ngay(self):
        return self.ngay
    def get_dongia(self):
        return self.dongia
    def get_soluong(self):
        return self.soluong
    def thanh_tien(self):
        return 0
    def __str__(self):
        return f"Ma GD: {self.maGD}, Ngay: {self.ngay}, Đon giá: {self.dongia}, SL: {self.soluong}"

class GiaoDichVang(GiaoDich):
    def __init__(self, maGD, ngay, dongia, soluong, loaiVang):
        super().__init__(maGD, ngay, dongia, soluong)
        self.loaiVang = loaiVang
    def get_loaiVang(self):
        return self.loaiVang
    def thanh_tien(self):
        return self.soluong * self.dongia

    def __str__(self):
        return super().__str__() + f", Loai vang: {self.loaiVang}, Thanh tien: {self.thanh_tien()}"

class GiaoDichTienTe(GiaoDich):
    def __init__(self, maGD, ngay, tygia, soluong, loaiTien, loaiGD):
        super().__init__(maGD, ngay, tygia, soluong)
        self.loaiTien = loaiTien
        self.loaiGD = loaiGD
    def get_loaiTien(self):
        return self.loaiTien
    def get_loaiGD(self):
        return self.loaiGD
    def thanh_tien(self):
        if self.loaiGD.lower() == "mua":
            return self.soluong * self.dongia
        elif self.loaiGD.lower() == "ban":
            return (self.soluong * self.dongia) * 1.05
        else:
            return 0

    def __str__(self):
        return super().__str__() + f", Loai tiền: {self.loaiTien}, Giao dich: {self.loaiGD}, Thanh tien: {self.thanh_tien()}"
ds_gdv = []
n = int(input("Nhap vao so luong giao dich: "))
for i in range(n):
  print("Nhap vao giao dich: ")
  maGD = input("Nhap vao ma giao dich: ")
  ngay = input("Nhap vao ngay: ")
  dongia = float(input("Nhap vao don gia: "))
  soluong = int(input("Nhap vao so luong: "))
  loaiVang = input("Nhap vao loai vang(18k, 24k, 9999): ")
  ds_gdv.append(GiaoDichVang(maGD, ngay, dongia, soluong, loaiVang))
ds_gdtt = []
m = int(input("Nhap vao so luong giao dich: "))
for i in range(n):
  print("Nhap vao giao dich: ")
  maGD = input("Nhap vao ma giao dich: ")
  ngay = input("Nhap vao ngay: ")
  tygia = float(input("Nhap vao ty gia: "))
  soluong = int(input("Nhap vao so luong: "))
  loaiTien = input("Nhap vao loai tien(USD, EUR, AUD): ")
  loaiGD = input("Nhap vao loai giao dich(mua/ban): ")
  ds_gdtt.append(GiaoDichTienTe(maGD, ngay, tygia, soluong, loaiTien, loaiGD))
ds_gd = ds_gdv + ds_gdtt
print("Danh sach giao dich:")
for gd in ds_gd:
    print(gd)
tong_sl_vang = 0

for gd in ds_gd:
    if isinstance(gd, GiaoDichVang):
        tong_sl_vang += gd.soluong
tong_tt_vang = 0

for gd in ds_gd:
  if isinstance(gd, GiaoDichVang):
    tong_tt_vang += gd.thanh_tien()

tong_sl_tiente = 0

for gd in ds_gd:
    if isinstance(gd, GiaoDichTienTe):
        tong_sl_tiente += gd.soluong

tong_tt_tiente = 0

for gd in ds_gd:
    if isinstance(gd, GiaoDichTienTe):
        tong_tt_tiente += gd.thanh_tien()

print(f"Tong SL vang     : {tong_sl_vang}")
print(f"Tong thanh tien vang : {tong_tt_vang}")
print(f"Tong SL tien te  : {tong_sl_tiente}")
print(f"Tong thanh tien tien te: {tong_tt_tiente}")