# 💧 AquaConsciente

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-181717?style=for-the-badge&logo=github&logoColor=white)
![Sustentabilidade](https://img.shields.io/badge/Sustentabilidade-Água-00A8E8?style=for-the-badge)

## 🎯 Sobre o projeto

O **AquaConsciente** é um script em Python criado para uma campanha de conscientização ambiental de uma companhia de saneamento. Ele classifica o **perfil de consumo de água** de um imóvel e mostra **alertas educativos** para o morador.

## 🧠 Regras de classificação

| Tipo de imóvel | Consumo mensal | Mensagem |
|---|---|---|
| 🏢 Comercial | qualquer | Tarifa comercial aplicada – consulte o plano corporativo. |
| 🏬 Apartamento | menor que 10 m³ | Consumo econômico – excelente controle de água! |
| 🏠 Casa ou apartamento | até 25 m³ | Consumo moderado – dentro do padrão residencial. |
| 🚨 Qualquer outro caso | acima de 25 m³ | Consumo excessivo – adote medidas de economia e verifique vazamentos. |

## 🛠️ Tecnologias utilizadas

- 🐍 **Python 3**
- 🐙 **Git e GitHub** para versionamento

## ▶️ Como executar

1. Certifique-se de ter o **Python 3** instalado:
```bash
   python --version
```
2. Clone este repositório:
```bash
   git clone https://github.com/davivaresch1/aqua-consciente.git
```
3. Entre na pasta do projeto:
```bash
   cd aqua-consciente/consumo-agua
```
4. Execute o programa:
```bash
   python app.py
```

## 💻 Exemplo de uso

```
Tipo do imóvel (comercial, casa ou apartamento): apartamento
Consumo mensal em m³: 8
Consumo econômico - excelente controle de água!
```