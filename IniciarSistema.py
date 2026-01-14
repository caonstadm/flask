'''
#-------------------------------------------------------------------------------
# Name:        Drv_on.py
# Purpose:
#
# Author:      Celso Abreu
#
# Created:     12/03/2023
# Copyright:   (c) CA_ON 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python  '''

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from objgr.libspadrao import PlotlyChart, ip_local, Nominatim, geocoder, data_e_hora_atuais, \
sqlite3, conn, sha256, px, go, os, socket, validate, datetime, sleep

import flet as ft
from flet import * 
import pdfkit

from flet_route import Params,Basket

#engine = create_engine("sqlite:///cadbdrv.sqlite")

#from Val_cpf import validate

import mysql.connector

db = SQLAlchemy()

# Configuração de conexao para execução de comandos SQL
import sqlite3

print("Inicializando o sistema...!")


def handle_position_change(e):
	page.add(ft.Text(f"New position: {e.latitude} {e.longitude}"))
	gorig_lat = e.latitude
	gorig_lng = e.longitude

#gl = Geolocator(GeolocatorPositionAccuracy.BEST)
#print(type(gl),gl.get_current_position_async([0]),gl.get_current_position_async([1]))
#if gl:
#	p = gl.get_current_position_async()
#	gorig_lat = gl.get_current_position_async([0])
#	gorig_lng = gl.get_current_position_async([1])
#else:
gorig_lat = -12.9356309
gorig_lng = -38.3395556

print("GetCurrentPosition:", gorig_lat, gorig_lng)
geolocator = Nominatim(user_agent="vemail")
#geolocator = Nominatim(user_agent="myGeocoder")
location = geolocator.reverse(str(gorig_lat) + "," + str(gorig_lng))
#   print("distancia:", dist, location2.raw )
print("DADOS DO LSTCANDID")
print(location.raw['address'])
print("---------------------------------------------------------------------------")
print(location.raw)
print("Place:",location.raw["address"].get('place_id'))
print("End:", location.raw["address"].get('residential'))
print("Nr:", location.raw.get("place_rank"))
print("Bairro:", location.raw["address"].get('suburb'))
print("Cidade:", location.raw["address"].get('city'))
print("Estado:", location.raw["address"].get('state'))
print("Cod. Estado:", location.raw["address"].get('ISO3166-2-lvl4'))
print("Municipio:", location.raw["address"].get('city_district'))
print("CEP:", location.raw["address"].get('postcode'))
print("Pais:", location.raw["address"].get('country'))
print("Cod.Pais:", location.raw["address"].get('country_code'))
print("Pais:", location.raw.get("country"))
print("Regiao:", location.raw["address"].get('region'))
print("DisplayName:", location.raw.get('display_name'))
#
vpais     = location.raw["address"].get('country')
vuf       = location.raw["address"].get('state')
vnr       = location.raw.get("place_rank")
vcidade   = location.raw["address"].get('city')
vbairro   = location.raw["address"].get('suburb')
vendereco = location.raw["address"].get('residential')
vcep      = location.raw["address"].get('postcode')
vcod_mun  = location.raw["address"].get('place_id')
vregiao   = location.raw["address"].get('region')
#location = geolocator.geocode("1600 Pennsylvania Ave NW, Washington, DC 20500")
vnome    	= "Administrador"
vuser    	= "Adm"
vfirst_name = "Adm"
vlast_name 	= "Sistems"
vemail   	= "caonst.contact@gmail.com"
vcelular 	= "5571991092626"
vcpf     	= "203.688.250-19"
if vcpf == "":
	print("CPF invalido!")
else:
	print("CPF:", vcpf)
	obj_cpf = validate(vcpf)
	print("OBJCPF:", obj_cpf)
if obj_cpf == True:
	print("CPF Correto !!!", obj_cpf)
else:
	print("Erro CPF invalido !")
vdt_nasc 	= "01/01/2023"
vstatus  	= "A" #request.form.get('status')
vtipo   	= "*" #request.form.get('tipo')
vdatacr     = data_e_hora_atuais
vip 		= ip_local
vfoto 		= "fotousu/ca.jpg"
vautentic   = True
vsenha   = "123456"
vcsenha  = "123456"
vid_usu = 1
if (vsenha == vcsenha):
	#vsenha   = generate_password_hash(request.form.get('senha'))
	vsenha = sha256((vcsenha).encode()).hexdigest()
