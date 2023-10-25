## pip install matplotlib

from threading import Thread
import time
import random
from numpy import log as ln
import datetime
import math
import threading
import matplotlib.pyplot as plt
import numpy as np
import statistics
import matplotlib
matplotlib.use("pdf")
from math import sqrt

count_server = 0
count_client = 0

################################################################
TChegada = 9.5	# Taxa de chegada
#TChegada = 9.5	# Taxa de chegada
TAtendimento = 10.0 	# Taxa de atendimento

tempo_espera = []
tempo_espera_pos_transiente = []
tempo_atendimento = []
#clientes_na_fila = any
servidor_em_atendimento = False
tempo_anterior_server = datetime.datetime.now()
tempo_anterior_client = datetime.datetime.now()
count_clientes_na_fila = 0
z_95 = 1.960

k_mser = 6
# m é o número de blocos
m_mser = 5
N_mser = 0
numero_simulacoes = 0

N_mser = k_mser * m_mser
numero_simulacoes = N_mser

lista_Z = []
elementos_bloco = []
media_Z = 0
count_blocos = 1
count_client_number = 0
count_pos_transiente = 0
last_attended_client_number = 0
H_interval = 0
X_average = 0

continuar_simulacao = True
remover_transiente = True

# variaveis von neuman
beta_von = 0.94 # 273555 parei a simulacao
beta_von = 1.29
B_Von = 20
bloco_von = 100
count_blocos_von = 0


Eliminar_Correlacao = True
start_time = time.time()

def media_amostral(list):
  if len(list) == 0 :
    return 0.0

  sum = 0.0
  for element in list:
    sum = sum + element

  return sum/len(list)

def RVN_Numerador(list):
  if len(list) == 0 :
    return 0.0

  sum = 0.0
  anterior = 0
  count = 0
  for element in list:
    
    if count > 0:
        sum = sum + ((anterior - element)*(anterior - element))
    anterior = element
    count += 1

  return sum

def RVN_Denominador(list, R_):
  if len(list) == 0 :
    return 0.0

  sum = 0.0
  for element in list:
    sum = sum + ((element - R_)*(element - R_))

  return sum


def variancia_amostral(list):
  if len(list) == 0 :
    return 0.0

  media = media_amostral(list)

  sum = 0.0
  for element in list:
    sum = sum + ((element - media) * (element - media))

  return (1/( len(list)-1 )) * sum


def desvio_padrao(list):

  return math.sqrt(variancia_amostral(list))

def intervalo_confianca(list, z):

    first = 0
    second = 0
    if len(list)>0 :
        first = media_amostral(list) - ( (desvio_padrao(list) * z) / math.sqrt( len (list) ) )

        second = media_amostral(list) + ( (desvio_padrao(list) * z) / math.sqrt( len (list) ) )

    return [first, second]

def H_interval_calc(interval_confianca):
    return ((interval_confianca[1] - interval_confianca[0]))

def VA_Enponencial(T):
	# 1/TC: intervalo entre chegadas
	random_va = random.expovariate(1.0)

	while random_va > 1:
		random_va = random.expovariate(1)

	# X = -β ln (1 – U) - slide 27
	return -(1/T)  * ln( 1.0 - random_va )

def MSER_5Y_bloco(bloco: []):
    # k é o número de blocos 
    # k_mser = 5
    # m é o tamanho dos blocos
    # m_mser = 10
    # N_mser = k_mser * m_mser
    sum_bloco = 0.0
    i_mser = 0
    for elemento in bloco:
        sum_bloco += elemento
        i_mser += 1
        #print('elemento')
        #print(elemento)
    sum_bloco = sum_bloco / m_mser  
    return sum_bloco

def MSER_5Y(list_z):
    k_local = len(list_z)
    print('k_local: {0:}'.format(k_local))
    d_local = 0
    mser5_k_d_anterior = 0
    
    mser_list = []
    while ( d_local < ( (3*k_local)/5) ) :
        mser5_k_d = desvio_padrao(list_z) / math.sqrt(k_local-d_local)     
        
        if mser5_k_d in mser_list:
            print('falhou ***********************************')
            return d_local
        else:
            mser_list.append( mser5_k_d )

        #print('mser5_k_d')
        #print(mser5_k_d)
        if(d_local==0):
            mser5_k_d_anterior = mser5_k_d
        else:
            if(mser5_k_d < mser5_k_d_anterior):
                if(d_local>(k_local/2)):
                    print('falhou ***********************************')
                    return d_local
                else:
                    mser5_k_d_anterior = mser5_k_d
            
        
        d_local += 1
        list_z.pop() # remove first element

    return -1

def R1(list_z, elemento):
    countMaior = 0
    countMenor = 0
    for z_ele in list_z:
        
        if elemento > z_ele:
            countMaior += 1
        if elemento < z_ele:
            countMenor += 1
    if(countMaior == len(list_z)):
        print('falhou')
        return -1
    else:
        if(countMenor == len(list_z)):
            print('falhou')
            return -1
        else:
            return len(list_z)


