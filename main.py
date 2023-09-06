from entidades.ResponseService import ResponseService
from entidades.Expressao import Expressao
from services.instagram_service import main as instagram

expressao = Expressao(1,1,"Fallen na Furia", "Fallen na Fúria")
expressao.addHashTag("#falleninsider")
expressao.addHashTag("#fallennafuria")

response = ResponseService(expressao)

instagram(response)