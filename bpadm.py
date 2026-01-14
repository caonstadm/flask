#-------------------------------------------------------------------------------
# Name:        bpadm.py
# Purpose:
#
# Author:      Celso Abreu
#
# Created:     12/03/2023
# Copyright:   (c) CA_ON 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from flask import Flask, render_template, request, redirect, flash, Response
from flask import Blueprint
from datetime import date
from datetime import datetime
from app.models.tabels import CaUsuario, CaModulo, CaRotina, CaAplic
#, CaUsucli, CaUsumot, CaGrupo, CaMemgrupo, CaPedcar, Post, Follow
from database import db
from Cpf_cnpj import Cpf_cnpj
import tkinter as tk
import tkinter.messagebox as tkmsg

data_atual = date.today()
data_em_texto = data_atual.strftime('%d/%m/%Y')
dt_ini = data_atual.strftime('%d/%m/%Y')
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
duracao = data_e_hora_atuais.strftime('%d/%m/%Y')

bp_adm = Blueprint("adm", __name__, template_folder="app/templates") 

@bp_adm.route('/c_mod', methods=['GET', 'POST'])
def c_mod():
	msg = {}
	if request.method=='GET':
		return render_template('adm/cad_mod.html', msg=msg)
	
	if request.method=='POST':
		vmodulo    = request.form.get('modulo')
		if vmodulo:
			i = CaModulo(modulo=vmodulo)
			db.session.add(i)
			db.session.commit()
			return redirect('/adm/l_mod')
		else:
			msg['msg'] = 'CPF Invalido !!!'
			msg['class'] = 'alert-danger'
			return render_template('adm/cad_mod.html', msg=msg)

#			return '''  
#				<html>
#				    <head><title>Hello Flask</title></head>
#				    <body>
#				   		''' +  vuser     + ''' '<br>'
#				    </body>
#				</html> '''


@bp_adm.route('/l_mod/<int:id>', methods=['GET', 'POST'])
@bp_adm.route('/l_mod', defaults={'id': None})
def l_mod(id):
	msg = {}
	db = CaModulo.query.all()
	return render_template('adm/lst_mod.html', db=db, msg=msg)

@bp_adm.route('/u_mod/<int:id>', methods=['GET', 'POST'])
def u_mod(id):
	msg = {}
	dt = CaModulo.query.get(id)
	#dt = CaModulo.query.filter_by(id=id).first()
	if request.method == 'GET':
		return render_template('adm/cad_mod.html', dt=dt, msg=msg)
		
	if request.method == 'POST':
		if dt:
			db.session.delete(dt)
			db.session.commit()
			vmodulo = request.form.get('modulo')
			u = CaModulo(modulo=vmodulo)
			#db.session.execute(f" UPDATE Usuario SET nome='{vnome}', user='{vuser}', celular='{vcelular}', dt_nasc='{vdt_nasc}', dt_ini='{vdt_ini}', duracao='{vduracao}' WHERE id='{id}' ")
			db.session.add(u)
			db.session.commit()
			return redirect('/adm/l_mod')
		else:
			return HTTPResponse('Usuario nao Encontrado!')


@bp_adm.route('/d_mod/<int:id>', methods=['GET', 'POST'])
def d_mod(id):
	msg = {}
	d = CaRotina.query.get(id)
	if request.method == 'POST':
		if d:
			db.session.delete(d)
			db.session.commit()
			return redirect('/adm/l_mod')
	#	abort(404)
	return render_template('confElimina.html')


@bp_adm.route('/c_rot', methods=['GET', 'POST'])
def c_rot():
	msg = {}
	tb = CaModulo.query.all()
	dt = {}
	if request.method=='GET':
		return render_template('adm/cad_rot.html', tb=tb, dt=dt, msg=msg)
	
	if request.method=='POST':
		vid_mod = request.form.get('id_mod')
		vrotina = request.form.get('rotina')
		if vrotina:
			i = CaRotina(id_mod=int(vid_mod), rotina=vrotina)
			db.session.add(i)
			db.session.commit()
			return redirect('/adm/l_rot')
		else:
			msg['msg'] = 'Rotina nao cadastrada !!!'
			msg['class'] = 'alert-danger'
			return render_template('adm/cad_rot.html', tb=tb, dt=dt, msg=msg)

#			return '''  
#				<html>
#				    <head><title>Hello Flask</title></head>
#				    <body>
#				   		''' +  vuser     + ''' '<br>'
#				    </body>
#				</html> '''


