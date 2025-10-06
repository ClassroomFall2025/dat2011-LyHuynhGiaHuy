def TinhTienNuoc(SoNuoc):
    GiaBanNuoc = (7500, 8800, 12000, 24000)
    if SoNuoc < 10 and SoNuoc >=0:
        TienNuocThang = SoNuoc * GiaBanNuoc[0]
    elif SoNuoc <= 20:
        TienNuocBan = 10 * GiaBanNuoc[0] + (SoNuoc - 10) * GiaBanNuoc[1]
    elif SoNuoc <=30:
        TienNuocBan = 10 * GiaBanNuoc[0] + 10 * GiaBanNuoc[1] + (SoNuoc - 20) * GiaBanNuoc[2]
    else: 
        TienNuocBan = 10 * GiaBanNuoc[0] + 10 * GiaBanNuoc[1] + 10 * GiaBanNuoc[2] + (SoNuoc - 30 ) * GiaBanNuoc[3]
    return TienNuocBan


def TinhNguyenLieu(B_DauXanh, B_ThapCam, B_Deo):
    Duong = B_DauXanh * 0.04 + B_ThapCam * 0.06 + B_Deo * 0.05
    Dau = B_DauXanh * 0.07 + B_ThapCam * 0 + B_Deo *0.02
    Nl = ("Sugar:",Duong , "Dau:",Dau)
    return Nl 

    