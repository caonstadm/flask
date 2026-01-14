#-------------------------------------------------------------------------------
# Name:        bpusuarios.py
# Purpose:
#
# Author:      Celso Abreu
#
# Created:     12/03/2023
# Copyright:   (c) CA_ON 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sqlite3
from flask import Flask, render_template, request, redirect, flash, Response
from flask import Blueprint
from datetime import date
from datetime import datetime
from app.models.tabels import CaUsuario, CaModulo, CaRotina, CaAplic
#, CaUsucli, CaUsumot, CaGrupo, CaMemgrupo, CaPedcar, Post, Follow
from database import db
from Cpf_cnpj import Cpf_cnpj
from app.vcpf import valida_cpf
from app.models.forms import UserForm
from werkzeug.security import generate_password_hash, check_password_hash
from Val_cpf import validate

data_atual = date.today()
data_em_texto = data_atual.strftime('%d/%m/%Y')
dt_ini = data_atual.strftime('%d/%m/%Y')
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
duracao = data_e_hora_atuais.strftime('%d/%m/%Y')

bp_usuarios = Blueprint("usuarios", __name__, template_folder="app/templates") 

# Validação do CPF pip install validate-docbr


@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
	msg = {}
	form = UserForm()
	dt = {}
	if request.method=='GET':
		return render_template('usu/cad_user.html', msg=msg)
	
	if request.method=='POST':
		vnome    = request.form.get('nome')
		vfirst_name = request.form.get('first_name')
		vlast_name = request.form.get('last_name')
		vuser    = request.form.get('user')
		vemail   = request.form.get('email')
		vcelular = request.form.get('celular')
		vcpf     = request.form.get('cpf')
	#	obj_cpf = Cpf_cnpj(vcpf)
	#	print(obj_cpf)	
		if vcpf == "":
			msg['msg'] = 'CPF em branco !!!'
			msg['class'] = 'alert-danger'
			return render_template('usu/cad_user.html', form=form, msg=msg, dt=dt)
		else:
			print(vcpf)
		#	obj_cpf = validate(vcpf)
			valida_cpf(vcpf)
		#	print('Tipo:', type(obj_cpf))
			print("Valida_cpf", valida_cpf(vcpf))
			if valida_cpf:
				vcpf = request.form.get('cpf')
				print(valida_cpf)
			else:
				msg['msg'] = 'CPF Invalido !!!'
				msg['class'] = 'alert-danger'
				return render_template('usu/cad_user.html', form=form, msg=msg, dt=dt)
		vdt_nasc = request.form.get('dt_nasc')
		vstatus  = 0
		vtipo    = "ADM"
		vdatacr  = date.today()
		vfoto    = ""
		vautentic = False
		vsenha   = request.form.get('senha')
		# Gerar o hash da senha
		hashed_password = generate_password_hash(vsenha, method='pbkdf2:sha256')
