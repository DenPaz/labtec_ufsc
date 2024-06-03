# LabTec UFSC

Site em desenvolvimento...

## Comandos para rodar o projeto localmente

- Clonar o repositório:

```bash
git clone https://github.com/DenPaz/labtec_ufsc.git
cd labtec_ufsc
```

- Configurar ambiente virtual:

```bash
python -m venv venv
```

- Ativar ambiente virtual:

```bash
# Windows
venv\Scripts\activate

# Linux
source venv/bin/activate
```

- Instalar dependências:

```bash
pip install -r requirements/local.txt
```

- Criar migrações:

```bash
python manage.py makemigrations
```

- Aplicar migrações:

```bash
python manage.py migrate
```

- Criar superusuário:

```bash
python manage.py createsuperuser
```

- Rodar servidor de desenvolvimento:

```bash
python manage.py runserver
```

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
