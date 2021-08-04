from pyautocad import APoint, Autocad
import math

# Interação com o usuário

arq_aberto = 0

while arq_aberto == 0:

    print('\nVocê já abriu o "Arquivo Padrão D.U" no AutoCad?')

    resposta = input('[s] ou [n]: ')

    print('\n')

    if resposta == 's':

        acad = Autocad()

        print('Arquivo encontrado: ')

        print(acad.doc.Name)

        arq_correto = input('Este é o arquivo correto?\n[s] ou [n]: ')
        
        arq_aberto = 1
        
        if arq_correto == 'n':
            
            arq_aberto = 0          
            
    elif resposta == 'n':

        print('Abra o arquivo indicado para fazer o desenho')

    else:

        print('Esta resposta não é valida. ')

print('Desenhando ...')

# Entrada de Dados
n_total_de_quadros = 6
nomes = ['QDC - 1', 'QDC - 2', 'QDC - 3', 'QDC - 4', 'QDC - 5', 'QDC - 6', 'QDC - 7', 'QDC - 8', 'QDC - 9', 'QDC - 10']
fases = [3, 2, 1, 3, 2, 3, 2, 3, 2, 1]
dij = ['10A', '20A', '30A', '40A', '50A', '60A', '70A', '80A', '90A', '100A']
n_circuitos = [10, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numero_do_circuito = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def calc_reservas(n_circuitos_do_quadro):  # Essa função só irá trabalhar corretamente dentro de um loop.

    qtd_reserva = 2

    if n_circuitos_do_quadro > 30:
        
        qtd_reserva = int(0.15 * n_circuitos_do_quadro)

    elif n_circuitos_do_quadro > 12:

        qtd_reserva = 4

    elif n_circuitos_do_quadro > 6:

        qtd_reserva = 3

    return qtd_reserva

def perimetro_diagrama(ponto_ini, total_circ, nmr_fases, disjuntor):

    # Desenha o retângulo  (Cada linha vai ter uma altura de 60)

    # horizontal superior
    acad.model.AddLine(ponto_ini, APoint(ponto_ini.x + 360, ponto_ini.y)).Layer = 'EJEL05130C'

    # horizontal inferior
    acad.model.AddLine(APoint(ponto_ini.x, ponto_ini.y - 90 * (total_circ + 2)),
                       APoint(ponto_ini.x + 360, ponto_ini.y - 90 * (total_circ + 2))).Layer = 'EJEL05130C'

    # vertical esquerda
    acad.model.AddLine(ponto_ini, APoint(ponto_ini.x, ponto_ini.y - 90 * (total_circ + 2))).Layer = 'EJEL05130C'

    # vertical direita
    acad.model.AddLine(APoint(ponto_ini.x + 360, ponto_ini.y),
                       APoint(ponto_ini.x + 360, ponto_ini.y - 90 * (total_circ + 2))).Layer = 'EJEL05130C'

    # Disjuntor geral do diagrama 1º as linhas
    acad.model.AddLine(APoint(ponto_ini.x + 60, ponto_ini.y),
                       APoint(ponto_ini.x + 60, ponto_ini.y - 30)).Layer = 'EJEL05130C'

    acad.model.AddLine(APoint(ponto_ini.x + 60, ponto_ini.y - 90),
                       APoint(ponto_ini.x + 60, ponto_ini.y - 90 * (total_circ + 1))).Layer = 'EJEL05130C'

    # Agora os círculos e arco
    acad.model.AddCircle(APoint(ponto_ini.x + 65, ponto_ini.y - 30), 5).Layer = 'EJEL05130C'
    acad.model.AddCircle(APoint(ponto_ini.x + 65, ponto_ini.y - 90), 5).Layer = 'EJEL05130C'
    acad.model.AddArc(APoint(ponto_ini.x + 65, ponto_ini.y - 60), 30, (-math.pi) / 2,
                      (math.pi) / 2).Layer = 'EJEL05130C'


    # Informações do disjuntor
    if nmr_fases > 1:
        acad.model.AddLine(APoint(ponto_ini.x + 85, ponto_ini.y - 45),
                           APoint(ponto_ini.x + 100, ponto_ini.y - 45)).Layer = 'EJEL05130C'
        acad.model.AddLine(APoint(ponto_ini.x + 85, ponto_ini.y - 75),
                           APoint(ponto_ini.x + 100, ponto_ini.y - 75)).Layer = 'EJEL05130C'

    if nmr_fases != 2:
        acad.model.AddLine(APoint(ponto_ini.x + 85, ponto_ini.y - 60),
                           APoint(ponto_ini.x + 100, ponto_ini.y - 60)).Layer = 'EJEL05130C'

    acad.model.AddText('%s A' % disjuntor, APoint(ponto_ini.x + 105, ponto_ini.y - 65), 10).Layer = 'EJEL05130C'

def linha_diagrama(ponto_ini, total_circ, n_reservas, n_do_circuito, bitola_fio, fases, disjuntor):

    lista = list(range(total_circ - n_reservas))

    var = total_circ - n_reservas

    for i in lista:


        # Ponto inicial de cada linha
        ponto_zero = ponto_ini + APoint(60, -180) + APoint(0, -90) * i

        # Desenha as linhas
        acad.model.AddLine(ponto_zero, APoint(ponto_zero.x + 60, ponto_zero.y)).Layer = 'EJEL05130C'

        acad.model.AddLine(APoint(ponto_zero.x + 120, ponto_zero.y),
                           APoint(ponto_zero.x + 320, ponto_zero.y)).Layer = 'EJEL05130C'

        # Desenha os círculos
        acad.model.AddCircle(APoint(ponto_zero.x + 60, ponto_zero.y + 5), 5).Layer = 'EJEL05130C'

        acad.model.AddCircle(APoint(ponto_zero.x + 120, ponto_zero.y + 5), 5).Layer = 'EJEL05130C'

        # Desenha o arco
        acad.model.AddArc(APoint(ponto_zero.x + 90, ponto_zero.y + 10), 30, 0, math.pi).Layer = 'EJEL05130C'

        # Desenha as fases
        if len(fases) > 1:

            acad.model.AddLine(APoint(ponto_zero.x + 75, ponto_zero.y + 25),
                               APoint(ponto_zero.x + 75, ponto_zero.y + 55)).Layer = 'EJEL05130C'

            acad.model.AddLine(APoint(ponto_zero.x + 105, ponto_zero.y + 25),
                               APoint(ponto_zero.x + 105, ponto_zero.y + 55)).Layer = 'EJEL05130C'

        if len(fases) != 2:
            acad.model.AddLine(APoint(ponto_zero.x + 90, ponto_zero.y + 25),
                               APoint(ponto_zero.x + 90, ponto_zero.y + 55)).Layer = 'EJEL05130C'

        # Textos
        acad.model.AddText('%s' % n_do_circuito, APoint(ponto_zero.x + 335, ponto_zero.y), 10).Layer = 'EJEL05130C'
        acad.model.AddText('%s mm²' % bitola_fio, APoint(ponto_zero.x + 215, ponto_zero.y + 15), 10).Layer = 'EJEL05130C'
        acad.model.AddText('%s A' % disjuntor, APoint(ponto_zero.x + 80, ponto_zero.y - 15), 10).Layer = 'EJEL05130C'
        acad.model.AddText('%s' % fases, APoint(ponto_zero.x - 30, ponto_zero.y), 10).Layer = 'EJEL05130C'

    var2 = total_circ - n_reservas
    print(var2)

    for k in range(var2, total_circ):

        print(k)

        ponto_zero = ponto_ini + APoint(60, -180) + APoint(0, -90) * k

        acad.model.AddLine(ponto_zero, ponto_zero + APoint(300, 0))

        acad.model.AddText('Reserva', ponto_zero + APoint(335, 15), 10)





# Loop principal
for i in range(n_total_de_quadros):

    #Definição do ponto inicial variavel
    p0 = APoint(0, 250)

    pv = p0 + APoint(450, 0) * i

    reservas = calc_reservas(n_circuitos[i])

    total_circ = n_circuitos[i] + reservas

    perimetro_diagrama(pv, total_circ, 3, "70")

    linha_diagrama(pv, total_circ, reservas, numero_do_circuito[i], '3', '2', 20)



print('Pronto!')

# linha_diagrama(pv, numero_do_circuito[k], '3', '2', '20')


# for obj in acad.iter_objects(['Circle', 'Line']):
#     print(obj.ObjectName)
#     print(obj.Position_X)

#for item in acad.iter_objects("Line"):
 #   print(item.Coordinates)



# for obj in acad.iter_objects():  -> testar se ele acha circulos aqui
#     print(obj)






