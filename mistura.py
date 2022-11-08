from modelos import densid_sal, densid, Solub #, densid_susp
#from scipy import optimize
from constantes import PMsal, PMagua, PMmeg

# Calcula algumas propriedades da mistura

def fracao_massa(Cs, Xmeg):
	# Fracoes massicas
	# Base de calculo: 1,0 kg de solvente

	massa_sal = Cs*1.0*1.0E-6
	massa_meg = Xmeg*1.0
	massa = massa_sal + 1.0
	xsal = massa_sal/massa
	xmeg = massa_meg/massa
	xagua = round(1.0 - xsal - xmeg, 4)

	return xsal, xmeg, xagua


def v_massica(vazaomass, xmeg, xsal):
	### Vazoes massicas dos componentes, em kg/h
	vazaomeg = vazaomass*xmeg
	vazaosal = vazaomass*xsal
	vazaoagua = vazaomass - vazaomeg - vazaosal
	return vazaomeg, vazaosal, vazaoagua


def peso_molar(xsal, xmeg, xagua):
	# Massa molar (ou molecular) media
	# Base de cálculo: 1,0 kg de mistura.
	### Total molar de mistura, de acordo com a base de calculo, em kmol
	mol = xsal/PMsal + xmeg/PMmeg + xagua/PMagua
	return 1.0/mol

def particao_vmassica(vazaomass, Csal_solido, vazaosal):
	### Particao de sal solido e dissolvido, em kg/h
	vazaosal_solido = Csal_solido*(vazaomass - vazaosal)*1.0E-6
	vazaosal_diss = vazaosal - vazaosal_solido
	return vazaosal_solido, vazaosal_diss

# Funcao utilizada para estimar xsal quando abaixo da saturacao
# Retorna o valor de xsal*rho - Cs (e sua derivada em relacao a xsal)
def equacao(Cs, T, Xmeg, xsal):
	rho, drho = densid(T, Xmeg, xsal)[0:2]
	funcao = xsal*rho*1.e3 - Cs
	derivada = rho*1.e3 + xsal*drho*1.e3
	return funcao, derivada

# Funcao que calcula algumas variaveis na saturacao, com base 
# na solubilidade
def saturacao(T, Xmeg):

	# Fracoes massica e molar de MEG, ambas em base livre de sal
	Cs_sat = Solub(T, Xmeg)

	### Solubilidade em peso/peso (kg/kg ou g/g etc.)
	Speso = Cs_sat*1.0E-6

	### Fracao massica de sal e MEG na saturacao 
	xsal_sat = Speso/(Speso + 1.0)
	xmeg_sat = Xmeg*(1.0 - xsal_sat)

	return xsal_sat, xmeg_sat, Cs_sat
	

def xsal_maior(xsal, xsal_sat, Xmeg, T, rho_sat):

	# Base de calculo: 1.0 kg de solucao saturada
	m_sat = 1.0
	V_sat = m_sat/rho_sat
	msal_solid = m_sat*(xsal - xsal_sat)/(1. - xsal)
	Vsal_solid = msal_solid/densid_sal(T)

	rho = (m_sat + msal_solid)/(V_sat + Vsal_solid)

	return rho

# Funcao que calcula a concentracao de sal
def calc_Cs(T, Xmeg, xsal):

	# base de calculo: 1,0 kg de mistura
	#
	massa_sal = 1.0*xsal
	Cs = int(massa_sal*1E6/(1.0 - massa_sal))
	xsal_sat, xmeg_sat, Cs_sat = saturacao(T, Xmeg)
	Cs_diss, Cs_solido = particao_Cs(Cs, Cs_sat)

	return Cs, Cs_solido, Cs_diss, Cs_sat

def particao_Cs(Cs, Cs_sat):

	if Cs > Cs_sat:
		# Sistema com excesso de sal. 
		# Considerado que o excesso está solido.
		Cs_diss = Cs_sat
		Cs_solido = Cs - Cs_diss
	else:
		# Solucao nao saturada ou saturada. Todo sal esta dissolvido.
		Cs_diss = Cs
		Cs_solido = 0
	
	return Cs_diss, Cs_solido
