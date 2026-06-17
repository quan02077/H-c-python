import random

def mat_Khau():
  try:
    do_dai = int(input("Nhap do dai mat khau: "))
  except ValueError:
    print("Vui long nhap vao mot so nguyen!")
    return None
  chu_cai = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  so = '0123456789'
  ki_tu = '!@#$%^&*'
  DS = chu_cai + so + ki_tu
  mat_khau = ''.join(random.choice(DS) for a in range(do_dai))
  return mat_khau
print(f"Mat khau: {mat_Khau()}")