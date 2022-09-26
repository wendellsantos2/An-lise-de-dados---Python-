import csv
from model.DbUtil import DbUtil
from model.Endereco import Endereco

import re 
class CepController():
    @staticmethod
    def buscar_ceps():
        with open("ceps.txt","r", encoding="utf-8") as arquivos:
            enderecos = csv.DictReader(arquivos,delimiter="\t")
            itens = " "
            cont = 1
            while True != False:                
                for ceps in enderecos:
                    cep = Endereco(ceps["CEP"],ceps["ESTADO"],ceps["BAIRRO"],ceps["COMPLEMENTO"],ceps["RUA"],)
                    CepController.convesor_nulo(cep)
                    CepController.conversor_caractere_especial(cep)
                    itens += f"""('{cep.cep}','{cep.estado}','{cep.rua}','{cep.bairro}','{cep.complemento}'),"""
                    cont+=1
                    if cont == 1000:
                        DbUtil.enviar_para_banco(itens[:-1])
                        cont = 1
                        itens = " "

    def convesor_nulo(cep):
        if  cep.complemento is None:
            cep.complemento = ""
                    
    def conversor_caractere_especial(cep):
        cep.complemento = cep.complemento.replace("'", "d\\'")
        cep.estado = cep.estado.replace("'", "d\\'")
        cep.rua = cep.rua.replace("'", "d\\'")
        cep.bairro = cep.bairro.replace("'", "d\\'")
             
    def menu():
            print('------------------------------------')
            enviar_enderecos = input("Escolha o que vc deseja: (1-Enviar ceps para o banco , 2-Consultar ceps) : ")
            print(f'Você escolheu  o {enviar_enderecos}')
            if enviar_enderecos == "1":
                CepController.buscar_ceps()
            while '2' != True:        
                if enviar_enderecos == "2" :
                    cep = input('Qual cep vc deseja consultar: ')
                    DbUtil.consultar_endereco(cep)
                    consultar_novamente= input('Você deseja consultar de novo ? (2-sim,1-nao)')
                    if consultar_novamente == "1":
                        print('fechando o programa ') 
                        break 
                    
            
            
                    