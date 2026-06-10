# Global Solution - Análise Estatística de Missões Espaciais

## Descrição da solução
Este projeto realiza uma análise estatística exploratória sobre missões espaciais utilizando uma base real publicada no Kaggle: **All Space Missions from 1957**. A análise busca apoiar uma empresa do setor aeroespacial na leitura de padrões de lançamento, concentração temporal e desempenho das missões.

## Fonte da base de dados
- Kaggle: All Space Missions from 1957
- Versão limpa consultada: Space Missions Dataset (From 1957), com referência ao Kaggle e ao Next Spaceflight.
- Arquivo usado no projeto: `space_missions_kaggle_amostra.csv`

## Justificativa da base
A base é adequada ao tema da avaliação porque contém registros reais de lançamentos espaciais, incluindo empresa responsável, local de lançamento, data, foguete, status do foguete e status da missão. Esses dados permitem analisar tendências da nova economia espacial, como concentração de lançamentos por empresa, desempenho operacional e evolução temporal das missões.

## Arquivos do repositório
- `space_missions_kaggle_amostra.csv`: base de dados utilizada.
- `analise_space_missions.py`: código-fonte em Python.
- `Relatorio_Estatistico_Space_Missions.pdf`: relatório técnico final.
- `entrega.txt`: modelo do arquivo de entrega com nomes/RM e link do GitHub.
- `resultados/`: pasta criada ao executar o código, contendo tabelas e gráficos.

## Bibliotecas utilizadas
- pandas
- matplotlib

## Como executar
1. Instale as dependências:
```bash
pip install pandas matplotlib
```
2. Execute o código:
```bash
python analise_space_missions.py
```
3. Os gráficos e tabelas serão salvos automaticamente na pasta `resultados`.

## Requisitos atendidos
- Seleção e justificativa de base real.
- Tabela de frequência para variável quantitativa discreta.
- Tabela de frequência para variável quantitativa contínua.
- Dois gráficos estatísticos com variáveis diferentes.
- Duas análises univariadas com média, mediana, moda, máximo, mínimo, amplitude, variância, desvio padrão e quartis.
- Relatório estatístico final em PDF com interpretação dos resultados.