def R2(list_z):

    media = media_amostral(list_z)

    anterior = 0
    count = 0 
    cruzou = False
    countCruzadas = 0
    for z_ele in list_z:
        
        if(count>0):
            if (z_ele > media) & (anterior > media):
                cruzou = False
                print('são maiores +++++++++++++++++++++++++++')
            else:
                if (z_ele < media) & (anterior < media):
                    cruzou = False
                    print('são menores +++++++++++++++++++++++++++')
                else:
                    cruzou = True
                    print('cruzou ++ ++++ ++++ ++++ +++++++++++++: {0:.4f} {1:.4f} {2:.4f}', anterior, z_ele, media)
        
        anterior = z_ele

        if(cruzou):
            countCruzadas += 1
        count += 1

    #print('countCruzadas *************************** media: {0:.4f}', media)
    #print(countCruzadas)

    if(countCruzadas>7):
        print('countCruzadas *************************** media: {0:.4f}', media)
        print(countCruzadas)

        return count
    else:
        return -1


def medias_blocos_OBM(lista_pos_transiente, bloco_OBM_local, divider):

    elementos_bloco_OBM = []
    lista_menores_medias_OBM = []
    medias_blocos = []
    count = 0

    for ele in lista_pos_transiente:
        elementos_bloco_OBM.append(ele)

        if(count % bloco_OBM_local == 0):
            
            elementos_bloco_OBM_copy = elementos_bloco_OBM.copy()

            elementos_bloco_OBM_less_S = elementos_bloco_OBM_copy

            media_bloco_OBM = media_amostral(elementos_bloco_OBM_less_S)

            medias_blocos.append( media_bloco_OBM )

            elementos_bloco_OBM = []
            slice_array = int( bloco_OBM_local/divider )
            #print('slice array {0:}'.format(slice_array))
            elementos_bloco_OBM = [x for x in elementos_bloco_OBM_copy[ slice_array :]]

            count = 0
        else:
            count += 1 

    return medias_blocos


def medias_blocos(lista_pos_transiente, bloco_von_local):

    elementos_bloco_von = []
    lista_menores_medias_von = []
    medias_blocos = []
    count = 0

    for ele in lista_pos_transiente:
        elementos_bloco_von.append(ele)

        if(count % bloco_von_local == 0):
            
            elementos_bloco_von_copy = elementos_bloco_von.copy()

            elementos_bloco_von_less_S = elementos_bloco_von_copy

            media_bloco_von = media_amostral(elementos_bloco_von_less_S)

            medias_blocos.append( media_bloco_von )

            elementos_bloco_von = []

        count += 1 

    return medias_blocos


def von_neuman(lista_pos_transiente, bloco_von_local):

    elementos_bloco_von = []
    lista_menores_medias_von = []
    count = 0

    for ele in lista_pos_transiente:
        elementos_bloco_von.append(ele)

        if(count % bloco_von_local == 0):
            
            elementos_bloco_von_copy = elementos_bloco_von.copy()

            elementos_bloco_von_less_S = elementos_bloco_von_copy

            media_bloco_von = media_amostral(elementos_bloco_von_less_S)

            menores_media_bloco_von = count_menores(elementos_bloco_von, media_bloco_von)

            lista_menores_medias_von.append( menores_media_bloco_von )

            elementos_bloco_von = []

        count += 1 

    R_ = media_amostral(lista_menores_medias_von)

    print('lista_menores_medias_von')
    print(lista_menores_medias_von)

    print('RVN_Denominador(lista_menores_medias_von, R_)')
    print(RVN_Denominador(lista_menores_medias_von, R_))

    return RVN_Numerador(lista_menores_medias_von) / RVN_Denominador(lista_menores_medias_von, R_)

def count_menores(elementos_bloco_von, media_bloco):
    count = 0
    for ele in elementos_bloco_von:
        if ele <= media_bloco:
            count += 1
    return count

