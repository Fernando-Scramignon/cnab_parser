# cnab_parser

## descrição

Esse é um projeto que permite a conversão de um arquivo cnab simples por meio de requisições normais e upload de arquivos txt.

## Início Rápido

- **Criação do ambiente virtual**

```python
python -m venv venv
```

Se você está no windows, precisa permitir a criação do ambiente virtual
```bash
Set-ExecutionPolicy AllSigned
```
<br>

- **Entre no ambiente virtual**

linux:
```
source venv/bin/activate
```

windows:
```
.\venv\Scripts\activate
```

<br>

- **Instalando dependências**

Esse comando instala recursivamente todas as dependências no arquivo requirements.txt

```python
pip install -r requirements.txt
```

<br>

- **Rodando migrations**

Isso vai criar as tabelas do banco de dados e popular a tabela de tipos com os valores default

```python
./manage.py migrate
```

<br>

- **Rodando o servidor**

Esse comando vai rodar o servidor em http://localhost:8000/

```python
./manage.py runserver
```

<br>

- **Rotas da documentação**

Se tudo foi configurado corretamente, você será capaz de acessar a documentação das rotas por essas urls

http://localhost:8000/api/docs/
<br>
http://localhost:8000/api/docs/swagger-ui/

O primeiro é o download de um arquivo yaml e o segundo a interface da documentação.
<br>
A porta pode variar dependendo de onde o servidor está rodando. A porta padrão é 8000.
