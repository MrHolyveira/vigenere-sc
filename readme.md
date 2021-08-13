# Universidade de Brasília
## Projeto cifrador/decifrador/Quebrador de Vigenère

## Compilação windows

Para gerar o executável execute o comando abaixo:

```sh
pip install -r requirements.txt
```
E depois execute:
```
pyinstaller main.spec
```
ou execute o arquivo 'Gera exe.bat'.

## OBS:
Ao que parece a versão atual do PyInstaller não é compatível com o matplotlib==3.4.2, então caso dê um erro na hora da compilação será necessário instalar uma versão do PyInstaller mais nova onde a incompatibilidade foi corrigida executando o comando abaixo:
```
pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip
```