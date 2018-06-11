from django.db import models

class BaseModel(models.Model):
	#模型抽象基类
	is_delete = models.BooleanField(default=False,verbose_name='删除标记')
	create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
	update_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')
#Django 模型类的Meta是一个内部类，它用于定义一些Django模型类的行为特性。
	class Meta:
		#这个属性是定义当前的模型类是不是一个抽象类。所谓抽象类是不会对应数据库表的。一般我们用它来归纳一些公共属性字段，然后继承它的子类可以继承这些字段。
		abstract = True

