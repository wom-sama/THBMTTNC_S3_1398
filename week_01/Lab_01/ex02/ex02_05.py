so_gio_lam =float(input("Nhap so gio lam moi tuan"))
luong_gio=float(input("Nhap thu lao tieu chuan"))
gio_tieu_tieu_chuan=44
gio_vuot=max(0,so_gio_lam-gio_tieu_tieu_chuan)
thuc_linh=gio_tieu_tieu_chuan*luong_gio+gio_vuot*luong_gio*1.5
print(f"so tien thuc linh la:{thuc_linh}")