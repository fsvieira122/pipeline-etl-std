import pandas as pd

# Extract
def extrair_dados():
    dados = pd.read_csv('vendas_livros.csv')
    return dados

# Transform
def transformar_dados(dados):
    # Calcula o total de vendas por autor
    total_por_autor = dados.groupby('AUTOR')['VENDAS'].sum().reset_index()

    # Filtra livros publicados após 2010
    livros_apos_2010 = dados[dados['ANO DE PUBLICAÇÃO'] > 2010]

    return total_por_autor, livros_apos_2010

# Load
def carregar_dados(total_por_autor, livros_apos_2010):
    # Salva os totais de vendas por autor em um novo arquivo CSV
    total_por_autor.to_csv('total_vendas_por_autor.csv', index=False)

    # Salva os livros publicados após 2010 em um novo arquivo CSV
    livros_apos_2010.to_csv('livros_apos_2010.csv', index=False)

    # Exibe os totais de vendas por autor e os livros após 2010
    print("Totais de Vendas por Autor:")
    print(total_por_autor)

    print("\nLivros Publicados Após 2010:")
    print(livros_apos_2010)

def main():
    # Passo 1: Extração
    dados = extrair_dados()

    # Passo 2: Transformação
    total_por_autor, livros_apos_2010 = transformar_dados(dados)

    # Passo 3: Carregamento
    carregar_dados(total_por_autor, livros_apos_2010)

if __name__ == '__main__':
    main()
