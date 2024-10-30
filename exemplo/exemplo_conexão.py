from sqlalchemy import create_engine, text

# Variaveis de conexao com o banco

host = 'localhost'
user = 'root'
password = 'root'
database = 'bd_produtos'

# funçao para conectar ao banco 
def conecta_banco():
    try:
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

        # estabelecea a conexao
        with engine.connect() as conexao:
            query = 'SELECT * FROM vendas'
            resultados = conexao.execute(text(query))

            for item in resultados:
                print(f'{item[0]}, {item[1]}, {item[2]}')

    except ImportError as e:
        print(f'Erro: {e}')




# chama funçao que conecta ao banco de dados 
conecta_banco()

