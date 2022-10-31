### Необходимые шаги для запуска тестов Перед запуском тестов необходимо ввести ваши данные в следующие файлы:

В файле test_project / config / config.json заполнить поля client_key, client_secret, resource_owner_key,resource_owner_secret

### Установка и сборка репозетория Склонируйте данный репозиторий с github

### В скаченном репозитории из корня каталога, выполните в консоли команду:

pip install -r requirements.txt

### Запуск тестов Необходимо перейти в директорию /test_project/tests/ и выполнить команду
url для запуска =  https://api.tumblr.com <br>

python -m pytest <test_name>

pytest --html=report.html --base_url=123 -k test
