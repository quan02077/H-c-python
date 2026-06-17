class MonHoc:
    def __init__(self, toan, ly, anh):
        self.toan = toan
        self.ly = ly
        self.anh = anh
    def get_toan(self):
        return self.toan
    def get_ly(self):
        return self.ly
    def get_anh(self):
        return self.anh

class SinhVien(MonHoc):
    def __init__(self, maSV, hoTen, toan, ly, anh):
        self.maSV = maSV
        self.hoTen = hoTen
        super().__init__(toan, ly, anh)
    def get_maSV(self):
        return self.maSV
    def get_hoTen(self):
        return self.hoTen
    def __str__(self):
        return f"Mã SV: {self.maSV}, Họ tên: {self.hoTen}, Toán: {self.toan}, Lý: {self.ly}, Anh: {self.anh}"

    # Hàm tiện ích để giữ điểm trong [0,10]
    def _clamp(self, value):
        return min(max(value, 0), 10)

    # Toán tử cộng
    def __add__(self, value):
        return SinhVien(
            self.maSV, self.hoTen,
            self._clamp(self.toan + value),
            self._clamp(self.ly + value),
            self._clamp(self.anh + value)
        )

    # Toán tử trừ
    def __sub__(self, value):
        return SinhVien(
            self.maSV, self.hoTen,
            self._clamp(self.toan - value),
            self._clamp(self.ly - value),
            self._clamp(self.anh - value)
        )

    # Toán tử nhân
    def __mul__(self, value):
        return SinhVien(
            self.maSV, self.hoTen,
            self._clamp(self.toan * value),
            self._clamp(self.ly * value),
            self._clamp(self.anh * value)
        )

    # Toán tử chia
    def __truediv__(self, value):
        if value == 0:
            print("Lỗi chia cho 0: giữ nguyên điểm")
            return self
        else:
            return SinhVien(
                self.maSV, self.hoTen,
                self._clamp(self.toan / value),
                self._clamp(self.ly / value),
                self._clamp(self.anh / value)
            )


# ======================
sv = []
n = int(input("Nhập vào số lượng sinh viên: "))
for i in range(n):
    print(f"\nNhập vào thông tin sinh viên thứ {i+1}: ")
    maSV = input("Mã SV: ")
    hoTen = input("Họ tên: ")
    toan = float(input("Điểm toán: "))
    ly = float(input("Điểm lý: "))
    anh = float(input("Điểm anh: "))
    sv.append(SinhVien(maSV, hoTen, toan, ly, anh))

print("\n===== Danh sách sinh viên =====\n")
for sinhVien in sv:
    print(sinhVien)

# Test toán tử
print("\n===== Thử toán tử trên sinh viên cuối cùng =====")
sinhVien = sv[-1]

print("\nADD 3:")
print(sinhVien + 3)

print("\nSUB 2:")
print(sinhVien - 2)

print("\nMUL 2:")
print(sinhVien * 2)

print("\nDIV 0:")
print(sinhVien / 0)
