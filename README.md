
## ACS Store

**Clone repository:**

```
git clone https://github.com/dolyadima/acs_store.git
```

**Set your environment variables:**

```
cp .env.example .env
```

**Generating a SECRET_KEY using the terminal**

```
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

**Install requirements.txt:**

```
pip install -r requirements.txt
```

**Build and run containers:**

```
docker-compose build
docker-compose up
```
*after the first run, you need to restart CONTAINER-DB*

**Migrations, SuperUser, CollectStatic:**

```
docker exec -it CONTAINER-WEB bash
./manage.py migrate
./manage.py createsuperuser
./manage.py collectstatic
```

**Open your browser:**

```
http://0.0.0.0:80
```
