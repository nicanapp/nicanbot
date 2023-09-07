"""
essa biblioteca faz abstração dos dados para autenticação
com na API e tipos de dados enviados e recebidos

- api tambem altera o status do serviço especificado

"""
from lib.config import Config


class _APIsingleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            instance._configure()
            cls._instances[cls] = instance

        return cls._instances[cls]
    
class API(metaclass=_APIsingleton):

    def _configure():
        pass


def dummyData():
    return [
        {
            "id":1,
            "expressoes":[
                {
                    "id":1,
                    "last":"",
                    "silencioso":False,
                    "objeto_analise":"",
                    "expressao":"",
                    "midias":[
                        {
                            "slug":"instagram",
                            "config":{},
                        },
                        {
                            "slug":"facebook",
                            "config":{},
                        }
                    ],
                    "hashtags":[]
                }
            ]
        }
    ]