import os

from flask import Flask

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
		# SESSION_TYPE='filesystem'
		)
	if test_config is None:
		print('no test_config')
		app.config.from_pyfile('config.py', silent=True)
	else:
		print('got test_config')
		print(vars(test_config))
		app.config.from_mapping(test_config)
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	from . import db
	db.init_app(app)

	from . import auth
	app.register_blueprint(auth.bp)

	return app
