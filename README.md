# nicanbot
Scraping Bot

### Expressões

Expressão exemplo: `palavra1 de palavra2 palavra3`

parte1: tenta a frase completa

```
txt = re.sub("palavra1 de palavra2 palavra3", "<b>palavra1 de palavra2 palavra3</b>", txt)
```

parte1: splita as palavras e substitui

```
txt = re.sub("palavra1", "<b>palavra1</b>", txt)
txt = re.sub("palavra2", "<b>palavra2</b>", txt)
txt = re.sub("palavra3", "<b>palavra3</b>", txt)
```

parte3: busca a ocorrencia da primeira palavra ou frase e pega sua posição para fazer um substring

