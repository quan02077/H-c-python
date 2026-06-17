import random

def nhap_DS():
  n = int(input("Nhap vao so luong phan tu: "))
  DS = []
  for abc in range(n):
    x = int(input("Nhap vao phan tu: "))
    DS.append(x)
  return DS
def chon_so_random():
  DS = nhap_DS()
  x = random.choice(DS)
  return x
print(f"So ngau nhien chon tu mang: {chon_so_random()}")