rem Arquivo .bat que executa um arquivo em python que lê e detecta QDC's numa planilha
rem echo é uma msg na tela
rem @echo off impede o cmd de mostrar o código sem colocar '@' na frente de todos os comandos
rem rem é um comentário
:: também é um comnetário
rem goto :local manda o programa ir para a linha que tem :local (local pd ser qlqr coisa)
rem definir variaveis é feito com o set (nome variável)=(valor)
rem receber input é feito: set /p (nome variável)=(valor)
rem a unica forma que achei de fazer 'or' é com a mecânica esquisita dos if's que usei abaixo
rem esse arquivo abre o cmd e executa os comandos a partir do diretório que está instalado...
rem portanto para executar programas, é necessário que o bat e ele estejam na mesma pasta
rem para rodar o .bat basta clicar 2x nele
rem obrigado por virem à minha palestra TED
@echo off
:inicio
cls
echo Bem vindo!
echo Rodando teste de planilha...
python simu_planilha.py
echo fornecimento
python DiagramaUnifilar.py
echo Deu certo?
:erro
set /p resp="  (s/n) "
if %resp%==s goto :valido
if %resp%==n goto :inicio
echo resposta invalida
goto :erro
:valido
echo Maravilha :)
echo Tchau Tchau
timeout 5