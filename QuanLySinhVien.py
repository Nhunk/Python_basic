# Danh sách sinh viên
DSSV = []

# Hàm thêm sinh viên mới
def them_SV():
    ma_sv = input("Nhap ma sinh vien: ")
    ho_ten = input("Nhap ho ten: ")
    tuoi = input("Nhap tuoi: ")
    nganh = input("Nhap nganh hoc: ")
    diemTB = input("Nhap diem trung binh: ")
    sinh_vien = {"ma_sv": ma_sv, "ho_ten": ho_ten, "tuoi": tuoi, "nganh": nganh, "diemTB": diemTB}
    DSSV.append(sinh_vien)
    print("Da them sinh vien thanh cong!\n")

# Hàm cập nhật tên sinh viên
def capnhat_tenSV():
    ma_sv = input("Nhap ma sinh vien can cap nhat ten: ")
    for sv in DSSV:
        if sv['ma_sv'] == ma_sv:
            new_name = input("Nhap ten moi: ")
            sv['ho_ten'] = new_name
            print("Cap nhat ten sinh vien thanh cong!\n")
            return
    print("Khong tim thay sinh vien voi ma da nhap.\n")

# Hàm xóa sinh viên
def xoa_SV():
    ma_sv = input("Nhap ma sinh vien can xoa: ")
    for sv in DSSV:
        if sv['ma_sv'] == ma_sv:
            DSSV.remove(sv)
            print("Da xoa sinh vien thanh cong!\n")
            return
    print("Khong tim thay sinh vien voi ma da nhap.\n")

# Hàm hiển thị danh sách sinh viên
def hien_thi_DSSV():
    print("\nDanh sach sinh vien:")
    for sv in DSSV:
        print(f"Ma SV: {sv['ma_sv']}, Ho Ten: {sv['ho_ten']}, Tuoi: {sv['tuoi']}, Nganh hoc: {sv['nganh']}, Diem TB: {sv['diemTB']}")
    print()

# Hàm tìm kiếm sinh viên
def tim_kiem_SV():
    ma_sv = input("Nhap ma sinh vien can tim: ")
    for sv in DSSV:
        if sv['ma_sv'] == ma_sv:
            print(f"Ma SV: {sv['ma_sv']}, Ho Ten: {sv['ho_ten']}, Tuoi: {sv['tuoi']}, Nganh hoc: {sv['nganh']}, Diem TB: {sv['diemTB']}")
            return
    print("Khong tim thay sinh vien voi ma da nhap.\n")

# Hàm thống kê số lượng sinh viên
def thong_ke_SV():
    print(f"Co tong cong {len(DSSV)} sinh vien trong danh sach.\n")

# Hàm sắp xếp danh sách sinh viên theo điểm trung bình giảm dần
def sap_xep_SV():
    DSSV.sort(key=lambda x: float(x['diemTB']), reverse=True)
    print("Danh sach sinh vien da duoc sap xep theo diem trung binh giam dan.\n")

# Hàm đảo ngược danh sách sinh viên
def dao_nguoc_DSSV():
    DSSV.reverse()
    print("Danh sach sinh vien da duoc dao nguoc.\n")

# Chương trình chính với menu
def main():
    while True:
        print("---- Quan Ly Danh Sach Sinh Vien ----")
        print("1. Them sinh vien moi")
        print("2. Cap nhat ten sinh vien")
        print("3. Xoa sinh vien")
        print("4. Hien thi danh sach sinh vien")
        print("5. Tim kiem sinh vien")
        print("6. Thong ke so luong sinh vien")
        print("7. Sap xep danh sach sinh vien theo diem trung binh")
        print("8. Dao nguoc danh sach sinh vien")
        print("Q. Thoat chuong trinh")
        lua_chon = input("Nhap lua chon cua ban: ")
        
        if lua_chon == '1':
            them_SV()
        elif lua_chon == '2':
            capnhat_tenSV()
        elif lua_chon == '3':
            xoa_SV()
        elif lua_chon == '4':
            hien_thi_DSSV()
        elif lua_chon == '5':
            tim_kiem_SV()
        elif lua_chon == '6':
            thong_ke_SV()
        elif lua_chon == '7':
            sap_xep_SV()
        elif lua_chon == '8':
            dao_nguoc_DSSV()
        elif lua_chon.upper() == 'Q':
            print("Da thoat chuong trinh.")
            break
        else:
            print("Lua chon khong hop le. Vui long chon lai.\n")

# Chạy chương trình chính
main()