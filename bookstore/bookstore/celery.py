import os
from celery import Celery

# set the default Django setting module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE','bookstore.settings')

app = Celery('bookstore',broker='redis://127.0.0.1:6379/6')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings',namespace='CELERY')

# Load task modules from all registered Django app configs.
# 从所有已注册的Django应用程序配置中加载任务模块。
# Load负荷; 装载; 负担; 工作量; 使担负; 装填; 把…装入或装上; 装满，堆积; 加载; 装货
# task作业; 工作，任务; 苦差事; 交给某人; 使过于劳累
# modules组件; 单元; 模块( module的名词复数 ); 舱
# registered注册的; 登记过的; 已挂号的; 附有血统证明的; 注册; 登记; 记录; 显出
# app计算机应用程序; 应用(Application); 穿甲试验(Armor Pi

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
	print('Request: {0!r}'.format(self.request))

