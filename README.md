Сайт за http://www.obshtestvo.bg


## Инсталация (за програмисти)

### Изисквания

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
# sudo ln -s ~/.virtualenvs/obshtestvobg/lib/python2.7/site-packages/django/contrib/admin/static/admin ./static/
python manage.py collectstatic -l
```

### Подкарване


Копирайте си server/settings_app.py.sample като server/settings_app.py и оправете в него настройките:

Генерирайте нов SECRET_KEY (apg -m32 например);
Сложете настройките на базата данни;
Вероятно може да закоментирате STATICFILES_DIRS;

#### Когато още се разработва

```
django-admin.py runserver --settings=settings --pythonpath=/home/ubuntu/projects/obshtestvo.bg  --insecure
```

```
# initial:
python manage.py syncdb
# and
python manage.py convert_to_south projects
python manage.py migrate projects 0001 --fake
# OR
python manage.py schemamigration projects --initial
# on changes:
python manage.py schemamigration projects --auto
python manage.py migrate projects
# update last migraiton:
python manage.py schemamigration projects --auto --update
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
