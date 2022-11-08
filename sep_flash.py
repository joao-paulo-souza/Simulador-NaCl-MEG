from constantes import bin_min, bin_max, tern_min, tern_max
from calculos import definido_xsal, vapor_mix, liquido_mix, definido_Cs

# balanco de massa
def balanco_sep_flash(Tvap, Tbase, entrada, Xmeg_vapor, fator_evaporacao):
    
    xmeg_entrada, xsal_entrada, vazao_entrada = entrada
    
    # na mistura binaria, Xmeg = xmeg
    xmeg_vapor = Xmeg_vapor

    vazao_vapor = fator_evaporacao*vazao_entrada*(1. - xsal_entrada)
    vazao_salmoura = vazao_entrada - vazao_vapor

    xsal_salmoura = xsal_entrada*vazao_entrada/vazao_salmoura
    xmeg_salmoura = (xmeg_entrada*vazao_entrada - \
                     xmeg_vapor*vazao_vapor)/vazao_salmoura
    Xmeg_salmoura = xmeg_salmoura/(1. - xsal_salmoura)

    Cs = xsal_salmoura/(1. - xsal_salmoura)*1.E6

    resp_base = definido_Cs(Tbase, Xmeg_salmoura, Cs, vazao_salmoura)
    resp_vapor = vapor_mix(Tvap, Xmeg_vapor, vazao_vapor)

    return resp_vapor, resp_base

def limites_vazao_salmoura(xsal_entrada, vazaomassa_entrada):

    limite1 = xsal_entrada*vazaomassa_entrada/bin_max
    limite2 = vazaomassa_entrada - 0.01 

    return limite1, limite2

def limites_Xmeg_salmoura(Xmeg_entrada, xsal_entrada, vazaomassa_entrada,
                          Xmeg_vapor, vazao_salmoura):

    # calcula os valores limites que podem ser atribuidos/definidos pelo 
    # usuario para Xmeg_salmoura

    xmeg_entrada = Xmeg_entrada*(1. - xsal_entrada)
    xsal_salmoura = vazaomassa_entrada*xsal_entrada / vazao_salmoura

    xmeg_vapor = Xmeg_vapor
    a = min(xmeg_entrada, xmeg_vapor)
    b = (vazaomassa_entrada*(xmeg_entrada - xmeg_vapor) + \
         vazao_salmoura*xmeg_vapor)/vazao_salmoura

    if b < a:
        lim = 0., b/(1. - xsal_salmoura)
    else:
        lim = 0., a/(1. - xsal_salmoura) - 0.0001

    return lim

def limites_Xmeg_condensado(Xmeg_entrada, xsal_entrada, vazaomassa_entrada, 
                            Xmeg_salmoura, vazao_salmoura, Xmeg_vapor):
    
    # calcula os valores limites que podem ser atribuidos/definidos pelo 
    # usuario para Xmeg_condensado

    xsal_salmoura = vazaomassa_entrada*xsal_entrada / vazao_salmoura
    xmeg_salmoura = Xmeg_salmoura*(1. - xsal_salmoura)
    xmeg_entrada = Xmeg_entrada*(1. - xsal_entrada)

    # na mistura binaria, Xmeg = xmeg
    xmeg_vapor = Xmeg_vapor
    a = (xmeg_entrada*vazaomassa_entrada - \
         xmeg_salmoura*vazao_salmoura)/(vazaomassa_entrada - vazao_salmoura)
    
    return 0., min(a, xmeg_entrada, xmeg_vapor) - 0.0001

