try:
    nilai = int(input("Masukan Nilai : "))
    if 90 <= nilai <= 100:
        print("Nilai Huruf : A")
        print("Predikat : Dengan Pujian")
    elif 80 <= nilai <= 89:
        print("Nilai Huruf : B")
        print("Predikat : Sangat Memuaskan")
    elif 70 <= nilai <= 79:
        print("Nilai Huruf : C")
        print("Predikat : Memuaskan")
    elif 60 <= nilai <= 69:
        print("Nilai Huruf : D")
        print("Predikat : Tidak Memuaskan")
    elif 0 <= nilai <= 59:
        print("Nilai Huruf : E")
        print("Predikat : Tidak LULUS")
except ValueError:
    print("Masukan Nilai 0-100")