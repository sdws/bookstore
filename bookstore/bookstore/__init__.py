import pymysql
#保证链接数据库的
pymysql.install_as_MySQLdb()

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.

from .celery import app as celery_app

__all__ = ['celery_app']