#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 11:06:55 2025

@author: Jorge Paulo Santos
"""

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def calcular_dpp(dum):
    """Calcula a Data Provável do Parto usando a Regra de Naegele"""
    dpp = dum + relativedelta(days=7, months=-3)
    return dpp

def calcular_idade_gestacional(dum):
    """Calcula a idade gestacional atual em semanas e dias"""
    hoje = datetime.now().date()
    diferenca = hoje - dum
    semanas = diferenca.days // 7
    dias = diferenca.days % 7
    return semanas, dias

def determinar_trimestre(semanas):
    """Determina o trimestre da gestação"""
    if semanas < 14:
        return "Primeiro trimestre"
    elif 14 <= semanas < 28:
        return "Segundo trimestre"
    else:
        return "Terceiro trimestre"

def main():
    print("\nCalculadora Obstétrica - Data Provável do Parto (DPP)\n")
    
    while True:
        try:
            entrada = input("Digite a Data da Última Menstruação (DD/MM/AAAA): ")
            dum = datetime.strptime(entrada, "%d/%m/%Y").date()
            
            if dum > datetime.now().date():
                print("Erro: A data não pode ser futura!\n")
                continue
                
            dpp = calcular_dpp(dum)
            semanas, dias = calcular_idade_gestacional(dum)
            trimestre = determinar_trimestre(semanas)
            
            print("\nResultados:")
            print(f"Data da Última Menstruação (DUM): {dum.strftime('%d/%m/%Y')}")
            print(f"Data Provável do Parto (DPP): {dpp.strftime('%d/%m/%Y')}")
            print(f"Idade Gestacional: {semanas} semanas e {dias} dias")
            print(f"Trimestre: {trimestre}")
            
            if semanas >= 40:
                print("\nAtenção: Gestação prolongada!")
            
            break
            
        except ValueError:
            print("Formato inválido! Use DD/MM/AAAA\n")
        except Exception as e:
            print(f"Ocorreu um erro: {str(e)}")
            break

if __name__ == "__main__":
    main()
    print("\nConsulte sempre seu médico para acompanhamento adequado!")