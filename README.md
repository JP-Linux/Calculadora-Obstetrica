# Calculadora Obstétrica - Data Provável do Parto (DPP)

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

## 👩💻 Contribuição

1. Faça um fork do projeto
2. Crie sua branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📜 Licença

Distribuído sob licença MIT. Veja `LICENSE` para mais informações.

## ⚠️ Aviso Legal

Este software é destinado **apenas para fins educacionais e de pesquisa**. Não substitui a avaliação de um profissional médico qualificado. Sempre consulte seu obstetra para acompanhamento pré-natal adequado.

## ✉️ Contato

Jorge Paulo Santos - [@jorgepaulo](https://github.com/JP-Linux) - jorgepsan7@gmail.com