#		vcsenha  = request.form.get('csenha')	
		try:
			conn = sqlite3.connect('./instance/cadb.sqlite')     
			sql = conn.cursor()     
			sql.execute("INSERT INTO causuarios (nome, first_name, last_name, user, email, celular, cpf, dt_nasc, status, tipo, datacr, foto, autentic, senha) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (vnome, vfirst_name, vlast_name, vuser, vemail, vcelular, vcpf, vdt_nasc, vstatus, vtipo, vdatacr, vfoto, vautentic, hashed_password))

			#cursor.execute("INSERT INTO causuarios (nome, first_name, last_name, user, email, celular, cpf, dt_nasc, status, tipo, datacr, foto, autentic, senha) VALUES (?, ?)", (vnome, vfirst_name, vlast_name, vuser, vemail, vcelular, vcpf, vdt_nasc, vstatus, vtipo, vdatacr, vfoto, vautentic, vsenha))
#//			db.session.add(i))
			conn.commit()
		except Exception as e:	
				msg['msg'] = 'Registro Cadastrado com Sucesso!!!' + str(e)
				msg['class'] = 'alert-danger'
				return render_template('usu/cad_user.html', form=form, msg=msg, dt=dt)

#			i = CaUsuario(vnome, vfirst_name, vlast_name, vuser, vemail, vcelular, vcpf, vdt_nasc, vdt_ini, vduracao, vstatus, vsenha, vcsenha)
#//			db.session.add(i)
#			db.session.commit()

		return redirect('/usuarios/lst_usu')

#			return '''  
#				<html>
#				    <head><title>Hello Flask</title></head>
#				    <body>
#				    i
#				    </body>
#				</html> '''

#			return '''  
#				<html>
#				    <head><title>Hello Flask</title></head>
#				    <body>
#				        ''' +  vnome     + ''' '<br>' 
#				    	''' +  vfirst_name  + ''' '<br>'
#				    	''' +  vlast_name  + ''' '<br>'
#				        ''' +  vuser     + ''' '<br>'
#				        ''' +  vemail    + ''' '<br>'
#				        ''' +  vcelular  + ''' '<br>'
#				        ''' +  vcpf      + ''' '<br>'
#				        ''' +  vdt_nasc  + ''' '<br>'
#				        ''' +  vdt_ini   + ''' '<br>'
#					    ''' +  vduracao  + ''' '<br>'
#					    ''' +  str(vstatus)   + ''' '<br>'
#				        ''' +  vsenha    + ''' '<br>'
#				        ''' +  vcsenha   + '''
#				    </body>
#				</html> '''
      

@bp_usuarios.route('/lst_usu/<int:id>', methods=['GET', 'POST'])
@bp_usuarios.route('/lst_usu', defaults={'id': None})
def lst_usu(id):
	msg = {}
	db = CaUsuario.query.all()
	return render_template('usu/lst_user.html', db=db, msg=msg)

@bp_usuarios.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
	msg = {}
	dt = CaUsuario.query.get(id)
	#dt = Usuario.query.filter_by(id=id).first()
	if request.method == 'GET':
		return render_template('cad_user.html', dt=dt, msg=msg)
		
	if request.method == 'POST':
		if dt:
			db.session.delete(dt)
			db.session.commit()
			vnome    = request.form.get('nome')
			vfirst_name = request.form.get('first_name')
			vlast_name = request.form.get('last_name')			
			vuser    = request.form.get('user')
			vemail   = request.form.get('email')
			vcelular = request.form.get('celular')
			vcpf     = request.form.get('cpf')
			vdt_nasc = request.form.get('dt_nasc')
			vstatus  = int(request.form.get('status'))
			vsenha   = request.form.get('senha')
			vcsenha  = request.form.get('csenha')
			vstatus  = 0
			vtipo    = "ADM"
			vdatacr  = date.today()
			vfoto    = ""
#			vautentic = False
			if valida_cpf:
				msg['msg'] = 'CPF Invalido !!!'
				msg['class'] = 'alert-danger'
			else:
				conn = sqlite3.connect('./instance/cadb.sqlite')
				sql = conn.cursor()
				sql.execute('UPDATE CaUsuario SET nome=vnome, user=vuser, celular=vcelular, dt_nasc=vdt_nasc, status=vstatus, tipo=vtipo, datacr=vdatacr, foto=vfoto, autentic=vautentic, senha=vsenha WHERE id={id}')
				conn.commit()
				conn.close()

#				u = CaUsuario(nome=vnome, first_name=vfirst_name, last_name=vlast_name, user=vuser, email=vemail, /
#				  celular=vcelular, cpf=vcpf, dt_nasc=vdt_nasc, status=vstatus, tipo=vtipo, datacr=vdatacr, foto=vfoto, autentic=vautentic,
#					 senha=vsenha)
				#db.session.execute(f" UPDATE Usuario SET nome='{vnome}', user='{vuser}', celular='{vcelular}', dt_nasc='{vdt_nasc}', dt_ini='{vdt_ini}', duracao='{vduracao}' WHERE id='{id}' ")
#				db.session.add(u)
#				db.session.commit()
				return redirect('/usuarios/lst_usu')
		else:
			return HTTPResponse('Usuario nao Encontrado!')


@bp_usuarios.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
	msg = {}
	d = CaUsuario.query.get(id)
	if request.method == 'POST':
		if d:
			db.session.delete(d)
			db.session.commit()
			return redirect('/usuarios/lst_usu')
	#	abort(404)
	return render_template('confElimina.html')






