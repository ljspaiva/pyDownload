# pyDownload Beta 0.01
# Create: Prof. Me. Leandro J. S. Paiva
# Date: 04/09/2019
# Update Date: 05/09/2019

import urllib.request, urllib.parse, urllib.error

arq = open('lista.txt', 'r')
log = open('log_erro.txt', 'w')

for line in arq:
    name = line.split("/")
    tamLine = len(name)
    fileName = name[tamLine-3] + "_" + name[tamLine-2] + "_" + name[tamLine-1].rstrip('\n')
    print("Download: " + fileName)
    try:
        urllib.request.urlretrieve(line, fileName)
    except Exception as e:
        print("Erro ao efetuar download: " + fileName)
        print("Detalhes: " + str(e))
        log.write(line + "[[[ERRO: " + str(e) + "]]]\n")

arq.close();
log.close();
