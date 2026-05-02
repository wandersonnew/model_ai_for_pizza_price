# Model AI for Pizza Price

Projeto de machine learning para prever o preço de uma pizza com base no seu diâmetro, utilizando Regressão Linear. Inclui um notebook para treinamento do modelo e uma aplicação web interativa com Streamlit.

## Estrutura do Projeto

```
model_ai_for_pizza_price/
├── pizza_price_simple.ipynb  # Notebook: análise, treinamento e exportação do modelo
├── app_pizza_simple.py       # Aplicação web Streamlit para previsão de preços
├── pizzas.csv                # Dataset de treinamento (diâmetro x preço)
├── pizza_price_model.pkl     # Modelo treinado serializado
└── pyproject.toml            # Dependências do projeto (gerenciado pelo Poetry)
```

## Como Funciona

1. **Treinamento** (`pizza_price_simple.ipynb`):
   - Carrega o dataset `pizzas.csv` com colunas `diametro` (cm) e `preco` (R$)
   - Treina um modelo de Regressão Linear com scikit-learn
   - Exporta o modelo treinado para `pizza_price_model.pkl` via pickle

2. **Aplicação** (`app_pizza_simple.py`):
   - Carrega o modelo salvo (`pizza_price_model.pkl`)
   - Recebe o diâmetro da pizza como entrada do usuário
   - Exibe o preço previsto em reais

## Pré-requisitos

- Python >= 3.12
- [Poetry](https://python-poetry.org/)

## Instalação

```bash
poetry install
```

## Executando a Aplicação

```bash
poetry run streamlit run app_pizza_simple.py
```

## Dependências Principais

| Pacote | Versão |
|---|---|
| streamlit | >=1.57.0, <2.0.0 |
| scikit-learn | >=1.8.0, <2.0.0 |
| matplotlib | >=3.10.9, <4.0.0 |

## Dataset

O arquivo `pizzas.csv` contém 11 amostras com diâmetros de 20 a 40 cm e preços de R$50 a R$100, com incremento linear de R$2,50 por cm.

## Licença

Consulte o arquivo [LICENSE](LICENSE).
