

def func():
    num10 = int(input("Введите целое положительное число : "))
    if type(num10) is not int or num10<0:
      print("Повторюсь, введите целое положительное число : ")
      func()

    elif num10==0:
      print("Ноль в любой системе счистления будет нулем, введите что-нибудь поинтереснее : ")
      func()
    choice = int(input("В какую систему счисления вы хотите перевсти? Напишите 2 если в двоичную, 8 если восьмиричную, 0 если в обе: "))

    def convert(n, f):
      i=1
      d=0
      while n>0:
        d+=n%f*i 
        i*=10
        n//=f
      return(d)

    match choice: 
      case 2:
         print(convert(num10, 2))
      case 8:
         print(num10, "в 8-ой сс = ", convert(num10, 8))
      case 0: 
         print(num10, "в 2-ой сс = ", convert(num10, 2))
         print(num10, "в 8-ой сс = ", convert(num10, 8))
func()