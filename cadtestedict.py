from pyautocad import Autocad, APoint
from blocks_ejel import linha_diagrama, perimetro_diagrama
import math

acad = Autocad()

# acad.model.AddLine(ponto inicial, ponto final)
# acad.model.AddCircle(centro, raio)
# acad.model.AddArc(centro do arco, raio do arco, ângulo do ponto inicial, ângulo do ponto final)

def perimetro_diagrama(ponto_ini, total_circ, nmr_fases, disjuntor):
            
    #Desenha o retângulo  (Cada linha vai ter uma altura de 60)
    acad.model.AddLine(ponto_ini, APoint(ponto_ini.x + 360, ponto_ini.y))
    acad.model.AddLine(APoint(ponto_ini.x, ponto_ini.y - 90*(total_circ + 2)), APoint(ponto_ini.x + 360, ponto_ini.y - 90*(total_circ + 2)))
    acad.model.AddLine(ponto_ini, APoint(ponto_ini.x, ponto_ini.y - 90*(total_circ + 2)))
    acad.model.AddLine(APoint(ponto_ini.x + 360, ponto_ini.y), APoint(ponto_ini.x + 360, ponto_ini.y - 90*(total_circ + 2)))
    
    #Disjuntor geral do diagrama   1º as linhas
    acad.model.AddLine(APoint(ponto_ini.x + 60, ponto_ini.y), APoint(ponto_ini.x + 60, ponto_ini.y - 30))
    acad.model.AddLine(APoint(ponto_ini.x + 60, ponto_ini.y - 90), APoint(ponto_ini.x + 60, ponto_ini.y - 90*(total_circ + 1)))
    
    #Agora os círculos e arco
    acad.model.AddCircle(APoint(ponto_ini.x + 65, ponto_ini.y - 30), 5)
    acad.model.AddCircle(APoint(ponto_ini.x + 65, ponto_ini.y - 90), 5)
    acad.model.AddArc(APoint(ponto_ini.x + 65, ponto_ini.y - 60), 30, (-math.pi)/2, (math.pi)/2)
   
    #Informações do disjuntor
    if nmr_fases > 1:
        acad.model.AddLine(APoint(ponto_ini.x + 75, ponto_ini.y - 50), APoint(ponto_ini.x + 105, ponto_ini.y - 50))        
        acad.model.AddLine(APoint(ponto_ini.x + 75, ponto_ini.y - 70), APoint(ponto_ini.x + 105, ponto_ini.y - 70))
        
    if nmr_fases != 2:
        acad.model.AddLine(APoint(ponto_ini.x + 75, ponto_ini.y - 60), APoint(ponto_ini.x + 105, ponto_ini.y - 60))
        
    acad.model.AddText('%s A' % disjuntor, APoint(ponto_ini.x + 105, ponto_ini.y - 65), 10)   
    


def linha_diagrama(ponto_ini, nmr_circuito, bitola_fio, fases, disjuntor):
    
    #Desenha as linhas
    acad.model.AddLine(ponto_ini, APoint(ponto_ini.x + 60, ponto_ini.y)).Layer = 'EJEL0550C'
    acad.model.AddLine(APoint(ponto_ini.x + 120, ponto_ini.y), APoint(ponto_ini.x + 320, ponto_ini.y)).Layer = 'EJEL0550C'
        
    #Desenha os círculos
    acad.model.AddCircle(APoint(ponto_ini.x + 60, ponto_ini.y + 5), 5)
    acad.model.AddCircle(APoint(ponto_ini.x + 120, ponto_ini.y + 5), 5)
        
    #Desenha o arco
    acad.model.AddArc(APoint(ponto_ini.x + 90, ponto_ini.y + 10), 30, 0, math.pi)
        
    #Desenha as fases
    if len(fases) > 1:
        acad.model.AddLine(APoint(ponto_ini.x + 80, ponto_ini.y + 25), APoint(ponto_ini.x + 80, ponto_ini.y + 55))        
        acad.model.AddLine(APoint(ponto_ini.x + 100, ponto_ini.y + 25), APoint(ponto_ini.x + 100, ponto_ini.y + 55))
        
    if len(fases) != 2:
        acad.model.AddLine(APoint(ponto_ini.x + 90, ponto_ini.y + 25), APoint(ponto_ini.x + 90, ponto_ini.y + 55))
        
    #Textos
    acad.model.AddText('%s' % nmr_circuito, APoint(ponto_ini.x + 335, ponto_ini.y), 10)
    acad.model.AddText('%s mm^2' % bitola_fio, APoint(ponto_ini.x + 215, ponto_ini.y + 15), 10)
    acad.model.AddText('%s A' % disjuntor, APoint(ponto_ini.x + 80, ponto_ini.y - 15), 10)
    acad.model.AddText('%s' % fases, APoint(ponto_ini.x - 30, ponto_ini.y), 10)     


# Cria uma instância do autocad e seleciona o desenho que está aberto
acad = Autocad()
print (acad.doc.Name)


proj_dictionary = [{
    'Nmr_circuito' : '1',
    'Bitola' : '2,5',
    'Fases' : 'RS',
    'Disjuntor' : '20'
}, {
    'Nmr_circuito' : '1',
    'Bitola' : '2,5',
    'Fases' : 'RS',
    'Disjuntor' : '20'
}]

#proj_dictionary = {
#    'Nmr_circuito' : '1',
#    'Bitola' : '2,5',
#    'Fases' : 'RS',
#    'Disjuntor' : '20'
#}
#proj_el = [[1, "2,5", "RS", "20"], [2, "2,5", "ST", "15"], [3, "4", "RST", "25"], [4, "6", "RS", "50"], [5, "1,5", "T", "10"], [6, "2,5", "RT", "15"], [7, "4", "RT", "15"]]

ponto_ini = APoint(0, 0)
total_circ = 2
#total_circ = len(proj_el) 

#Desenha o perímetro do diagrama.  perimetro_diagrama(ponto_ini, qtd de circuitos, qtd de fases, str do disjuntor)
perimetro_diagrama(ponto_ini, total_circ + 2, 3, "70")

#Desenha todas as linahs do diagrama dentro de um array. O Array usado não é final. 
for i in range(0,total_circ):
    #linha_diagrama(ponto_ini, nmr do circuito, bitola fio, str-fases, str-disjuntor)
    linha_diagrama(APoint(ponto_ini.x + 60, ponto_ini.y - 90 - 90 * (i+1)), proj_dictionary['Nmr_circuito'][i], proj_dictionary['Bitola'][i], proj_dictionary['Fases'][i], proj_dictionary['Disjuntor'][i])

i += 1
acad.model.AddLine(APoint(ponto_ini.x + 60, ponto_ini.y - 90 - 90 * (i+1)), APoint(ponto_ini.x + 380, ponto_ini.y - 90 - 90 * (i+1)))
acad.model.AddText('Reserva', APoint(ponto_ini.x + 385, ponto_ini.y - 90 - 90 * (i+1)), 10)

i += 1
acad.model.AddLine(APoint(ponto_ini.x + 60, ponto_ini.y - 90 - 90 * (i+1)), APoint(ponto_ini.x + 380, ponto_ini.y - 90 - 90 * (i+1)))
acad.model.AddText('Reserva', APoint(ponto_ini.x + 385, ponto_ini.y - 90 - 90 * (i+1)), 10)