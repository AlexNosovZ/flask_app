from flask import Flask
from api.api_pull import blueprint as api
import core.conf_prod as conf_prod
# from . import conf_prod.config, conf_prod.CfgProd, conf_prod.get_config

def create_app():
    app = Flask(__name__)  
    conf_prod.config = conf_prod.CfgProd()
    app.config.from_object(conf_prod.get_config2())
    app.register_blueprint(api)
    return app

    


    
