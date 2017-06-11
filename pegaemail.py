########################################
##Feito por: Eduardo C.B da Silva 	  ##
##Contato: eduardocodigo0@gmail.com   ##
##Feito em: python 2.7.13             ##
########################################





#importando bibliotecas
import requests	#biblioteca para requisicoes
import os		#biblioteca para ser possivel dar comandos ao sistema operacional
import re 		#biblioteca para exprecoes regulares

#Cria arquivo que vai conter os e-mails
emailLista = open('email.txt', 'w')
emailLista.close()

#Metodo responsavel por gravar os e-mails capturados no arquivo emails.txt
def salvaEmail(e ):
	
	e = e.encode("utf8") #necessario converter para conseguir salvar

	email = e

	emailLista = open('email.txt', 'r')	#abre o arquivo modo leitura
	emailnovo = emailLista.readlines()   	#passa o conteudo a varivael
	emailnovo.append(email)					#adiciona uma nova linha com a informacao nova						
	emailLista = open('email.txt', 'w')	#abre o arquivo modo escrita
	emailLista.writelines(emailnovo)		#escreve o informacao nova no arquivo
	emailLista.writelines("\n")				#escreve uma quebra de linha no arquivo
	emailLista.close()						#fecha o arquivo

#metodo responsavel por acessar o site e retornar seu conteudo
def acessaSite(url):
	try:
		r = requests.get(url)	#faz requisicao a uma pagina pelo metodo get
		return r.text			#retorna o conteudo da pagina como uma string
	except:
		return"Erro ao acessar o link, verifique sua url"



def procuraEmail(site):
	padraoEmail = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', site) #usa esprecao regular para encontrar e-mails no site

	for i in padraoEmail: 	#faz loop na lista de e-mails que e gerada
		salvaEmail(i)		#envia o e-mail para ser salvo
		print i

os.system("cls")	#limpa a tela
print"Feito por: Cod23"
print"##############################################"
print"###### Seja bem vindo ao pega e-mail! ########"
print"##############################################"
print""
print""

while(True):	#loop infinito
	endereco = raw_input("Insira o link: ") #local onde deve ser inserido o link
	site = acessaSite(endereco)				#chama metodo acessaSite enviando link como parametro

	
	print""
	print"E-mails encontrados em: "+ endereco
	print""
	procuraEmail(site)		#chama metodo procura email usando conteudo do site como parametro

	padraoURL = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', site) #pesquisa no site usando esprecao regular que busca por url

	for i in padraoURL: #Loop que manda as URLs encontradas para o metodo procura email
		print""
		print"E-mails encontrados em: "+ i
		print""
		procuraEmail(acessaSite(i))

	print"Processo finalizado..."
	print""
	continua = raw_input("Fazer nova busca? Sim(Y) Nao(N)") 
	if(continua == "Y" or continua =="y"):
		os.system("cls")
		print""
	else:
		break
os.system("pause") #fim 

