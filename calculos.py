from constantes import PMsal, PMagua, PMmeg
from mistura import fracao_massa, saturacao, v_massica, particao_Cs
from mistura import peso_molar, particao_vmassica, calc_Cs
#from modelos import prop_vapor, prop_liquido_mix, prop_vapor_mix


# Funcao que calcula as demais variaveis da corrente
def definido_Cs(T, Xmeg, Cs, vazaomass):

	# Calculo de parametros na condicao de saturacao
	xsal_sat, xmeg_sat, Cs_sat = saturacao(T, Xmeg)
	
	Cs_diss, Cs_solido = particao_Cs(Cs, Cs_sat)

	# Fracao massica de agua em base de mistura
	xsal, xmeg, xagua = fracao_massa(Cs, Xmeg)

	# Massa molar (ou molecular) media
	PMmedio = peso_molar(xsal, xmeg, xagua)

	# Variaveis Extensivas
	### Vazoes massicas dos componentes, em kg/h
	vazaomeg, vazaosal, vazaoagua = v_massica(vazaomass, xmeg, xsal)
	vazaosal_solido, vazaosal_diss = particao_vmassica(vazaomass,
	                                	Cs_solido, vazaosal)

	prop_calc = {
		'fracMasMEG':xmeg, 
		'fracMasAgua':xagua, 
		'fracMasSal':xsal,
		'concSalSaturado':Cs_sat,
		'concSalSolub':Cs_diss,
		'concSalSoli':Cs_solido,
		'pesoMolMedio':PMmedio, 
		'megFrac':Xmeg, 
		'salConc':Cs,
		'vazMasMEG':vazaomeg, 
		'vazMasAgua':vazaoagua, 
		'vazMasSal':vazaosal, 
		'vazMasSalSolub':vazaosal_diss, 
		'vazMasSalSoli':vazaosal_solido, 
		'flow':vazaomass}

	return prop_calc


def definido_xsal(T, Xmeg, xsal, vazaomass):

	xmeg = Xmeg*(1. - xsal)
	xagua = 1.0 - round(xmeg, 4) - round(xsal, 4)
	
	Cs, Cs_solido, Cs_diss, Cs_sat = calc_Cs(T, Xmeg, xsal)
	PMmedio = peso_molar(xsal, xmeg, xagua)

	vazaomeg, vazaosal, vazaoagua = v_massica(vazaomass, xmeg, xsal)
	vazaosal_solido, vazaosal_diss = particao_vmassica(vazaomass,
	                                    Cs_solido, vazaosal)

	prop_calc = {
		'fracMasMEG':xmeg, 
		'fracMasAgua':xagua, 
		'fracMasSal':xsal,
		'concSalSaturado':Cs_sat,
		'concSalSolub':Cs_diss,
		'concSalSoli':Cs_solido,
		'pesoMolMedio':PMmedio, 
		'megFrac':Xmeg, 
		'salConc':Cs,
		'vazMasMEG':vazaomeg, 
		'vazMasAgua':vazaoagua, 
		'vazMasSal':vazaosal, 
		'vazMasSalSolub':vazaosal_diss, 
		'vazMasSalSoli':vazaosal_solido, 
		'flow':vazaomass}

	return prop_calc


def vapor_dagua(T, vazaomass):
	xsal, xmeg, xagua = 0., 0., 1.
	Cs, Cs_sat, Cs_solido, Cs_diss = 0, 0, 0, 0
	Xmeg = 0.

	vazaomeg, vazaosal, vazaoagua = 0., 0., vazaomass
	vazaosal_solido, vazaosal_diss = 0., 0.

	PMmedio = PMagua

	prop_calc = {
		'fracMasMEG':xmeg, 
		'fracMasAgua':xagua, 
		'fracMasSal':xsal,
		'concSalSaturado':Cs_sat,
		'concSalSolub':Cs_diss,
		'concSalSoli':Cs_solido,
		'pesoMolMedio':PMmedio, 
		'megFrac':Xmeg, 
		'salConc':Cs,
		'vazMasMEG':vazaomeg, 
		'vazMasAgua':vazaoagua, 
		'vazMasSal':vazaosal, 
		'vazMasSalSolub':vazaosal_diss, 
		'vazMasSalSoli':vazaosal_solido, 
		'flow':vazaomass}

	return prop_calc


def vapor_mix(T, Xmeg, vazaomass):

	# no sistema binario agua-MEG, o Xmeg = xmeg
	xmeg = Xmeg
	xagua = 1. - xmeg
	xsal = 0.
	Cs, Cs_sat, Cs_solido, Cs_diss = 0, 0, 0, 0
	
	vazaomeg, vazaosal, vazaoagua = v_massica(vazaomass, xmeg, xsal)
	vazaosal_solido, vazaosal_diss = 0., 0.

	PMmedio = peso_molar(xsal, xmeg, xagua)

	prop_calc = {
		'fracMasMEG':xmeg, 
		'fracMasAgua':xagua, 
		'fracMasSal':xsal,
		'concSalSaturado':Cs_sat,
		'concSalSolub':Cs_diss,
		'concSalSoli':Cs_solido,
		'pesoMolMedio':PMmedio, 
		'megFrac':Xmeg, 
		'salConc':Cs,
		'vazMasMEG':vazaomeg, 
		'vazMasAgua':vazaoagua, 
		'vazMasSal':vazaosal, 
		'vazMasSalSolub':vazaosal_diss, 
		'vazMasSalSoli':vazaosal_solido, 
		'flow':vazaomass}

	return prop_calc


def liquido_mix(T, Xmeg, vazaomass):

	# no sistema binario agua-MEG, o Xmeg = xmeg
	xmeg = Xmeg
	xagua = 1. - xmeg
	xsal = 0.

	Cs, Cs_sat, Cs_solido, Cs_diss = 0, 0, 0, 0

	vazaomeg, vazaosal, vazaoagua = v_massica(vazaomass, xmeg, xsal)
	vazaosal_solido, vazaosal_diss = 0., 0.

	PMmedio = peso_molar(xsal, xmeg, xagua)

	# Organizando as respostas em listas
	### Fracoes massicas
	fracmass = [xmeg, xagua, xsal]

	### Propriedades da mistura
	propriedades = [Cs_sat, Cs_diss, Cs_solido, PMmedio, Xmeg, Cs]

	### Vazoes massicas
	vmass = [vazaomeg, vazaoagua, vazaosal, vazaosal_diss, 
			 vazaosal_solido, vazaomass]

	return fracmass, propriedades, vmass