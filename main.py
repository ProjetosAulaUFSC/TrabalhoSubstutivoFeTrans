from componente import Componente
import os

t_liquido = 30
h_liquido = 1500
l_substrato = 8*10**(-3)
k_substrato = 238
R_eq = 1/(l_substrato/k_substrato+1/h_liquido)
t_ar = 25
h_ar = 200

def addComp():
    name = input("Insira a Identificacao do Componente: ")
    t_max = int(input("Insira a Temperatura Limite de Funcionamento (°C): "))
    area = float(input("Insira a Area de Contato do Componente (m²): "))
    heat = round(R_eq*(t_max - t_liquido)*area, 3)
    return Componente(name, t_max, area, heat, heat/area)

def seeComp(vec):
    if(len(vec) == 0): print("Nenhum componente cadastrado")
    else:
        print("Lista de Componentes Cadastrados")
        for i in range(len(vec)):
            print(f'\nComponente: {vec[i].name}')
            print(f'Temperatura Máxima: {vec[i].t_max}°C')
            print(f'Calor: {vec[i].heat}W')
    input("\nPressione enter para continuar")

def calcArea(vec):
    q_total = 0
    flux_total = 0
    for comp in vec: 
        q_total = q_total + comp.heat
        flux_total = flux_total + comp.flux
    print(f"O total de calor gerado pelo sistema é {q_total:.3f} W")
    print(f"O fluxo de calor gerado pelo sistema é {flux_total:.3f} W/m²")
    A = q_total/(h_ar*(t_liquido-t_ar))
    print(f"Para manter o sistema dentro das condições ideais, precisariamos de pelo menos {A:.3f} m² de serpentinas resfriadas pelas ventoinhas")
    input("\nPressione enter para continuar")

def main():
    vec = []
    opt = "0"
    flag = False
    while(opt):
        if(len(vec)>0): flag = True
        os.system("cls")
        print("Menu")
        print("1 - Adicionar Componente")
        print("2 - Ver Componentes")
        if(flag):
            print("3 - Calcular Calor Total e Área para arrefecimento")
            print("4 - Sair")
        else: print("3 - Sair")
        opt = input("Escolha uma opcao: ")
        os.system("cls")
        if(opt == "1"): vec.append(addComp())
        elif(opt == "2"): seeComp(vec)
        elif(opt == "3" and flag): calcArea(vec)
        elif(opt == "4" or (opt == "3" and not flag)): break
        elif(opt == "7"): 
            heat = round(R_eq*(75 - t_liquido)*0.012508,3)
            vec.append(Componente("Genérico", 75, 0.012508, heat))
        else: opt = "0"

main()
