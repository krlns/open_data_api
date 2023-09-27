<h1 align="center">
Open data api
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32" alt=""/>
</h1>

<p>✏️ Это API, предоставляющая сведения о кинотеатрах, зарегистрированных в единой информационной системе ✏️</p>
<hr>
<p>Для того, чтобы клонировать репозиторий, выполните команду:</p>

    git clone https://github.com/krlns/open_data_api.git
<hr>
<h3>Вы можете запустить API двумя способами:</h2>
<h3>1</h3>
<ul><li>

    cd locallibrary
</li></ul>
<ul><li>

    python manage.py makemigrations
</li></ul>
<ul><li>

    python manage.py migrate
</li></ul>
<ul><li>

    python manage.py run server
</li></ul>

<h3>2</h3>
<ul><li>

    docker-compose build
</li></ul>
<ul><li>

    docker-compose up -d
</li></ul>
<p>Чтобы остановить, выполните команду:</p>
<ul><li>

    docker ps
</li></ul>
<p>Скопируйте поле CONTAINER ID</p>
<ul><li>

    docker stop <CONTAINER ID>
</li></ul>

<p>Аналогично и для запуска</p>
<ul><li>

    docker start <CONTAINER ID>
</li></ul>
<hr>
<h3>Получить данные можно, добавив в url:

    /cinema
</h3>

<h3>также можно получить запись по его номеру:

    /cinema/<номер записи>
</h3>

