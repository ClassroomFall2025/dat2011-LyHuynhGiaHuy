import re

class NhanVien:
    def __init__(self, Ma, HoTen, Luong):
        self.Ma = Ma.strip()
        self.HoTen = HoTen.strip()
        self.Luong = float(Luong)

    def TinhThuNhap(self):
        return self.Luong

    def TinhThue(self):
        ThuNhap = self.TinhThuNhap()
        if ThuNhap < 9000000:
            return 0.0
        elif ThuNhap <= 15000000:
            return ThuNhap * 0.10
        else:
            return ThuNhap * 0.12

    def __str__(self):
        return f"{self.Ma:10} | {self.HoTen:25} | Lương: {self.Luong:,.0f} | Thu nhập: {self.TinhThuNhap():,.0f} | Thuế: {self.TinhThue():,.0f}"


class TiepThi(NhanVien):
    def __init__(self, Ma, HoTen, Luong, DoanhSo, TyLeHoaHong):
        super().__init__(Ma, HoTen, Luong)
        self.DoanhSo = float(DoanhSo)
        self.TyLeHoaHong = self.ChuanTyLe(TyLeHoaHong)

    def ChuanTyLe(self, TyLe):
        TyLe = float(TyLe)
        if TyLe > 1:
            return TyLe / 100.0
        return TyLe

    def TinhThuNhap(self):
        return self.Luong + self.DoanhSo * self.TyLeHoaHong

    def __str__(self):
        return f"{self.Ma:10} | {self.HoTen:25} | Lương: {self.Luong:,.0f} | Doanh số: {self.DoanhSo:,.0f} | Hoa hồng: {self.TyLeHoaHong*100:.1f}% | Thu nhập: {self.TinhThuNhap():,.0f} | Thuế: {self.TinhThue():,.0f}"


class TruongPhong(NhanVien):
    def __init__(self, Ma, HoTen, Luong, LuongTrachNhiem):
        super().__init__(Ma, HoTen, Luong)
        self.LuongTrachNhiem = float(LuongTrachNhiem)

    def TinhThuNhap(self):
        return self.Luong + self.LuongTrachNhiem

    def __str__(self):
        return f"{self.Ma:10} | {self.HoTen:25} | Lương: {self.Luong:,.0f} | Trách nhiệm: {self.LuongTrachNhiem:,.0f} | Thu nhập: {self.TinhThuNhap():,.0f} | Thuế: {self.TinhThue():,.0f}"
    

def KiemTraMaHopLe(Ma):
    if not Ma or not Ma.strip():
        return False
    return re.match(r'^[A-Za-z0-9-]+$', Ma.strip()) is not None

def TimTheoMa(DanhSach, Ma):
    for Nv in DanhSach:
        if Nv.Ma.lower() == Ma.strip().lower():
            return Nv
    return None

def ThemNhanVien(DanhSach, Nv):
    if TimTheoMa(DanhSach, Nv.Ma):
        return False
    DanhSach.append(Nv)
    return True

def XoaTheoMa(DanhSach, Ma):
    Nv = TimTheoMa(DanhSach, Ma)
    if Nv:
        DanhSach.remove(Nv)
        return True
    return False

def SapXepTheoThuNhap(DanhSach, GiamDan=True):
    return sorted(DanhSach, key=lambda x: x.TinhThuNhap(), reverse=GiamDan)

def Top5ThuNhap(DanhSach):
    return SapXepTheoThuNhap(DanhSach, True)[:5]

def HienThiDanhSach(DanhSach):
    if not DanhSach:
        print("Danh sách nhân viên trống.")
        return
    print("-" * 120)
    for Nv in DanhSach:
        print(Nv)
    print("-" * 120)