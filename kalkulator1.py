import logging
import sys
logging.basicConfig(level=logging.DEBUG)
def kalkulator(first,second,third):
    if first==1:
        result=second+third
    elif first==2:
        result=second-third
    elif first==3:
        result=second*third
    elif first==4:
        result=second/third
    else:
        exit(1)
    print(result)
if __name__ =='__main__':
    print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    first=float(input())
    print("podaj składnik 1")
    second=float(input())
    print("podaj składnik 2")
    third=float(input())
    kalkulator(first,second,third)



