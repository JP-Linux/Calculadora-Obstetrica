# Calculadora Obstétrica - Data Provável do Parto (DPP)

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://jp-linux.github.io)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Ferramenta clínica para cálculo da Data Provável do Parto (DPP), idade gestacional e trimestre de gravidez, seguindo a Regra de Naegele.

## 📑 Funcionalidades

- **Cálculo da DPP**: Usando a Regra de Naegele (DUM + 7 dias - 3 meses)
- **Idade Gestacional**: Apresentação em semanas + dias decorridos
- **Determinação do Trimestre**: Classificação automática do trimestre
- **Validações**: Checagem de datas futuras e formato correto

## ⚙️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/JP-Linux/Calculadora-Obstetrica.git
```

2. Instale as dependências:
```bash
pip install python-dateutil
```

## 🚀 Como Usar

Execute o script:
```bash
python3 calculadora_obstetrica.py
```

**Formato de entrada:**  
`DD/MM/AAAA` (ex: 10/04/2025)

**Saída:**
```
Data da Última Menstruação (DUM): 10/04/2025
Data Provável do Parto (DPP): 17/01/2026
Idade Gestacional: 0 semanas e 0 dias
Trimestre: Primeiro trimestre
```

## 🧠 Base Científica

- **Regra de Naegele**: Padrão ouro para cálculo de DPP desde 1812
- **Trimestres**: 
  - 1º: 0-13 semanas
  - 2º: 14-27 semanas
  - 3º: 28+ semanas

## 👤 Autor

**Jorge Paulo Santos**  
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JP-Linux)
[![Email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jorgepsan7@gmail.com)

## 💝 Suporte ao Projeto

Se este projeto foi útil para você, considere apoiar meu trabalho através do GitHub Sponsors:

[![Sponsor](https://img.shields.io/badge/Sponsor-JP_Linux-ea4aaa?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/JP-Linux)


## 📜 Licença

Distribuído sob licença MIT. Veja `LICENSE` para mais informações.

## ⚠️ Aviso Legal

Este software é destinado **apenas para fins educacionais e de pesquisa**. Não substitui a avaliação de um profissional médico qualificado. Sempre consulte seu obstetra para acompanhamento pré-natal adequado.

