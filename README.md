# reminder

## Visão Geral

*reminder* é um sistema Python projetado para enviar e-mails automáticos com lembretes programados. O sistema utiliza uma base de dados PostgreSQL para armazenar os lembretes e um servidor SMTP para enviar os e-mails.

## Funcionalidades Principais

- Adicionar novos lembretes
- Listar todos os lembretes existentes  
- Excluir lembretes individuais ou todos
- Enviar e-mails com lembretes programados

## Como Usar

1. Instale as dependências:
   ```
   pip install click psycopg2-binary load_dotenv
   ```

2. Configure as variáveis de ambiente no arquivo .env:
   - PASSWORD
   - EMAIL
   - DATABASE
   - DB_USER
   - DB_PASSWORD
   - HOST
   - PORT

3. Execute o script Python:
   ```
   python main.py
   ```

4. Use os seguintes comandos:
   - `python main.py list` - Lista todos os lembretes
   - `python main.py insert <mensagem>` - Adiciona um novo lembrante  
   - `python main.py delete <id>` - Exclui um lembrante por ID
   - `python main.py clear` - Exclui todos os lembretes
   - `python main.py send` - Envia e-mails com lembretes programados

## Requisitos

- Python 3.6+
- PostgreSQL
- SMTP server configurado