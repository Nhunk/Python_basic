import math
#Câu 1: Tìm ước chung lớn nhất của hai số a và b
def ucln():
    a = int(input("Nhap so a: "))
    b = int(input("Nhap so b: "))
    while b!=0:
        a, b = b, a%b
    print(f"Uoc chung lon nhat cua a va b la: {a}")

#Câu 2: Tính giai thừa của số n và in kết quả
def giaithua():
    n =int(input("Nhap so nguyen n: "))
    gt = 1
    for i in range(1,n+1):
        gt*=i
    print(f"Giai thua cua so nguyen n la: {gt}")

#Câu 3: Kiểm tra xem số nguyên n có phải là số nguyên tố hay không.
def ktsont():
    n = int(input("Nhap so n: "))
    if n<=1:
        print(f"{n} khong la so nguyen to")
    for i in range(2, int(math.sqrt(n)) +1 ): #Kiểm tra i từ 2 đến căn bậc 2 của n
        if n % i == 0:
            print(f"{n} khong la so nguyen to")
    print(f"{n} la so nguyen to")

#Câu 4: Tìm các số từ 2000 đến 3200 chia hết cho 7 nhưng không chia hết cho 5 và in chúng cách nhau bằng dấu phẩy
def chiahet7():
    a = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            a.append(str(i)) #Chuyển dữ liệu thành dạng chuỗi để in ra kết quả
    print(", ".join(a)) #Hàm join nối các số trong danh sách a bằng dấu ","

#Câu 5: Tạo một từ điển với các key là các số từ 1 đến n và value là bình phương của key rồi in ra: {1:1, 2:4, 3:9, 4:14}
def tao_dict():
    dic = {i:i**2 for i in range(1, 5)}
    print(dic)

#Câu 6: Dùng hàm ẩn danh lamda
def ham_lambda():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    output = list(filter(lambda x: x%2==0, lst)) #filter lọc các phần tử true từ hàm lambda kiểm tra trả về
    print(output)
    
def main():
    while True:
        choice = input("Nhap lua chon: ").strip().lower()
        if choice == '1':
            ucln()
        elif choice == '2':
            giaithua()
        elif choice == '3':
            ktsont()
        elif choice == '4':
            chiahet7()
        elif choice == '5':
            tao_dict()
        elif choice == '6':
            ham_lambda()
        elif choice == 'q':
            print("Thoat chuong trinh.")
            break
        else:
            print("Lua chon khong hop le! Vui long chon lai.")
if __name__ == "__main__":
    main()