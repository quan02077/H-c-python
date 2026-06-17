import random
import json

class DSHocSinh:
  def __init__(self, ten, tuoi, gioi_tinh, lop, diem):
    self.ten = ten
    self.tuoi = tuoi
    self.gioi_tinh = gioi_tinh
    self.lop = lop
    self.diem = diem
  def in_ds(self):
    return {
        "Ten": self.ten,
        "Tuoi": self.tuoi,
        "Gioi tinh": self.gioi_tinh,
        "Lop hoc": self.lop,
        "Diem": self.diem
        }
def DS_Hoc_Sinh_random():
  try:
    n = int(input("Nhap vao so luong hoc sinh:"))
  except ValueError:
    print("Vui nhap mot so nguyen!")
    return None
  Ten = ["Van Quan", "Minh Quan", "Hao Nhien", "Dai Phong", "Peter Griffin", "Glenn Quagmire", "Brian", "Joe", "Stewie", "Lois", "Meg", "Chris", "Patrick Bateman", "Cleverland"]
  Gioi_tinh = ["Nam", "Nu"]
  Lop = ["A", "B", "C", "D"]
  DS = []
  for i in range(n):
    ten = random.choice(Ten)
    tuoi = random.randint(18, 25)
    gioi_tinh = random.choice(Gioi_tinh)
    lop = random.choice(Lop)
    diem = random.randint(0, 10)
    DS.append(DSHocSinh(ten, tuoi, gioi_tinh, lop, diem))
  return DS
def _add_Hoc_Sinh_Moi(ds):
  ten = input("Nhap vao ten hoc sinh: ")
  tuoi = int(input("Nhap vao tuoi hoc sinh: "))
  gioi_tinh = input("Nhap vao gioi tinh hoc sinh: ")
  lop = input("Nhap vao lop hoc sinh: ")
  diem = int(input("Nhap vao diem hoc sinh: "))
  ds.append(DSHocSinh(ten, tuoi, gioi_tinh, lop, diem))
  print("Them thanh cong hoc sinh!")
def xem_danh_sach(ds):
  for i in range(len(ds)):
    print(f"{i + 1}. {ds[i].in_ds()}")
def _tim_kiem_Hoc_Sinh(ds, ten_can_tim):
  for hs in ds:
    if hs.ten.lower() == ten_can_tim.lower():
      return hs
  return None
def _cap_nhat(ds):
  ten_can_cap_nhat = input("Nhap vao ten hoc sinh can cap nhat: ")
  hs = _tim_kiem_Hoc_Sinh(ds, ten_can_cap_nhat)
  if hs:
    print("Nhap thong tin moi")
    ten_moi = input("Nhap ten moi: ")
    tuoi_moi = int(input("Nhap tuoi moi: "))
    gioi_tinh_moi = input("Nhap gioi tinh moi: ")
    lop_moi = input("Nhap lop moi: ")
    diem_moi = int(input("Nhap diem moi: "))
    if ten_moi: hs.ten = ten_moi
    if tuoi_moi: hs.tuoi = tuoi_moi
    if gioi_tinh_moi: hs.gioi_tinh = gioi_tinh_moi
    if lop_moi: hs.lop = lop_moi
    if diem_moi: hs.diem = diem_moi
    print("Cap nhat thanh cong!")
  else:
    print("Khong tim thay hoc sinh!")
def _xoa_hs(ds):
  ten_can_xoa = input("Nhap vao ten hoc sinh can xoa: ")
  hs = _tim_kiem_Hoc_Sinh(ds, ten_can_xoa)
  if hs:
    ds.remove(hs)
    print("Xoa thanh cong!")
  else:
    print("Khong tim thay hoc sinh!")

ds = DS_Hoc_Sinh_random()
print("Danh sach hoc sinh")
xem_danh_sach(ds)

_add_Hoc_Sinh_Moi(ds)
print("Danh sach hoc sinh")
xem_danh_sach(ds)

_cap_nhat(ds)
print("Danh sach hoc sinh sau khi cap nhat")
xem_danh_sach(ds)

_xoa_hs(ds)
print("Danh sach hoc sinh sau khi xoa")
xem_danh_sach(ds)

with open('danh_sach_hoc_sinh.json', 'w', encoding='utf-8') as f:
    json.dump([hs.in_ds() for hs in ds], f, ensure_ascii=False, indent=4)

print("Da luu danh sach hoc sinh vao file 'danh_sach_hoc_sinh.json'")