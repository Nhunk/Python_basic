List =  [32, 44, -9, -4, 8, 47, 10, -10]

#Bài 1: Tính tổng các phần tử của danh sách
def Bai1():
    tong = 0
    for i in List:
        tong += i
    print("1. \nTong cac phan tu cua danh sach la: ", tong)
    Bai3(tong)

#Bài 2: Đếm số lượng các số hạng dương và tổng của các số hạng dương
def Bai2():
    so_duong = 0
    tong_duong = 0
    for x in List:
        if x > 0:
            so_duong +=1
            tong_duong+=x
    print("2. \nSo so hang duong la: ", so_duong)
    print("Tong cac so hang duong la: ", tong_duong)
    Bai3(so_duong, tong_duong)

#Bài 3: Tính TBC của cả danh sách và TBC của các phần tử dương
def Bai3(tong, so_duong, tong_duong):
    TBC = sum(List)/len(List)
    TBC_duong = sum(x for x in List if x > 0)/sum(1 for x in List if x >0)
    print("3. \nTrung binh cong cua danh sach la: ", TBC)
    print("Trung binh cong cua so duong trong danh sach la: ", TBC_duong)

#Bài 4: Tìm vị trí của phần tử âm đầu tiên trong danh sách
def Bai4():
    for num in List:
        if num < 0:
            vt_am_dau = List.index(num)
            print("4. \nVi tri cua so am dau tien trong danh sach la: ", vt_am_dau)
            break

#Bài 5: Tìm vị trí của phần tử dương cuối cùng trong danh sách
def Bai5():
    for i in range(len(List)-1, -1, -1):
        if List[i] > 0:
            print("5. \nVi tri so duong cuoi cung trong danh sach la : ",i)
            break

#Bài 6: Tìm phần tử lớn nhất và vị trí của phần tử lớn nhất cuối cùng
def Bai6():
    max_list = max(List)
    for i in range(len(List)-1, -1, -1):
        if List[i]==max_list:
            max_index = i
            break
    print(f"6. \nPhan tu lon nhat la {max_list} va vi tri cuoi cung cua no trong list la {max_index} ")

#Bài 7: Tìm phần tử lớn thứ nì và các vị trí của phần tử đạt giá trị lớn thứ nhì
def Bai7():
    first = float('-inf')
    second = float('-inf')
    for num in List:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    vt = [i for i, value in enumerate(List) if value == second]
    print(f'Phan tu lon thu nhi la: {second}')
    print(f'Cac vi tri cua phan tu lon thu nhi la: {vt}')

#Bài 8: tính số lượng các số dương liên tiếp nhiều nhất.
def Bai8():
    ans = 0
    cur = 0
    for x in List:
        if x > 0:
            cur +=1
            ans = max(ans, cur)
        else:
            cur = 0
    print(f"So luong so duong lien tiep nhieu nhat la: {ans}")

#Bài 9: Tính số lượng các số dương liên tiếp có tổng lớn nhất
def Bai9():
    max_sum = 0 # Tổng lớn nhất của các số dương liên tiếp
    cur_sum = 0 # Tổng của các số dương liên tiếp hiện tại
    max_length = 0 # Độ dài của đoạn số dương liên tiếp có tổng lớn nhất
    cur_length = 0 # Độ dài của đoạn số dương liên tiếp hiện tại
    for num in List:
        if num > 0:
            cur_sum += num
            cur_length += 1
        else:
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_length = cur_length
            cur_length = 0
            cur_sum = 0
    print(f'So luong cac so duong lien tiep co tong lon nhat la: {max_length}')

#Bài 10: Tính số lượng phần tử đan dấu nhiều nhất
def Bai10():
    max = 0
    cur = 0
    for i in range(len(List) - 1):
        if List[i] * List[i+1] < 0:
            cur +=1
            if cur > max:
                max = cur
        else:
            cur = 0
    max +=1
    print(f'So luong cac phan tu lien tiep dan dau nhieu nhat la: {max}')

#Bài 11: Tính số lượng các phần tử không tăng nhiều nhất
def Bai11():
    max = 1
    cur = 1
    for i in range(1,len(List)):
        if List[i] <= List[i-1]:
            cur += 1
            if cur > max:
                max =cur
        else:
            cur = 1
    print(f'So luong cac phan tu lien tiep khong tang nhieu nhat la: {max}')

