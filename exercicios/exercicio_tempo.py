import time
t= time.localtime()
print(t) # este e o objeto que contem o retorno da chamada anterior



def dia_semana(w):
    nome_dia=["2a-feira",
              "3a-feira",
              "4a-feira",
              "5a-feira",
              "6a-feira",
              "Sabado",
              "Dmingo"]
    return nome_dia[w]

def mes(m):
    nome_mes=["Janeiro",
              "Fevereiro",
              "Marco",
              "Abril"
              "Maio",
              "Junho",
              "Julho",
              "Agosto",
              "Setembro",
              "Outubro",
              "Novembro",
              "Dezembro" ]
    return nome_mes[m-1]

def mostrar_dia_hora():
    lt=time.localtime()
    print("\n\n**********************************************************************\n")
    print("Hoje é ",dia_semana(lt.tm_wday),
          " ",
          lt.tm_mday,
          " de ",mes(lt.tm_mon),
          " de ",lt.tm_year,
          " e são as ", lt.tm_hour,
          ":",lt.tm_min,
          "horas\n")
    print("**********************************************************************\n")
    #    gmt=time.gmtime()


    
mostrar_dia_hora()
