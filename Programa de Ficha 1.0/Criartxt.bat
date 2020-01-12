REM Esse programa cria o arquivo em que ficará inserido os dados da ficha
REM Ele simplesmente pergunta o seu nome, ou seja, o nome do arquivo txt 
REM Pra criar o arquivo txt, ele procura no directorio, o arquivo txt com o nome armazenado na variavel nomeVar. Ao não achar, ele cria o arquivo.

echo off
cls
set /p nomeVar=Nome: 
dir > Fichas\%nomeVar%.txt
pause
exit
