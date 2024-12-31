chuoi = input("Nhap vao chuoi (1 < do dai chuoi < 10^5): ")
print ("Chuoi ban dau:" + chuoi)
print("Chuoi bien doi:" + chuoi[::-1] )
print("Chuoi la mot palindrome:", chuoi==chuoi[::-1])