from pandas import DataFrame as df
from constantes_tela import texto, tela_props, formato, cabecalho


def gerar_tabela(correntes):
	
	nomes = [texto[prop].ljust(35) for prop in tela_props]
	tab_txt = df(columns=['Propriedades'] + cabecalho)
	tab_txt['Propriedades'] = nomes

	for j, corrente in enumerate(correntes, start=1):
		
		dados_txt = []
		for prop in tela_props:
			dado = getattr(corrente, prop)
			if dado == '':
				dados_txt.append('-')
			else:
				dados_txt.append('{0:{1}}'.format(dado, formato[prop]))

		tab_txt.iloc[:, j] = dados_txt

	return tab_txt


def converter_tabela(tab_txt, tipo='txt'):

	if tipo == 'tex':
		observacao = '% Adicione o pacote \\usepackage{booktabs} \n'
		return observacao + tab_txt.to_latex(index=False)
	elif tipo == 'csv':
		return tab_txt.to_csv(sep=';', index=False, line_terminator='\n')
	else:
		col_space = [35] + [12]*8
		return tab_txt.to_string(index=False, justify='center', col_space=col_space)


def number_formatter(number, string_format):
	
	if (not type(number) is float) and (not type(number) is int):
		formated_number = ''
	else:
		formated_number = '{0:{1}}'.format(number, string_format)
	return formated_number

