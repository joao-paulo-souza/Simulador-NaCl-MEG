direita = 'direita'
esquerda = 'esquerda'
cima = 'cima'
baixo = 'baixo'

horizontal = 'horizontal'
vertical = 'vertical'

norte = 'norte'
sul = 'sul'
leste = 'leste'
oeste = 'oeste'
ne = 'ne'
no = 'no'
se = 'se'
so = 'so'

esquerda1 = 'esquerda1'
esquerda2 = 'esquerda2'
esquerda3 = 'esquerda3'
esquerda4 = 'esquerda4'
esquerda5 = 'esquerda5'
direita1 = 'direita1'
direita2 = 'direita2'
direita3 = 'direita3'
direita4 = 'direita4'
direita5 = 'direita5'

entrada = 'entrada'
saida = 'saida'

#pasta = 'C:\\Users\\Documents\\Local\\'
#pasta = '/home/Nome/Documentos/Local/'
pasta = './'

titulo = 'Processo de Regeneração do Monoetileno Glicol (MEG)'

prop_list = [
    
    # temperatura, pressao, fracao MEG isento de sal
    # concentracao de sal base solvente, vazao massica
    'temp', 'pres', 'megFrac', 'salConc', 'flow',

    # vazoes massicas
    'vazMasMEG', 'vazMasAgua', 'vazMasSal',  'vazMasSalSoli', 'vazMasSalSolub', 

    # vazoes molares
    'vazMolMEG', 'vazMolAgua', 'vazMolSal', 'vazMolSalSoli', 'vazMolSalSolub', 'vazMolTotal',

    # densidade, v. volumetrica, solubilidade
    # concentracoes de saturacao, atual ou total, sal dissolvido ou solubilizado
    'dens', 'vazVol', 'solubNaCl', 'concSalSaturado', 'concSalSoli', 'concSalSolub',
    'pesoMolMedio', # Peso molar médio

    # fracoes massicas
    'fracMasMEG', 'fracMasAgua', 'fracMasSal', 'fracMasSalSoli', 'fracMasSalSolub', 

    # fracoes molares
    'fracMolMEG', 'fracMolAgua', 'fracMolSal', 'fracMolSalSoli', 'fracMolSalSolub'
    ]

stream_props = [
    # [propriedade, texto, formato]
    ['temp', 'Temperatura (\u00B0C)', '.1f'],
    ['pres', 'Pressão (kPa)', '.1f'],
    ['megFrac', 'MEG (% m/m livre de sal)', '.2f'],
    ['salConc', '[NaCl] (mg/kg solv.)', '.0f'],
    ['flow', 'Vazão mássica (kg/h)', '.2f'],
    ['vazMasMEG', 'Vazão MEG (kg/h)', '.2f'],
    ['vazMasAgua', 'Vazão água (kg/h)', '.2f'],
    ['vazMasSal', 'Vazão NaCl (kg/h)', '.2f'],
    ['vazMasSalSolub', 'Vazão NaCl dissolvido (kg/h)', '.2f'],
    ['vazMasSalSoli', 'Vazão NaCl sólido (kg/h)', '.2f'],
    ['concSalSaturado', '[NaCl] na saturação (mg/kg solv.)', '.0f'],
    ['concSalSolub', '[NaCl] dissolvido (mg/kg solv.)', '.0f'],
    ['concSalSoli', '[NaCl] sólido (mg/kg solv.)', '.0f'],
    ['pesoMolMedio', 'Peso molecular médio (kg/kmol)', '.2f']
    ]

texto = {}
formato = {}
tela_props = []
for item in stream_props:
    tela_props.append(item[0])
    texto[item[0]] = item[1]
    formato[item[0]] = item[2]

cabecalho = ['Corrente 1', 'Corrente 2', 'Corrente 3', 'Corrente 4',
                'Corrente 5', 'Corrente 6', 'Corrente 7', 'Corrente 8']