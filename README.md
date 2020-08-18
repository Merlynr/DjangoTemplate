# DjangoTemplate
致敬Vamei

;生成数据库表
1.
$ python manage.py makemigrations
$ python manage.py migrate --fake-initial
;首次数据迁移 migrate 时，需要使用 --fake-initial 参数，因为数据库已经存在，不带 --fake 会报错且迁移不成功。