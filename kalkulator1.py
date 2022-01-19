import logging
import math
logging.basicConfig(level=logging.DEBUG)
def kalkulator(first,second,third):
    if first==1:
        logging.info("Dodaję %d i %d" %(second,third))
        result=second+third
    elif first==2:
        logging.info("Odajemuję %d i %d" %(second,third))
        result=second-third
    elif first==3:
        logging.info("Mnoze %d i %d" %(second,third))
        result=second*third
    elif first==4:
        logging.info("Dziele %d i %d" %(second,third))
        result=second/third
    else:
        logging.error("Niepoprawne określenie działania")
        exit(1)
    logging.info("Wynik: %d" % result)
if __name__ =='__main__':
    print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    first=int(input())
    print("podaj składnik 1")
    second=float(input())
    print("podaj składnik 2")
    third=float(input())
    kalkulator(first,second,third)
