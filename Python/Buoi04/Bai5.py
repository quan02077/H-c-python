from datetime import datetime

class SinhVien:
    def __init__(self, maSv, tenSv, namSinh, diemTb):
        self.maSv = maSv
        self.tenSv = tenSv
        self.namSinh = namSinh
        self.diemTb = diemTb

    def get_maSv(self):
        return self.maSv

    def get_tenSv(self):
        return self.tenSv

    def get_namSinh(self):
        return self.namSinh

    def get_diemTb(self):
        return self.diemTb


def mangSv():
    sv = []
    n = int(input("Nhap so luong sinh vien: "))
    for i in range(n):
        print(f"\nNhap thong tin sinh vien thu {i+1}:")
        maSv = input("Nhap ma sinh vien: ")
        tenSv = input("Nhap ten sinh vien: ")
        namSinh = int(input("Nhap nam sinh: "))
        diemTb = float(input("Nhap diem trung binh: "))
        sv.append(SinhVien(maSv, tenSv, namSinh, diemTb))
    return sv


def hienThi(sv):
    print("\nDanh sach sinh vien:")
    for s in sv:
        print(f"Ma SV: {s.get_maSv()}, Ten SV: {s.get_tenSv()}, Nam sinh: {s.get_namSinh()}, Diem TB: {s.get_diemTb():.2f}")


def DieuKien(sv):
    count = 0
    for a in sv:
        if a.get_diemTb() >= 5.0:
            count += 1
    print(f"\nSo sinh vien co diem trung binh >= 5: {count}")


def Tuoi(sv):
    namHienTai = datetime.now().year
    print("\nCac sinh vien co tuoi >= 20: ")
    for b in sv:
        if namHienTai - b.get_namSinh() >= 20:
            print(f"Ma SV: {b.get_maSv()}, Ten SV: {b.get_tenSv()}, Nam sinh: {b.get_namSinh()}, Diem TB: {b.get_diemTb():.2f}")


def Demsv(sv):
    count = 0
    for c in sv:
        if len(c.get_maSv()) >= 4 and c.get_maSv()[2:4] == "DH":
            count += 1
    print(f"\nSo sinh vien he DH: {count}")


def DemSvcoTen(sv):
    count = 0
    for d in sv:
        if d.get_tenSv().split()[-1] == "Lan":
            count += 1
    print(f"\nSo sinh vien co ten la Lan: {count}")


def DemSvcoHo(sv):
    count = 0
    for e in sv:
        if e.get_tenSv().split()[0] == "Phan":
            count += 1
    print(f"\nSo sinh vien co ho la Phan: {count}")


sv = mangSv()
hienThi(sv)
DieuKien(sv)
Tuoi(sv)
Demsv(sv)
DemSvcoTen(sv)
DemSvcoHo(sv)
