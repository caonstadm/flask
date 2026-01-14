## Config.py
# Arquivo de configurações e variaveis de anbientes

DEBULG = True
# Criamos essa Variavel de ambiente padrao do ambiente Flask Obrigatorio para a segurança de criptografia

SECRET_KEY = "Taxi5388"
SQLALCHEMY_DATABASE_URI = "sqlite:///cadb.sqlite"
SQLALCHEMY_TRACK_MODIFICATIONS = True 

#UPLOAD_FOLDER = 'static/img/'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER