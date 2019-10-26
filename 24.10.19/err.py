
#Error Örnek:
# print(a)  # a değişkeni yok 
# print(int('1a2'))
# print(10/0)
while True:
    try:
        x=int(input('x:'))
        y=int(input('y:'))
        print(x/y)
    # except ZeroDivisionError:
    #     print('y için 0 girilemez!')

    # except ValueError:
    #     print('x ve y için sayısal değer girin.')

    # except (ZeroDivisionError, ValueError) as e:
    #     print('yanlis bilgi girdiniz')
    #     print(e)

    # else:
    #     print('Her şey yolunda')
    except Exception as ex:
        print("yanlis bilgi girdiniz!",ex)
    
    else:
        break

    finally:
        print("try/except blogu sonlandı.")