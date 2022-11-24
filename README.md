
## ACS Store

**Clone repository:**

```
git clone https://github.com/dolyadima/acs_store.git
```

**Set your environment variables:**

```
cp .env.example .env
```

**Set environment for dev:**

```
cp .env.dev .env
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
