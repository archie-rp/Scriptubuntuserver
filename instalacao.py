#! /usr/bin/env python
# coding=utf-8
#Includes
import os
import sys
#from termcolor import colored, cprint

#Program
#Escrever INFO
os.system("clear")
hostname = os.uname()[1]
username = os.environ['USER']
feito = ' Feito por ' + username + ' '
name = ' Utilizador ' + username + ' '
host = ' Maquina : ' + hostname + ' '
n =len(name)
h =len(host)
#Espaço dinamico para header
if n > h :
	e = n
else:
	e = h


# Variaveis
global m_Home
m_Home = '/home/' + username
pasta=os.getcwd()
linha =  "#"*e
sair = ""
i = 0
u = 0
erro = ""

#Funcoes

def ficheiro(nome):
	if not os.path.exists(nome):
		pass
	else:
		os.remove(nome)

def butil(u):
	lista=("cat /etc/passwd | grep '/home' | cut -d: -f1")
	os.system(lista + " >> .users.txt")
	users = open(pasta + '/' + '.users.txt', 'r+')
	users = users.read()
	ficheiro('.users.txt')
	utilizadores= users.split('\n')
	u=int(u)
	u=utilizadores[u]
	print (u)
	return u

def listusers():
	os.system("clear")
	print (linha)
	print("Utilizadores")
	print (linha)
	lista=("cat /etc/passwd | grep '/home' | cut -d: -f1")
	os.system(lista + " >> .users.txt")
	users = open(pasta + '/' + '.users.txt', 'r+')
	users = users.read()
	ficheiro('.users.txt')
	utilizadores= users.split('\n')
	print ('\nExistentes:')
	for u in range(len(utilizadores)):
		if utilizadores[u] == '':
			pass
		else:
			print (u,utilizadores[u])

def instalar(x):
	os.system("clear")
	print (linha)
	print ("Instalar pacotes: ")
	print (linha)
	print ("A installar :" + '"' + x+ '"')
	os.system('sudo apt-get install ' + x )
	teste=input("Concluido!!")
	pass

#Funcoes globais
ficheiro('.users.txt')
ficheiro('.apps.txt')
ficheiro('versao.txt')

#Programa
print ("Menu")
menu = ["Utilizadores","GitHub","Instalar Servidores('Squid', 'Webmin', 'SSH')","Configurar IPTABLES","Limpar Apps"]
os.system("clear")
while sair != "x":
	text = 'Ubuntu Server'
	print(text)
	print (linha)
	print (feito)
	print (name)
	print (host)
	print (linha)
	print ("Menu:")
	for i in range(len(menu)):
		print (i, menu[i])
	print ("\nx) Sair")
	i = (i + 1)
	print (erro)
	rsp=input('Opção: ')
	if rsp == "x":
		sair = "x"
	elif rsp == 0:
		os.system("clear")
		print(linha)
		listusers()
		print ("Gestor de Utilizadores:")
		print ('0' , 'Adicionar Utilizador')
		print ('1' , 'Remover Utilizador')
		print(linha)
		r = input('Selecionar:')
		if r==0:
			os.system('clear')
			print (linha)
			print ("Adicionar Utilizador: ")
			print (linha)
			utilizador=input('Nome:')
			os.system('sudo useradd -m -g users -G wheel,storage,video,audio,network -s /bin/bash ' + utilizador)
			print ("Password Utilizador: ")
			os.system('\nsudo passwd ' + utilizador)
			input("\nMenu principal <enter>")
		elif r==1:
			listusers()
			print (linha)
			print ("Remover Utilizador: ")
			print (linha)
			rsp=input('Número: ')
			os.system('sudo userdel -r ' + butil(rsp))
		else:
			pass
	elif rsp == 1:
		os.system("clear")
		print (linha)
		print ("GitHub: ")
		print (linha)
		instalar('xclip git')
		github_utilizador=input('\nGitHub Nome:')
		os.system('git config --global user.name ' + github_utilizador)
		github_email=input('GitHub Email:')
		os.system('git config --global user.email ' + github_email )
		input("Menu principal <enter>")
	elif rsp == 2:
		os.system("clear")
		servers=("webmin squid openssh-client openssh-server")
		print (linha)
		print ("Pacotes: " + servers )
		print (linha)
		dr=input('Instalar Servidores?''\n(s=1/n=0)')
		if dr == 1:
			#adicionar repositorio do webmin
			os.system("sudo echo 'deb http://download.webmin.com/download/repository sarge contrib' >> /etc/apt/sources.list")
			os.system("wget http://www.webmin.com/jcameron-key.asc && sudo apt-key add jcameron-key.asc");
			#Actualizar repositorios
			os.system('sudo apt-get update')
			instalar(servers)
	elif rsp == 3:
		os.system("clear")
		print (linha)
		print ("Configurar iptable: ")
		print (linha)
		print("O Seu ip de Servidor é :")
		os.system("hostname --ip-address")
		print("Placa de rede a ser utilizada é : 'enp0s3'")
		rss=input('Deseja bloquear "netbios" dentro da rede interna?(s=1/n=0)')
		if rss == 1:
			#bloquear porta 139 netbios
			os.system("sudo iptables -A INPUT  -p tcp --dport 139 -j DROP")
			os.system("sudo iptables -A INPUT  -p udp --dport 139 -j DROP")
		rss=input('Deseja bloquear "telnet" dentro da rede interna?(s=1/n=0)')
		if rss == 1:
			# bloquear porta 23 telnet
			os.system("sudo iptables -A INPUT  -p tcp --dport 23 -j DROP")
		rss=input('Deseja bloquear "FTP" dentro da rede interna?(s=1/n=0)')
		if rss == 1:
			# Bloquear acesso FTP
			os.system("sudo iptables -A INPUT  -p tcp --dport 20:21 -j DROP")
		rss=input('Deseja bloquear "Ips Publicos" dentro da rede interna?(s=1/n=0)')
		if rss == 1:
			#Bloquear acesso a IP Publicos
			os.system("sudo iptables -A INPUT  --src 192.168.0.0/16 -j DROP")
			os.system("sudo iptables -A INPUT  --src 172.16.0.0/12 -j DROP")
			os.system("sudo iptables -A INPUT  --src 10.0.0.0/8 -j DROP")
		rss=input('Dar acesso "Porta 80 (http)" dentro da rede interna?(s=1/n=0)')
		if rss == 1:
			#Aceita porta 80 http
			os.system("sudo iptables -A INPUT  -p tcp --dport 80 -j DROP")
		rss=input('Dar acesso "Porta 443 (https)" dentro da rede interna?(s=1/n=0)')
		if rss == 1:
			#Aceita porta 443 https
			os.system("sudo iptables -A INPUT  -p tcp --dport 443 -j DROP")
		rss=input('Ver todas as regras definidas?(s=1/n=0)')
		if rss == 1:
			os.system("sudo iptables -S")
		input("Menu principal <enter>")
	else:
		erro = 'Opção não válida'
	os.system("clear")
