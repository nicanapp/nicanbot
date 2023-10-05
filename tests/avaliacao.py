from lib.analise import avaliacao
from entidades.Publish import Publish

strpub = """“Não concordamos com a ideia de que a Polícia está sempre errada”, diz Flávio Dino.

Ministro da Justiça afirmou que ideia de que a polícia está sempre certa é falsa, mas que supor que a instituição está sempre errada desestimula a ação dos policiais."""

pubtest = Publish("instagram", strpub, "link")

avaliacao(pubtest, "Flávio Dino")

print(pubtest.avaliacao)