class SanPham:
    def _init_(self, Gia, TenSanPham, GiamGia):
        self.TenSanPham = TenSanPham
        self.Gia = Gia
        self.GiamGia = GiamGia
    def ThueNhapKhau(self):
        return self.Gia * 0.1
    def XuatThongTinSanPham(self):
        print(f"sản phẩm {self.TenSanPham} có giá {self.Gia} được giảm giá {self.GiamGia} và thuế nhập khẩu {self.TenSanPham}")
    def NhapThongTinSanPham(self):
        self.TenSanPham = input("tên sản phẩm: ")
        self.Gia = float(input("Giá: "))
        self.GiamGia = float(input("Giảm giá: "))
