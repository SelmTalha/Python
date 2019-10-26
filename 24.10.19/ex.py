




# x=10
# if x>5:
#     raise Exception("x 5'ten büyük değer alamaz.")  # Raise:Orjinal hata mesajını içine yazılan ifadeyle değiştirir.

while True:
    def parola_kontrolu(parola):
        if len(parola)<8:
            raise Exception("parola en az 7 karakterli olmalı")

    parola=input("Parola giriniz:")

    try:
        parola_kontrolu(parola)

    except Exception as ex:
        print(ex)

    else:
        print("Geçerli parola")
        break