else:
	print("Erro de senhas...!")
vacao = "Criando usuario"
vqtd = 1
print(vnome, vfirst_name, vlast_name, vuser, vemail, vcelular, vcpf, vdt_nasc, vstatus, vtipo, vdatacr, vautentic, vsenha)	
# Usuario Administrador
try:
	conn = sqlite3.connect('./instance/cadbger.sqlite')
	sql = conn.cursor()
	sql.execute('INSERT INTO causuarios(nome, first_name, last_name, user, email, celular, cpf, dt_nasc, status, tipo, datacr, foto, autentic, senha) \
		VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (vnome, vfirst_name, vlast_name, vuser, vemail, vcelular, vcpf, vdt_nasc, vstatus, vtipo,  vdatacr, vfoto, vautentic, vsenha))
	conn.commit()
	# Alimenta CaAcesso
	sql.execute('INSERT into caacessos(nome, id_usu, email, celular, acao, ip, datacr, qtd, pais, uf, cidade, bairro, endereco, cep, cod_mun, regiao, orig_lat, orig_lng) \
		VALUES  (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', \
		(vnome, vid_usu, vemail, vcelular, vacao, vip, vdatacr, vqtd, vpais, vuf, vcidade, vbairro, vendereco, vcep, vcod_mun, vregiao, gorig_lat, gorig_lng))
	conn.commit()
	conn.close()
	# Alimenta Camodulo
	conn = sqlite3.connect('./instance/cadbger.sqlite')
	sql = conn.cursor()
	sql.execute('INSERT into camodulos(modulo, descr, img) VALUES  (?,?,?)', ('Configurador', 'Dados Mestres', 'img/logo-caon.mp4'))
	sql.execute('INSERT into camodulos(modulo, descr, img) VALUES  (?,?,?)', ('OnDRV', 'Transportes On-Line', 'img/logo-caon.mp4'))
	sql.execute('INSERT into camodulos(modulo, descr, img) VALUES  (?,?,?)', ('Ponto', 'Ponto On Line', 'img/logo-caon.mp4'))
	sql.execute('INSERT into camodulos(modulo, descr, img) VALUES  (?,?,?)', ('Marketing', 'Marketing Reverso', 'img/logo-caon.mp4'))
	conn.commit()
	conn.close() 
	#INSERT INTO camodulos(modulo, descricao, imagem) VALUES ('Configurador', 'Dados Mestres', ' img/logo-caon.mp4')
except Exception as e:	
	print('Registro nao foi criado! ', {e} )

vparam ="tmout"
vdescr ="Tempo de Ociosidade da conexao"
vvalor = 0
vtime = 5 # tempo em minutos
vcond = ""
vdt_ini = datetime.now()
vdt_fim = datetime.now()
vdatacr = datetime.now()
vusuario = "caonst.contact@gmail.com"
#parametros padroes
try:
	conn = sqlite3.connect('./instance/cadbger.sqlite')
	sql = conn.cursor()
	sql.execute('INSERT INTO caparam (param, descr, valor, time, cond, dt_ini, dt_fim, datacr, usuario) \
		VALUES (?,?,?,?,?,?,?,?,?)', (vparam, vdescr, vvalor, vtime, vcond, vdt_ini, vdt_fim, vdatacr, vusuario))
	sql.execute('INSERT INTO caparam (param, descr, valor, time, cond, dt_ini, dt_fim, datacr, usuario) \
		VALUES (?,?,?,?,?,?,?,?,?)',  ('B1','Bandeira 1',1.73,'','',vdt_ini,vdt_fim,vdatacr,'bob@gmail.com'))
	conn.commit()
	print('Parametros criados com sucesso! ', {e} )
except Exception as e:	
	print('Parametro nao foi criado! ', {e} )

#INSERT INTO caparam (param, descr, valor, time, cond, dt_ini, dt_fim, datacr, usuario) VALUES  ('B1','Bandeira 1',1.73,'','','01/01/2023t00:00:00','31/12/2025t00:00:00','30/09/2023t00:00:00','bob@gmail.com')

print("Processo finalizado...!")




