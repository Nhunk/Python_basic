#1. Viết chương trình sử dụng set để loại bỏ các phần tử trùng lặp và in ra ds mới.
def Cau1():
    numbers = [1, 2, 2, 3, 4, 4, 5]
    unique = set(numbers)
    unique_list = list(unique)
    print(unique_list)

#2. Thực hiện các thao tác tính: hợp, giao, hiệu, hiệu đối xứng.
def Cau2():
    A = {1, 2, 3, 4, 5} 
    B = {4, 5, 6, 7, 8}
    hop = A.union(B)
    print(f"Hop cua A va B la: {hop}")
    giao = A.intersection(B)
    print(f"Giao cua A va B la: {giao}")
    hieu = A.difference(B)
    print(f"Hieu cua A va B la: {hieu}")
    dx = A.symmetric_difference(B)
    print(f"Hieu doi xung cua A va B la: {dx}")

#3. Nhập chuỗi và đếm số lượng ký tự độc nhất có trong chuỗi đó.
def Cau3():
    chuoi = input("Nhap chuoi: ")
    chuoi_set = set(chuoi) #Loai bo ky tu trung lap
    dem = len(chuoi_set)
    print(f"So ky tu doc nhat trong chuoi la: {dem}")

#4. Tìm các phần tử xuất hiện trong cả danh sách.
def Cau4():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    chung = set(list1)&set(list2)
    chung_list = list(chung)
    print(chung_list)

#5. Kiểm tra tập A có là tập con của B hay không.
def Cau5():
    A = {1, 2, 3}
    B = {1, 2, 3, 4, 5}
    con = A.issubset(B)
    if con:
        print("A la con B")
    else:
        print("A khong la con B")

#6. Loại bỏ các phần tử của set B ra khỏi set A.
def Cau6():
    A = {1, 2, 3, 4, 5}
    B = {3, 4, 5, 6, 7}
    loai = A.difference(B)
    print(loai)

#7. Nhập chuỗi và tạo một set từ các ký tự trong chuỗi đó nhưng loại bỏ các ký tự đặc biệt và khoảng trắng.
def Cau7():
    A = input("Nhap chuoi: ")
    A_loai = {char for char in A if char.isalnum()}
    print(A_loai)

#8. Tìm tất cả các cặp phần tử trong danh sách có tổng bằng một giá trị cho trước S.
def Cau8():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    S = 8
    seen= set()
    kq = set()
    for num in numbers:
        target = S - num
        if target in seen:
            kq.add((min(num, target), max(num,target)))
        seen.add(num)
    print(f"Cac cap phan tu co tong bang {S} la : {list(kq)}")

#9. Tìm phần tử chung giữa 3 set.
def Cau9():
    A = {1, 2, 3, 4}
    B = {2, 3, 5}
    C = {1, 2, 6}
    D = A.intersection(B).intersection(C)
    print(D)

#10. Tìm tất cả các số ngyên tố trong danh sách và lưu chúng vào một set.
def Cau10():
    numbers = [10, 15, 17, 19, 21, 23]
    kq = []
    for i in numbers:
        if i < 2:
            continue
        kt = 1
        for value in range(2, int(i**0.5)+1):
            if i%value==0:
                kt =0
                break
        if kt:
            kq.append(i)
    print(set(kq))

#11. Tạo ra tất cả các tập hợp con của một set đầu vào. Kết quả phải bao gồm cả tạo rỗng và chính set ban đầu.
def Cau11():
    A = {1, 2, 3}
    B = [[]]
    for i in A:
        B +=[x + [i] for x in B]
    kq = [set(n) for n in B]
    print(f"Tat ca cac tap hop con cua {A} la : {kq}")

#12. Tìm tất cả các bộ ba phần tử có tổng bằng một giá trị cho trước S.
def Cau12():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    S = 15
    numbers_set = set(numbers)
    kq =set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            value = S - numbers[i] - numbers[j]
            if value in numbers_set and value != numbers[i] and value != numbers[j]:
                k = tuple(sorted([numbers[i], numbers[j], value]))
                kq.add(k)
    output = sorted(kq)
    print(f"Cac bo ba co tong bang {S} la: {output}")

#13. Kiểm tra xem một chuỗi có phải là pangram hay không. Pangram là một câu chứa tất cả các chữ cái trong bảng chữ cái ít nhất một lần.
def Cau13():
    a = "The quick brown fox jumps over the lazy dog"
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    a_set = set( i for i in a.lower() if i.isalpha())
    kq = alphabet.issubset(a_set)
    print(kq)

#14. Tìm số nguyên tố chung giữa hai danh sách.
def Cau14():
    list1 = [2, 3, 4, 5, 7]
    list2 = [3, 5, 6, 7, 11]
    sont = lambda num: num > 1 and all(num%i!=0 for i in range(2, int(num**0.5)+1))
    s1 = {i for i in list1 if sont(i)}
    s2 = {i for i in list2 if sont(i)}
    kq = s1.intersection(s2)
    print(kq)

def main():
    while True:
        choice = input("Nhap lua chon: ")
        if choice == '1':
            Cau1()
        elif choice == '2':
            Cau2()
        elif choice == '3':
            Cau3()
        elif choice == '4':
            Cau4()
        elif choice == '5':
            Cau5()
        elif choice == '6':
            Cau6()
        elif choice == '7':
            Cau7()
        elif choice == '8':
            Cau8()
        elif choice == '9':
            Cau9()
        elif choice == '10':
            Cau10()
        elif choice == '11':
            Cau11()
        elif choice == '12':
            Cau12()
        elif choice == '13':
            Cau13()
        elif choice == '14':
            Cau14()
        elif choice == '0':
            break
        else:
            print("Lua chon khong hop le. Vui long chon lai.")

if __name__ == "__main__":
    main()