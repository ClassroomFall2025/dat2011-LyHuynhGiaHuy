class CN:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    def ChuVi(self):
        return(self.dai + self.rong)*2
    def DienTich(self):
        return(self.dai*self.rong)
class HV(CN):
    def __init__(self, canh):
        super().__init__(canh, canh)
    def Xuat(self):
        print("Diện tích CN: ",{self.DienTich()})
        print("Chu vi CN: ",{self.Chuvi()})
        print("Chu Vi H: ",{self.ChuVi()})
        print("Diện tích: ",{self.DienTich()})

