# Публичен сайт на Общество

Публичният сайт на http://www.obshtestvo.bg.

## Инсталация на проекта (за програмисти)

Проектът е написан на Python и Django и използва MySQL.

### В среда за разработване (development)

1. Нужен ви е Python 2.7. Проектът не е тестван на други версии.
2. Трябва да имате MySQL 5.x, плюс header файлове.
3. Инсталирайте pip, ако нямате – `easy_install pip` или `sudo easy_install pip`
4. Инсталирайте virtualenvwrapper – `pip install virtualenvwrapper` или `sudo pip install virtualenvwrapper`.
5. Заредете командите на virtualenvwrapper: `source /usr/local/bin/virtualenvwrapper.sh` – дава достъп до `mkvirtualenv` и други.
6. `mkvirtualenv obshtestvobg --no-site-packages` – ще създаде виртуална среда за инсталиране на pip пакети в `~/.virtualenvs/obshtestvobg`.
7. `workon obshtestvobg` за да превключите на това обкръжение.
8. Зависимостите на проекта: `pip install -r requirements.txt`

    Ако компилацията на MySQL адаптера не мине, може да се наложи да се изпълни `export CFLAGS=-Qunused-arguments` ([реф.](http://stackoverflow.com/questions/22313407/clang-error-unknown-argument-mno-fused-madd-python-package-installation-fa)) и да се стартира отново командата.

9. Създайте база данни в MySQL:

        CREATE DATABASE obshtestvo CHARACTER SET utf8 COLLATE utf8_general_ci

10. Създайте файл със специфичните за локалното ви копие настройки, като копирате `server/settings_app.py.sample` като `server/settings_app.py` и въведете в копието:

    - данните за достъп до MySQL базата данни
    - редактирайте пътя в `STATIC_ROOT`

11. Подгответе базата за първото пускане на миграциите: `python manage.py syncdb`
12. Пуснете миграциите: `python manage.py migrate`
13. Направете си админ потребител с `python manage.py createsuperuser`
14. Пуснете си сървър с `python manage.py runserver`
15. Deploy those files by configuring your webserver of choice to serve the files in STATIC_ROOT at STATIC_URL.

### Production

- По време на deployment: `python manage.py collectstatic -l`
- Генерирайте нова стойност на `SECRET_KEY`.
- Променете `DEBUG = True` на `DEBUG = False`.


#### Общи
 - pip (python package manager)
 - django
 - virtualenvwrapper
 - mysql driver and its dependencies

#### Production
 - nginx server
 - uwsgi server
 - uwsgi python plugin

#### Инсталация на изискванията (на debian-базирана машина)

##### Генерални

```sh
sudo apt-get install nginx-full uwsgi uwsgi-plugin-python python-pip
sudo pip install django virtualenvwrapper
```
и за mysql:

```sh
sudo apt-get install libmysqlclient-dev python-dev
```

##### За production

```sh
apt-get install nginx-full uwsgi uwsgi-plugin-python
```

Ако се ползва външното repository за debian на nginx (за по-нова версия):

```sh
apt-get install nginx uwsgi uwsgi-plugin-python
```

### Инсталация на проекта

```sh
source /usr/local/bin/virtualenvwrapper.sh # to have the mkvirtualenv commands, etc.
mkvirtualenv obshtestvobg --no-site-packages #this will create a virtual environment at ~/.virtualenvs/obshtestvobg
workon obshtestvobg
pip install django # even if you have django, install it in the virtual env
pip install mysql-python # mysql...
pip install -r requirements.txt # for the required packages
# sudo ln -s ~/.virtualenvs/obshtestvobg/lib/python2.7/site-packages/django/contrib/admin/static/admin static
python manage.py collectstatic -l
```

### Подкарване


Копирайте си server/settings_app.py.sample като server/settings_app.py и оправете в него настройките:

- Генерирайте нов SECRET_KEY (apg -m32 например);
- Сложете настройките на базата данни;
- Вероятно може да закоментирате STATICFILES_DIRS;
- Ако ще го разработвате, сложете DEBUG=True;

#### Начални стъпки да може да се разработва

```
django-admin.py runserver --settings=settings --pythonpath=/home/ubuntu/projects/obshtestvo.bg  --insecure
```

```
# initial database installation
# for production you just can get the DB from the running site
python manage.py syncdb
python manage.py migrate
```

#### Когато вече сайта е готов и е пуснат / Production server
Редактирайте домейна в `settings_nginx.optimised.conf` и `settings_nginx.basic.conf`.

##### Настройки за `nginx`

Проверете и в двата файла дали има да настройвате пътища.

```sh
# basic (no caching, no tweaking):
sudo ln -s /home/ubuntu/projects/obshtestvo.bg/server/settings_nginx.basic.conf /etc/nginx/sites-enabled/obshtestvobg.conf
# optimised
sudo ln -s /home/ubuntu/projects/obshtestvo.bg/server/settings_nginx.optimised.conf /etc/nginx/sites-enabled/obshtestvobg.conf
```
При nginx от официалното ngix repo:

```sh
# basic (no caching, no tweaking):
sudo ln -s /home/ubuntu/projects/obshtestvo.bg/server/settings_nginx.basic.conf /etc/nginx/conf.d/obshtestvobg.conf
# optimised
sudo ln -s /home/ubuntu/projects/obshtestvo.bg/server/settings_nginx.optimised.conf /etc/nginx/conf.d/obshtestvobg.conf
```


Които се активират с :
```sh
sudo service nginx restart
```

##### Настройки за `uwsgi`

Проверете какво има да настроите във файла.

```sh
# debian/ubuntu/mint...:
sudo ln -s /home/ubuntu/projects/obshtestvo.bg/server/settings_uwsgi.ini /etc/uwsgi/apps-enabled/obshtestvobg.ini
# fedora/centos/redhat...
sudo ln -s /home/ubuntu/projects/obshtestvo.bg/server/settings_uwsgi.ini /etc/uwsgi.d/obshtestvobg.ini
```

Които се активират с :
```
sudo service uwsgi restart
```

##### Опресняване на направени промени

```
sudo service uwsgi reload && sudo service nginx reload
```

##### Почистване на кеша на production системата

```
find /var/cache/nginx/ -type f | xargs rm
```