@bp_adm.route('/u_rot/<int:id>', methods=['GET', 'POST'])
def u_rot(id):
	msg = {}
	dt = CaRotina.query.get(id)
	tb = CaModulo.query.filter_by(id_mod=dt.id_mod).first()
	#console.log(tb)
	#dt = CaModulo.query.filter_by(id=id).first()
	if request.method == 'GET':
		return render_template('adm/cad_rot.html', tb=tb, dt=dt, msg=msg)
		
	if request.method == 'POST':
		if dt:
			db.session.delete(dt)
			db.session.commit()
			vrotina = request.form.get('rotina')
			u = CaRotina(id_mod=dt.id_mod, rotina=vrotina)
			#db.session.execute(f" UPDATE Usuario SET nome='{vnome}', user='{vuser}', celular='{vcelular}', dt_nasc='{vdt_nasc}', dt_ini='{vdt_ini}', duracao='{vduracao}' WHERE id='{id}' ")
			db.session.add(u)
			db.session.commit()
			return redirect('/adm/l_rot')
		else:
			return HTTPResponse('Usuario nao Encontrado!')


@bp_adm.route('/d_rot/<int:id>', methods=['GET', 'POST'])
def d_rot(id):
	msg = {}
	dt = CaRotina.query.get(id)
	if request.method == 'POST':
		if dt:
			db.session.delete(dt)
			db.session.commit()
			return redirect('/adm/l_rot')
	#	abort(404)
	return render_template('confElimina.html', msg=msg)


@bp_adm.route('/l_rot', methods=['GET', 'POST'])
@bp_adm.route('/l_rot', defaults={'id': None})
def l_rot(id):
	msg = {}
	tb = {}
	dt = CaRotina.query.all()
	return render_template('adm/lst_rot.html', tb=tb, dt=dt, msg=msg)



@bp_adm.route('/c_apl', methods=['GET', 'POST'])
def c_apl():
	msg = {}
	tb = CaRotina.query.all()
	dt = {}
	if request.method=='GET':
		return render_template('adm/cad_apl.html', tb=tb, dt=dt, msg=msg)
	
	if request.method=='POST':
		vid_mod = request.form.get('id_mod')
		vid_rot = request.form.get('id_rot')
		vaplic = request.form.get('aplic')
		vroteiro = request.form.get('roteiro')
		vrotina = request.form.get('rotina')
		vcaminho = request.form.get('caminho')
		vhtml = request.form.get('html')
		vdata = request.form.get('data')
		if vrotina:
			i = CaAplic(id_mod=int(vid_mod), id_rot=int(vid_rot), aplic=vaplic, roteiro=vroteiro, caminho=vroteiro, html=vhtml, data=vdata)
			db.session.add(i)
			db.session.commit()
			return redirect('/adm/l_apl')
		else:
			msg['msg'] = 'Aplicação nao cadastrada !!!'
			msg['class'] = 'alert-danger'
			return render_template('adm/cad_apl.html', tb=tb, dt=dt, msg=msg)

#			return '''  
#				<html>
#				    <head><title>Hello Flask</title></head>
#				    <body>
#				   		''' +  vuser     + ''' '<br>'
#				    </body>
#				</html> '''


@bp_adm.route('/u_apl/<int:id>', methods=['GET', 'POST'])
def u_apl(id):
	msg = {}
	dt = CaAplic.query.get(id)
	tb = CaModulo.query.filter_by(id_mod=dt.id_mod).first()
	tr = CaModulo.query.filter_by(id_mod=dt.id_mod, id_rot=dt.id_rot).first()
	#console.log(tb)
	#dt = CaModulo.query.filter_by(id=id).first()
	if request.method == 'GET':
		return render_template('adm/cad_apl.html', tb=tb, dt=dt, tr=tr, msg=msg)
		
	if request.method == 'POST':
		if dt:
			db.session.delete(dt)
			db.session.commit()
			vrotina = request.form.get('rotina')
			u = CaAplic(id_mod=int(vid_mod), id_rot=int(vid_rot), aplic=vaplic, roteiro=vroteiro, caminho=vroteiro, html=vhtml, data=vdata)
			#db.session.execute(f" UPDATE Usuario SET nome='{vnome}', user='{vuser}', celular='{vcelular}', dt_nasc='{vdt_nasc}', dt_ini='{vdt_ini}', duracao='{vduracao}' WHERE id='{id}' ")
			db.session.add(u)
			db.session.commit()
			return redirect('/adm/l_apl')
		else:
			return HTTPResponse('Registro nao Encontrado!')


@bp_adm.route('/d_apl/<int:id>', methods=['GET', 'POST'])
def d_apl(id):
	msg = {}
	dt = CaAplic.query.get(id)
	if request.method == 'POST':
		if dt:
			db.session.delete(dt)
			db.session.commit()
			return redirect('/adm/l_apl')
	#	abort(404)
	return render_template('confElimina.html', msg=msg)


@bp_adm.route('/l_apl', methods=['GET', 'POST'])
@bp_adm.route('/l_apl', defaults={'id': None})
def l_apl(id):
	msg = {}
	tb = {}
	dt = CaAplic.query.all()
	return render_template('adm/lst_apl.html', tb=tb, dt=dt, msg=msg)


