# Estudo de qualidade de vinhos
*Este repositório conta com um projeto de análise para identificar os fatores de qualidades de vinho, bem como apresenta um sistema para usuários interagirem com o modelo estatístico e realizarem suas simulações.*


# Dados
Os dados utilizados foram obtidos pelo kaggle ([link](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)) e um script foi responsável por ler o arquivo .csv e carregar em um banco de dados MySQL local.

# Ferramentas
Este projeto foi desenvolvido em um sistema operacional Ubuntu 22.04 utilizando Python 3.10.4 em um ambiente virtual. Todas as dependências estão no arquivo requirements.txt e podem ser instaladas pelo "pip install -r requirements.txt". As principais bibliotecas utilizadas foram:

- MySQL
- Python
- SQLAlchemy

# Manager
A gestão do banco de dados é feita por meio do script manager.py, que implementa funções de criação, remoção e seed de dados. Para interagir com este script em terminal, basta utilizar o comando "python manager.py <nome_data_funcao>". Os seguintes argumentos estão disponíveis:

- `python manager.py create` : faz a criação das tabelas no banco de dados.
- `python manager.py delete` : remove as tabelas com todo o conteúdo do banco de dados.
- `python manager.py seed` : carrega os dados de vinhos do arquivo csv.