class server(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global count_server
        global H_interval
        global X_average
        global tempo_anterior_server
        global servidor_em_atendimento
        global last_attended_client_number
        global elementos_bloco
        global tempo_espera
        global tempo_espera_pos_transiente
        global clientes_na_fila
        global count_client_number
        global continuar_simulacao
        global remover_transiente
        global media_Z
        global count_blocos
        global lista_Z
        global count_pos_transiente
        global beta_von
        global B_Von
        global bloco_von
        global Eliminar_Correlacao
        global start_time

        if(count_server==0):
            H_interval = z_95*3
            X_average = z_95

        print('(H_interval/X_average)>=z_95 server')
        print((H_interval/X_average)>=z_95)
        
        while ( remover_transiente  | Eliminar_Correlacao | continuar_simulacao ) :

            print('inside while {0:}'.format(last_attended_client_number))
            #fileResults = open("results.txt", "a")
            #fileResults.writelines('teste 222\n')
            #fileResults.close()

            va = VA_Enponencial( TAtendimento )

            time.sleep( va )

            last_attended_client_number += 1
            

            if(len(clientes_na_fila)>0):

                tempo_espera_menos_um = []
                tempo_anterior_client = clientes_na_fila.pop( next(iter(clientes_na_fila)) )
                current_time = datetime.datetime.now()
                delta = (current_time - tempo_anterior_client).microseconds
                tempo_espera_menos_um = tempo_espera.copy()
                tempo_espera.append( delta )
                elementos_bloco.append( delta )

                media_bloco_z = 0
                
                if(remover_transiente):

                    if(count_client_number % m_mser == 0):
                        
                        media_bloco_z = MSER_5Y_bloco(elementos_bloco)

                        lista_Z.append( media_bloco_z )

                        print('media_bloco_z {0:}'.format(media_bloco_z))

                        count_blocos += 1
                        elementos_bloco = []

                if(count_client_number>=30):

                    if remover_transiente:
                        
                        lista_Z_copy = lista_Z.copy()
                        result_Z = MSER_5Y(lista_Z_copy)
                        ## print('MSER_5Y(lista_Z): {0:}'.format(result_Z))
                        if result_Z != -1:
                            remover_transiente = False

                        ## result_r1 = R1(tempo_espera_menos_um, delta)
                        ## if result_r1 != -1:
                        ##     remover_transiente = False

                        #result_r2 = R2(tempo_espera)
                        #if result_r2 != -1:
                        #    remover_transiente = False

                    if not remover_transiente:

                        tempo_espera_pos_transiente.append(delta)

                        if( (B_Von * bloco_von) ==  count_pos_transiente):

                            if(Eliminar_Correlacao):
                                
                                von_value = von_neuman(tempo_espera_pos_transiente, bloco_von)

                                print('B_Von * bloco_von {0:} >> {1:}'.format(B_Von * bloco_von, count_pos_transiente))
                                strToSave = '{0:.4f}\n'.format(von_value)

                                fileResults = open("results.txt", "a")
                                fileResults.writelines( strToSave )
                                fileResults.close()
                                
                                Eliminar_Correlacao = not (von_value < beta_von)
                                bloco_von += 50
                            else:

                                medias_blocos_calc = medias_blocos_OBM( tempo_espera_pos_transiente, bloco_von, 4 )

                                X_average = media_amostral( medias_blocos_calc )
                                interval_confianca = intervalo_confianca( medias_blocos_calc, z_95)
                                
                                H_interval = H_interval_calc(interval_confianca)

                                if (H_interval/X_average)>=z_95:
                                    bloco_von += 50    
                                else:
                                    print('von_value >>>>>>>>>>>>>>>> >>>>>>>>>>{0:}'.format(von_value))
                                    
                                    print( 'interval_confianca server' )
                                    print( interval_confianca )

                                    print('X_average {0:}'.format(X_average))
                                    print('H_interval {0:}'.format( H_interval ))

                                    print('H_interval/X_average {0:}'.format(H_interval/X_average))
                                    
                                    print("--- %s seconds ---" % (time.time() - start_time))

                                    continuar_simulacao = False

                        count_pos_transiente += 1


# Create your dictionary class
class client_arrive_time(dict):
 
    # __init__ function
    def __init__(self):
        self = dict()
         
    # Function to add key:value
    def add(self, key, value):
        self[key] = value

clientes_na_fila = client_arrive_time()

class clients(Thread):

    def __init__(self):
        Thread.__init__(self)
    #def start(self):
        #self.servidor_em_atendimento_class = servidor_em_atendimento_param
        #self.start()
    def run(self):
        global H_interval
        global X_average
        global count_client   
        global z_95
        global tempo_anterior_client
        global clientes_na_fila
        global count_client_number
        global last_attended_client_number
        global servidor_em_atendimento
        global continuar_simulacao
        global remover_transiente

        if(count_client==0):
            H_interval = z_95*3
            X_average = z_95


        print('(H_interval/X_average)>=z_95 client {0:}'.format(count_client_number))
        print((H_interval/X_average)>=z_95)

        while ( remover_transiente | continuar_simulacao ) :

            va = VA_Enponencial( TChegada )
            time.sleep( va )

            #print('chegou cliente {0:}'.format(count_client_number))
            count_client_number += 1

            #servidor_em_atendimento_local = servidor_em_atendimento
            current_time = datetime.datetime.now()
            clientes_na_fila.add( count_client_number, current_time )
            #print('cliente chega e entra na fila de cliente {0:}'.format(count_client_number))
      
            count_client+=1

instance_clients = clients()
instance_clients.start()

instance_server = server()
instance_server.start()
