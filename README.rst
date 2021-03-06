Задача для Smart Space
======================
Тестовая задача для Smart Space.

Описание
--------
Сервис для перемножения матриц с использованием распараллеливания задач.

Доступные методы
----------------

``POST /multiply Content-Type: application/json``

``in: {"first":[[],[],..], "second":[[],[],..]}``

``out: {"job_id":""}``

``-------------------------------------------``


``GET /status/{job_id}``

``out: {"status":""}``

``-------------------------------------------``


``GET /result/{job_id}``

``out: {"status":"", "result":[[],[],..]}``


Особенности
-----------
Так как матрицы могут быть любого размера, чтобы ускорить перемножение
матрицы разбиваются на подматрицы, вычисляются промежуточные результаты,
которые впоследствии собираются в финальную матрицу.

Подзадачи запускаются с помощью Celery, для хранения промежуточных
результатов (celery backend) используется Redis.

TODO
----
- Если job_id невалидный, то будет возвращаться status: PENDING из-за дефолтного
  поведения Celery. Необходимо обрабатывать job_id руками.
- Сделать имплементацию алгоритма с разбиением на квадратные подматрицы.
  Он гораздо быстрее простого параллельного алгоритма, который сейчас реализован.
- Хранить как промежуточные, так и финальные результаты в БД.