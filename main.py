from entidades.Service import Service
from entidades.Expressao import Expressao
from services.instagram_service import main as instagram

expressao = Expressao(1,1,"Fallen na Furia", "Fallen na Fúria")
expressao.addHashTag("#falleninsider")
expressao.addHashTag("#fallennafuria")

service = Service(expressao)

instagram(service)