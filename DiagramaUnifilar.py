from pyautocad import APoint, Autocad

# Iniciação do programa
acad = Autocad()
print(acad.doc.Name)

# Entrada de Dados
n_total_de_quadros = 3
nomes = ['QDC - 1', 'QDC - 2', 'QDC - 3', 'QDC - 4', 'QDC - 5', 'QDC - 6', 'QDC - 7', 'QDC - 8', 'QDC - 9', 'QDC - 10']
fases = [3, 2, 1, 3, 2, 3, 2, 3, 2, 1]
dij=['10A','20A','30A','40A','50A','60A','70A','80A','90A','100A']
n_circuitos = [0,2,3,4,5,6,7,8,9,10]



# Funções
def calc_reservas(circuito):  # Essa função só irá trabalhar corretamente dentro de um loop.

    a = 0

    d = circuito * 0.2

    a = round(d + 0.5, 0)  # Tem que checar essa regra depois.

    if a <= 2:
        b = 2

    else:
        b = a


    c = circuito + b

    return c   # Calcula o número de circuitos reservas.

def ad_nome(ponto_inicial_variavel, nome_do_quadro):   # Essa função só rola dentro de loop.
    t = ponto_inicial_variavel + APoint(125, -25)
    t = acad.model.AddText(nome_do_quadro, t, 10)
    t.Color = 130

def desenha_quadros(ponto_inicial_variavel, n, i):# Essa função só irá trabalhar corretamente dentro de um loop.
    print(n)
    p1 = ponto_inicial_variavel
    p2 = p1 + APoint(250, 0)
    l1 = acad.model.AddLine(p1, p2)
    l1.Color = 130

    p3 = p2 + APoint(0, -92) + APoint(0, -30) * n
    l2 = acad.model.AddLine(p2, p3)
    l2.Color = 130

    p4 = p3 + APoint(-250, 0)
    l3 = acad.model.AddLine(p3, p4)
    l3.Color = 130

    p5 = p4 + APoint(0, 92) + APoint(0, 30) * n
    l4 = acad.model.AddLine(p4, p5)
    l4.Color = 130

def desenha_dijuntor(ponto_inicial_variavel,fase_do_quadro,valor_do_dijuntor):# Essa função só irá trabalhar corretamente dentro de um loop.

    # Linha e Dijuntor Geral (Sem fases)
    p6 = ponto_inicial_variavel + APoint(23, 50)
    p7 = ponto_inicial_variavel + APoint(23, -26)
    l5 = acad.model.AddLine(p6, p7)
    l5.Color = 130

    p8 = ponto_inicial_variavel + APoint(26, -26)
    c1 = acad.model.AddCircle(p8, 3)
    c1.Color = 130

    p9 = ponto_inicial_variavel + APoint(26, -52)
    c2 = acad.model.AddCircle(p9, 3)
    c2.Color = 130

    p10 = ponto_inicial_variavel + APoint(26, -39)
    arc1 = acad.model.AddArc(p10, 13, -3.14 / 2, 3.14 / 2)
    arc1.Color = 130

    p24 = ponto_inicial_variavel + APoint(23, -52)
    p25 = ponto_inicial_variavel + APoint(23, -62) + APoint(0, -30) * n
    l11 = acad.model.AddLine(p24, p25)
    l11.Color = 130

    # Decide o desenho da Fase do dijuntor
    if fase_do_quadro == 1:
        p11 = ponto_inicial_variavel + APoint(34, -39)
        p12 = ponto_inicial_variavel + APoint(44, -39)
        l5 = acad.model.AddLine(p11, p12)
        l5.Color = 130

    if fase_do_quadro == 2:
        p13 = ponto_inicial_variavel + APoint(34, -37)
        p14 = ponto_inicial_variavel + APoint(44, -37)
        l6 = acad.model.AddLine(p13, p14)
        l6.Color = 130

        p15 = ponto_inicial_variavel + APoint(34, -41)
        p16 = ponto_inicial_variavel + APoint(44, -41)
        l7 = acad.model.AddLine(p15, p16)
        l7.Color = 130

    if fase_do_quadro == 3:
        p17 = ponto_inicial_variavel + APoint(34, -39)
        p18 = ponto_inicial_variavel + APoint(44, -39)
        l8 = acad.model.AddLine(p17, p18)
        l8.Color = 130

        p19 = ponto_inicial_variavel + APoint(34, -42)
        p20 = ponto_inicial_variavel + APoint(44, -42)
        l9 = acad.model.AddLine(p19, p20)
        l9.Color = 130

        p21 = ponto_inicial_variavel + APoint(34, -36)
        p22 = ponto_inicial_variavel + APoint(44, -36)
        l10 = acad.model.AddLine(p21, p22)
        l10.Color = 130

    # Coloca o Valor do Dijuntor
    p23 = ponto_inicial_variavel + APoint(50, -39)
    t2 = acad.model.AddText(valor_do_dijuntor, p23, 5)
    t2.Color = 130

def desenha_circuitos(ponto_inicial_variavel, n_circ_no_quadro):

    cont = 0

    for k in range(n):

        p1 = ponto_inicial_variavel + APoint(23, -92) + APoint(0, -30) * k
        p2 = ponto_inicial_variavel + APoint(190, -92) + APoint(0, -30) * k
        l1 = acad.model.AddLine(p1, p2)
        l1.Color = 130

        cont += 1
    p3 = ponto_inicial_variavel + APoint(93, -91) + APoint(0, -30) * (cont - 1)
    t1 = acad.model.AddText('RESERVA', p3, 5)
    t1.Color = 130

    p4 = ponto_inicial_variavel + APoint(93, -91) + APoint(0, -30) * (cont - 2)
    t2 = acad.model.AddText('RESERVA', p4, 5)
    t2.Color = 130



# Loop principal
for i in range(n_total_de_quadros):

    #Definição do ponto inicial variavel
    p0 = APoint(0, 250)
    pv = p0 + APoint(300, 0) * i

    # Calcula o numero de circuitos reservas e retorna no n.
    n = calc_reservas(n_circuitos[i])

    # Desenha os quadros
    desenha_quadros(pv, n, i)

    # Adiciona o nome do quadro
    ad_nome(pv, nomes[i])

    # Desenha dijuntor completo e as linhas entorno dele
    desenha_dijuntor(pv, fases[i], dij[i])

    # Desenha circuitos no quadros
    desenha_circuitos(pv, n_circuitos[i])







# for obj in acad.iter_objects(['Circle', 'Line']):
#     print(obj.ObjectName)
#     print(obj.Position_X)

#for item in acad.iter_objects("Line"):
 #   print(item.Coordinates)



# for obj in acad.iter_objects():  -> testar se ele acha circulos aqui
#     print(obj)






