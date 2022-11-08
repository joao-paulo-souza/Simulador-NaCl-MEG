from constantes import bin_min, bin_max, tern_min, tern_max
from constantes import PMsal, PMagua, PMmeg
from modelos import densid, Solub
from scipy.optimize import newton
#from mistura import saturacao, v_massica, peso_molar
#from mistura import particao_vmassica, calc_Cs
from calculos import definido_xsal, vapor_dagua


# Equacao Cs = xsal*rho quando temos uma relacao Xmeg = f(xsal)
# Pode usar para obter xsal
def equacao2(Cs, T, xsal, Xmeg, dXmeg):

	f0 = xsal
	f1, df1x, df1y = densid(T, Xmeg, xsal)
	
	df0 = 1.
	df1 = df1x + dXmeg*df1y

	funcao = f0*f1*1.e3 - Cs
	derivada = df0*f1*1.e3 + df1*f0*1.e3

	return funcao, derivada


# Equacao S(Xmeg) - modelo_de_S(Xmeg, T) = 0
# Pode usar para obter Xmeg
# S(Xmeg) é uma expressão que relaciona a Molalidade_sat e Xmeg, 
# servindo como restricao
def equacao3(fXmeg, dfXmeg, Xmeg, T):
	
	# fXmeg representa o S(Xmeg), na escala peso/peso (g/g, kg/kg etc...)
	# dfXmeg representa a derivada de fXmeg em relacao a Xmeg
	f1, df1 = fXmeg, dfXmeg
	f2, df2 = Solub(T, Xmeg)

	funcao = f1 - f2*1.e-6
	derivada = df1 - df2*1.e-6

	return funcao, derivada


# Limites de atribuição para variáveis
def limites(Xmeg, xmeg, xsal):

	R = xmeg/xsal
	Xm_min = Xmeg
	xsal_min = xsal
	print('R: {:.4f}'.format(R))

	# Esses dois primeiros "if"s sao provisorios.
	# Necessario controlar os valores definidos
	if R > 9998.:
		R = 9998.

	if R < 1.0003e-4:
		R = 1.0003e-4
	
	Xm_final = tern_max/(1.-tern_max)*R

	# limites para definir Xm ou xsal.
	if R > 0.9999 and R <= 9998.:
		#xsal_min = tern_min
		#Xm_min = xsal_min/(1.-xsal_min)*R
		Xm_max = bin_max
		xsal_max = Xm_max/(R + Xm_max)

	elif Xm_final < bin_max:
		Xm_max = Xm_final
		#Xm_min = bin_min
		#xsal_min = Xm_min/(R + Xm_min)
		xsal_max = tern_max

	else:
		Xm_max = bin_max
		#Xm_min = bin_min
		#xsal_min = Xm_min/(R + Xm_min)
		xsal_max = Xm_max/(R + Xm_max)


	return [[round(Xm_min, 4), round(Xm_max, 4)],
	        [round(xsal_min, 4), round(xsal_max, 4)]]


# Balanço de massa para Xm conhecido na corrente de saida
def balanco_evap_atm(T, Xmeg, xmeg_entrada, xagua_entrada,
                     xsal_entrada, vazaomassa_entrada):
	
	R = xmeg_entrada/xsal_entrada
	xsal = Xmeg/(R + Xmeg)

	L = xsal_entrada*vazaomassa_entrada/xsal
	V = vazaomassa_entrada - L

	respL = definido_xsal(T, Xmeg, xsal, L)
	respV = vapor_dagua(T, V)

	return respV, respL


def verifica(T, Cs, vazaomeg, vazaoagua, vazaosal):
	
	R = vazaomeg/vazaosal
	xsal_entrada = vazaosal/(vazaomeg + vazaoagua + vazaosal)

	xsal = newton(
		    func=lambda x: equacao2(Cs, T, x, x/(1.-x)*R, R/(1.-x)**2)[0],
			x0=xsal_entrada,
			fprime=lambda x: equacao2(Cs, T, x, x/(1.-x)*R, R/(1.-x)**2)[1],
			maxiter=1000)

	return xsal