#Bài 12: Tìm vị trí bắt đầu đoạn con dương liên tiếp có nhiều phần tử nhất
def Bai12():
    max = 0
    start = -1
    cur = 0 # Độ dài của đoạn dương liên tiếp hiện tại
    cur_star = -1 # Vị trí bắt đầu của đoạn dương liên tiếp hiện tại
    for i in range(len(List)):
        if List[i] > 0:
            if cur == 0:
                cur_start = i
            cur +=1
        else:
            if cur > max:
                max = cur
                start = cur_start
            cur = 0
    if cur > max:
        max = cur
        start = cur_start
    print(f'Vi tri bat dau doan so duong lien tiep dai nhat la: {start}')        

#Bài 13: Tìm đoạn con có các số hạng dương liên tiếp có tổng lớn nhất
def Bai13():
    cur = []
    cur_sum = 0
    max = []
    max_sum = 0
    for num in List:
        if num > 0:
            cur.append(num)
            cur_sum += num
        else:
            if cur_sum > max_sum :
                max_sum = cur_sum
                max = [cur]
            elif cur_sum == max_sum & cur_sum > 0:
                max.append(cur)
            cur=[]
            cur_sum =0
    if cur_sum > max_sum:
        max = [cur]
    elif cur_sum == max_sum and cur_sum > 0:
        max.append(cur)
    print(f'So doan con duong lien tiep co tong lon nhat la: {len(max)}')
    print("Cac doan con do la: ", end = " ")
    for i in max:
        print(i)

#Bài 14: Đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím
def Bai14():
    X = int(input("Nhap gia tri X: "))
    count = List.count(X)
    print(f'So luong phan tu co gia tri bang {X} trong danh sach la: {count}')

#Bài 15: Chuyển các phần tử dương trong danh sách lên đầu và in ra màn hình
def Bai15():
    duong = [x for x in List if x > 0]
    khong_duong = [x for x in List if x <= 0]
    new = duong + khong_duong
    print(f'Danh sach sau khi dua cac phan tu duong len dau la: {new}')

#Bài 16: Tìm phần tử là số nguyên tố của danh sách và vị trí của nó trong danh sách
def Bai16():
    sont = [] #List chứa các số nguyên tố tìm được
    for index, value in enumerate(List):
        if value < 2:
            continue
        kt = 1
        for i in range(2, int(value ** 0.5) +1):
            if value % i == 0:
                kt = 0
                break
        if kt:
            sont.append((value, index))
    print("Cac so nguyen to tim duoc la: ")
    for x, vt in sont:
        print(f"So {x} o vi tri {vt}")

#Bài 17: Chèn một số m vào đầu, cuối và vị trí thứ 5 của danh sách
def Bai17():
    m = int(input("Nhap so can chen: "))
    List.insert(0, m)  
    List.append(m)
    List.insert(4,m)   
    print(List)  

#Bài 18: Chèn danh sách [1, 2, 3] vào vị trí đầu, cuối và vị trí thứ 5 của danh sách
def Bai18():
    A = [1, 2, 3]
    List_1 = A + List
    List_1.extend(A)
    List_1 = List_1[:4] + A + List_1[4:]
    print(List_1)  

#Bài 19: Xóa phần tử thứu k nhập từ bàn phím
def Bai19():
    k = int(input("Nhap vi tri k cần xoa: "))
    if k < 0 or k >= len(List):
        print("Vi tri khong hop le")
    else:
        del List[k]
        print(f"List sau khi xoa: {List}")

#Bài 20: Sắp xếp danh sách theo thứ tự tăng dần, giảm dần
def Bai20():
    List_tang = sorted(List)
    print(f"Danh sach xep tang dan: {List_tang}")
    List_giam = sorted(List, reverse=True)
    print(f"Danh sach xep giam dan: {List_giam}")
def main():
    while True:    
        choice = int(input("Nhap lua chon cua ban: "))  
        if choice == 0:
            print("Ket thuc chuong trinh!")
            break
        elif choice == 1:
            Bai1()
        elif choice == 2:
            Bai2()
        elif choice == 3:
            Bai3()
        elif choice == 4:
            Bai4()
        elif choice == 5:
            Bai5()
        elif choice == 6:
            Bai6()
        elif choice == 7:
            Bai7()
        elif choice == 8:
            Bai8()
        elif choice == 9:
            Bai9()
        elif choice == 10:
            Bai10()
        elif choice == 11:
            Bai11()
        elif choice == 12:
            Bai12()
        elif choice == 13:
            Bai13()
        elif choice == 14:
            Bai14()
        elif choice == 15:
            Bai15()
        elif choice == 16:
            Bai16()
        elif choice == 17:
            Bai17()
        elif choice == 18:
            Bai18()
        elif choice == 19:
            Bai19()
        elif choice == 20:
            Bai20()
        else:
            print("Lua chon khong hop le, vui long chon lai.")
main()