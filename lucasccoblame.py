#!/usr/bin/env python
import sys
import subprocess 

def print_result(msg):
  sep = '==========================='
  print('')
  print(sep)
  print msg
  print(sep)
  print('')

if len(sys.argv) != 3:
  errorMsg = []
  errorMsg.append(':( Infelizmente voce nao passou os argumentos certos lucasccoblame FILE_PATH LINE_NUMBER mas temos certeza que foi o lucascco quem fez a cagada!')
  print_result(errorMsg)
  sys.exit()


filename = sys.argv[1]
line = sys.argv[2]

if (not filename or not line):
  print_result(errorMsg)
  sys.exit(0)

gitblame = ['git', 'blame', '-L', str(line) + ',' + str(line), filename]

result = subprocess.check_output(gitblame)

culprit = result.split(' (')[1].split(' 20')[0]

msg = ''
if culprit == 'Lucas Correa':
  msg = 'Nao podia ser diferente, lucascco eh o culpado por essa cagada! :)'
else:
  msg = ':( Infelizmente o culpado por essa cagada eh o ' + culprit + ', mas, temos conviccao que foi em pair programming com lucascco.'
print_result(msg)