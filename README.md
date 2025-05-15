# reminder

*reminder* é um sistema Python projetado para enviar e-mails automáticos com lembretes programados. O sistema utiliza uma base de dados PostgreSQL para armazenar os lembretes e um servidor SMTP para enviar os e-mails.

## Para Utilizar

Para que o programa funcione corretamente, é interessante tem um banco de dados postgresql funcionando localmente, seja via docker ou realmente instalado na sua máquina.

Caso já esteja instalado na sua máquina, crie o arquivo .env e adicione as variáveis. Preencha de acordo.

```env
# Credenciais SMTP
PASSWORD=""
EMAIL=""

# Credenciais banco de dados
DATABASE=""
DB_USER=""
DB_PASSWORD=""
DB_CONTAINER=""
HOST="localhost"
PORT="5433"
```

Caso você prefira utilizar docker, vai abaixo um exemplo de *compose.yml* para utilização.

```yml
services:
  home-db:
    image: postgres:13
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5433:5432"

volumes:
  postgres_data:
```

Após subir o container e alterar no .env com as informações corretas, vamos ao script.

Para iniciar, execute os seguintes comandos:

```bash
# Execute um de cada vez para que não ocorram erros
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Após, o script já está funcional.

```bash
python main.py list
python main.py insert ""
python main.py delete ID
python main.py clear
python main.py send
```

## Link Simbólico

Caso você tenha reparado, existe um arquivo chamado *reminder.sh*.

Eu utilizo esse arquivo para criar um link simbólico para executar o script em qualquer lugar do meu terminal.

Segue comandos para criar esse link simbólico (Lembrando sempre de alterar os caminhos para os que correspondem a sua situação).

```bash
# O comando abaixo dá permissão de execução ao arquivo
chmod 775 reminder.sh 

# O comando abaixo cria o link simbólico e define o comando REMINDER como o nome do executor
sudo ln -s $HOME/Projects/python/send_mail_reminder/reminder.sh /bin/reminder

# Para executar
reminder list
reminder insert ""
reminder delete ID
reminder clear
reminder send
```

Bom, é isso.

Para dúvidas ou sugestões, entre em contato:
[linkedin](https://www.linkedin.com/in/pablodeas/)
[whatsapp](https://api.whatsapp.com/send?phone=5521966916139)