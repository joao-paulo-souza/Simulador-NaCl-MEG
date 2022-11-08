from math import exp
from constantes import PMsal, PMagua, PMmeg
import numpy as np

# Modelos

# Função que calcula a solubilidade do NaCl
def Solub (T, Xmeg):

	# Parametros do modelo
	a0 = 1.7740
	a1 = 1.2808E-01
	a2 = -3.2007
	a3 = 1.6515
	a4 = 2.2081E-01
	a5 = -4.2666E-01

	# Faixa de temperatura em Celsius
	Tmin = 20.0
	Tmax = 130.0

	# Temperatura em escala codificada de 0.0 a 1.0
	Tcod = (T-Tmin)/(Tmax-Tmin)

	# Fracao molar MEG isento de sal e sua derivada em relacao a Xmeg
	# Utilizado em escala molar em concordância com o modelo
	XMmeg = (Xmeg/PMmeg)/(Xmeg/PMmeg+(1-Xmeg)/PMagua)
	#dXMmeg = PMagua*PMmeg/(Xmeg*(PMagua - PMmeg) + PMmeg)
	
	# Solubilidade em mol/kg solv. de acordo com o modelo de regressao, e 
	# sua derivada parcial em relacao Xmeg
	Smodel = exp(a0 + a1*Tcod + a2*XMmeg + a3*XMmeg**2. + a4*Tcod*XMmeg + \
		     a5*Tcod*XMmeg**2.)
	#dSmodel = Smodel*(a2 + 2.*a3*XMmeg + a4*Tcod + 2.*a5*Tcod*XMmeg)*dXMmeg

	# Solubilidade em mg/kg solv. e sua derivada parcial em relacao Xmeg
	S = Smodel*PMsal*1000.0
	#dS = dSmodel*PMsal*1000.0

	return S

# Funcao que calcula a densidade da solução Agua/MEG/Sal
def densid (T, Xmeg, xsal):

	# Referência do modelo:
	# Adriano R. C. Silva; Osvaldo Chiavone-Filho; Dannielle J. da Silva; 
	# Leonardo S. Pereira; Jailton F. Nascimento
	# DETERMINAÇÃO DA COMPOSIÇÃO DE MONOETILENOGLICOL, CLORETO DE SÓDIO E 
	# ÁGUA A PARTIR DE MEDIDAS DE DENSIDADE E CONDUTIVIDADE DO SEPARADOR 
	# FLASH - XXI COREEQ - USP

	a0 = 1.010623
	a1 = 0.142471
	a2 = -0.033072
	a3 = 0.699980
	a4 = 0.207362
	a5 = -4.32E-4
	a6 = -2.0E-6

	# densidade em kg/m3
	densidade = (a0 + a1*Xmeg*(1-xsal) + a2*(Xmeg*(1-xsal))**2 + a3*xsal + \
		         a4*xsal**2 + a5*T + a6*T**2)*1000.0

	# derivada parcial em relacao a xsal
	d_xsal = (-a1*Xmeg - 2*a2*Xmeg**2 + 2*a2*Xmeg**2*xsal +\
		      a3 + 2*a4*xsal)*1000.

	# derivada parcial em relacao a Xmeg
	d_Xmeg = (a1*(1-xsal) + 2*Xmeg*a2*(1-xsal)**2)*1000.

	# Esta função retorna uma tupla com a densidade (indice [0]) e suas 
	# derivadas parciais (indice [1] e [2]).
	# A derivada sera utilizada para determinar xsal (com metodo numerico), 
	# no caso do sistema abaixo da saturacao
	# Tambem sera utilizada para calcular xsal na saida do evaporador 
	# atmosferico quando usuario definir a concentracao
	return densidade, d_xsal, d_Xmeg

# Funcao que calcula a densidade do sal sólido em kg/m3
def densid_sal (T):
	
	# Referência sal sólido:
	# https://pubchem.ncbi.nlm.nih.gov/compound/sodium_chloride#section=Top
	# Acesso em 10/09/18
	# Pubchem - Open Chemistry Database
	# Compound Summary for CID 5234 - Sodium chloride
	# densidade relativa de 2.17 a 25°/4°C

	# Referência sal líquido:
	# http://www.ddbst.com/en/EED/PCP/DEN_C4911.php
	# Acesso em 10/09/18
	# Dortmund Data Bank - Density of Sodium chloride
	# Dados apenas para líquido a partir de 817 °C, que é de 1.541,00 kg/m3.

	# Considerações para densidade constante nessa aplicação:
	# - a densidade não varia significativamente em quanto sólido
	# a pressões moderadas.
	# - a temperatura de operação está longe de 817 °C

	# densidade em kg/m3	
	densidade = 2170.0

	return densidade

# Funcao que calcula a densidade da mistura saturada e sal solido
def densid_susp(T, Cs, Cs_sat, rho_sat):

	# fracao em volume da solucao saturada
	frac_vol_sat = (densid_sal(T) - Cs*1.e-3)/(densid_sal(T) - Cs_sat*1.e-3)

	## Base de calculo 1.0 L de mistura
	Vsol_sat = frac_vol_sat*1.0

	msol_sat = Vsol_sat*rho_sat*1.0E3
	msal_diss = Cs_sat*Vsol_sat
	#msolvente = msol_sat - msal_diss
	msal = Cs*1.0
	msal_solido = msal - msal_diss

	#print(msal_solido + msol_sat)
	#print(msal + msolvente)

	rho = (msal_solido + msol_sat)/1.0 * 1.0E-3

	Cs_solido = int(msal_solido/1.0)
	Cs_diss = int(msal_diss/1.0)

	return rho, Cs_solido, Cs_diss

def prop_vapor(T):

	# densidade kg/m3 --- inserir um modelo
	rho = 1.0

	return rho

def prop_vapor_mix(T, Xmeg):

	# densidade kg/m3 --- inserir um modelo
	rho = 1.0

	return rho

def prop_liquido_mix(T, Xmeg):

	# densidade kg/m3 --- inserir um modelo
	rho = 1.0

	return rho

