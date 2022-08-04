class CfgProd:
    DEBUG = True
    TESTING = True
    FLASK_DEBUG = True

config: CfgProd = None
def get_config2() -> CfgProd:
    return config
