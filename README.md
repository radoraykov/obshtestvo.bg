# Публичен сайт на Общество

Публичният сайт на http://www.obshtestvo.bg.

## Инсталация на проекта (за програмисти)

Проектът е написан на Python и Django и използва MySQL.

### Development среда

1. Нужен ви е Python 2.7. Проектът не е тестван на други версии.
2. Трябва да имате MySQL 5.x, плюс header файлове.
3. Инсталирайте pip, ако нямате – `easy_install pip` или `sudo easy_install pip`
4. Инсталирайте virtualenvwrapper – `pip install virtualenvwrapper` или `sudo pip install virtualenvwrapper`.
5. Заредете командите на virtualenvwrapper: `source /usr/local/bin/virtualenvwrapper.sh` – дава достъп до `mkvirtualenv` и други.
6. `mkvirtualenv obshtestvobg --no-site-packages` – ще създаде виртуална среда за инсталиране на pip пакети в `~/.virtualenvs/obshtestvobg`.
7. `workon obshtestvobg` за да превключите на това обкръжение.
8. Клонирайте хранилището и влезте в директорията на проекта.
9. Зависимостите на проекта: `pip install -r requirements.txt`

    Ако компилацията на MySQL адаптера не мине, може да се наложи да се изпълни `export CFLAGS=-Qunused-arguments` ([реф.](http://stackoverflow.com/questions/22313407/clang-error-unknown-argument-mno-fused-madd-python-package-installation-fa)) и да се стартира отново командата.
10. Създайте база данни в MySQL:

        CREATE DATABASE obshtestvo CHARACTER SET utf8 COLLATE utf8_general_ci
11. Създайте файл със специфичните за локалното ви копие настройки, като копирате `server/settings_app.py.sample` като `server/settings_app.py` и въведете там параметрите за достъп до MySQL базата данни.
12. Подгответе базата за първото пускане на миграциите: `python manage.py syncdb`
13. Пуснете миграциите: `python manage.py migrate`
14. Направете си админ потребител с `python manage.py createsuperuser`
15. Пуснете си сървър с `python manage.py runserver`

Би трябвало да може да достъпите приложението на [http://localhost:8000/](http://localhost:8000/).

### Production среда

Инсталирайте приложението, използвайки инструкциите в предишната секция, с тези разлики:

1. В `server/settings_app.py`:

	- Променете `DEBUG = True` на `DEBUG = False`.
	- Генерирайте нова стойност на `SECRET_KEY`.

2. Настройте уеб сървъра си да сервира статичните файлове, намиращи се в `STATIC_ROOT` (обикновено папката `static/` в корена на проекта) на URL `/static/`.
3. Уверете се, че по време на deployment се изпълнява командата `python manage.py collectstatic -l`, за да се копират статичните файлове от приложението в `STATIC_ROOT`.
4. Използвайте Nginx или Apache сървър, плюс uwsgi server и uwsgi python plugin. Могат да се използват съответните конфигурационни файлове в папка `server/`.

### Deployment

След първоначалната инсталация, проектът се качва на сървъра с `fab deploy`. Процедурата е:

1. Правите промени.
2. `git commit` и `git push` на промените.
3. Изпълнявате `fab deploy` от корена на вашето локално копие.

Скриптът за deploy върши доста от нещата, описани в предишните секции. Прегледайте конфигурацията във `fabfile.py` и редактирайте по ваше желание.

### Примерна инсталация на Debian-базирана машина

Общи пакети за development и production:

```sh
sudo apt-get install nginx-full uwsgi uwsgi-plugin-python python-pip
sudo pip install django virtualenvwrapper
```

MySQL:

```sh
sudo apt-get install libmysqlclient-dev python-dev
```

Пакети, необходими само на production:

```sh
apt-get install nginx-full uwsgi uwsgi-plugin-python
```

Ако се ползва външното repository за debian на nginx (за по-нова версия):

```sh
apt-get install nginx uwsgi uwsgi-plugin-python
```

Подкарване на проекта:

```sh
source /usr/local/bin/virtualenvwrapper.sh # to have the mkvirtualenv commands, etc.
mkvirtualenv obshtestvobg --no-site-packages #this will create a virtual environment at ~/.virtualenvs/obshtestvobg
workon obshtestvobg
pip install django # even if you have django, install it in the virtual env
pip install mysql-python # mysql...
pip install -r requirements.txt # for the required packages
python manage.py collectstatic -l
```

#### Настройки на Nginx и uwsgi в production

Редактирайте домейна в `settings_nginx.optimised.conf` и `settings_nginx.basic.conf`.

##### Настройки за `nginx`

Проверете и в двата файла дали има да настройвате пътища.

```sh
# basic (no caching, no tweaking):
sudo cp /path/to/projects/obshtestvo.bg/server/settings_nginx.basic.conf.sample /etc/nginx/sites-enabled/obshtestvobg.conf
# optimised
sudo cp /path/to/projects/obshtestvo.bg/server/settings_nginx.optimised.conf.sample /etc/nginx/sites-enabled/obshtestvobg.conf
```

При nginx от официалното nginx repo:

```sh
# basic (no caching, no tweaking):
sudo cp /path/to/projects/obshtestvo.bg/server/settings_nginx.basic.conf.sample /etc/nginx/conf.d/obshtestvobg.conf
# optimised
sudo cp /path/to/projects/obshtestvo.bg/server/settings_nginx.optimised.conf.sample /etc/nginx/conf.d/obshtestvobg.conf
```

Които се активират с :

```sh
sudo service nginx restart
```

##### Настройки за `uwsgi`

Проверете какво има да настроите във файла.

```sh
# debian/ubuntu/mint...:
sudo cp /path/to/projects/obshtestvo.bg/server/settings_uwsgi.ini.sample /etc/uwsgi/apps-enabled/obshtestvobg.ini
# fedora/centos/redhat...
sudo cp /path/to/projects/obshtestvo.bg/server/settings_uwsgi.ini.sample /etc/uwsgi.d/obshtestvobg.ini
```

Които се активират с:

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
