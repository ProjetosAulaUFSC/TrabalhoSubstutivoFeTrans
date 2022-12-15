from componente import Componente
import time
import os

def addComp():
    name = input("Insira a Identificacao do Componente: ")
    t_max = int(input("Insira a Temperatura Limite de Funcionamento: "))
    f_heat = int(input("Insira o Fluxo de Calor: "))
    length = int(input("Insira a Expessura do Componente: "))
    return Componente(name, t_max, f_heat, length)

def seeComp(vec):
    if(len(vec) == 0): print("Nenhum componente cadastrado")
    else:
        print("Lista de Componentes Cadastrados")
        for i in range(len(vec)):
            print(f'\nComponente: {vec[i].name}')
            print(f'Temperatura Máxima: {vec[i].t_max}')
            print(f'Fluxo de Calor: {vec[i].f_heat}')
            print(f'Expessura: {vec[i].length}')
    aux = input("\nPressione enter para continuar")

def calcFlux(vec):
    return 0

def main():
    vec = []
    opt = 1
    flag = False
    while(opt):
        if(len(vec)>0): flag = True
        os.system("cls")
        print("Menu")
        print("1 - Adicionar Componente")
        print("2 - Ver Componentes")
        if(flag):
            print("3 - Calcular Fluxo de Calor")
            print("4 - Sair")
        else:
            print("3 - Sair")
        opt = input("Escolha uma opcao: ")
        os.system("cls")
        if(opt == "1"): vec.append(addComp())
        elif(opt == "2"): seeComp(vec)
        elif(opt == "3" and flag): calcFlux(vec)
        elif(opt == "4" or (opt == "3" and not flag)): break
        elif(opt == "7"): vec.append(Componente("Genérico", 75, 100000, 0.008) )
    print("Saindo")

main()
