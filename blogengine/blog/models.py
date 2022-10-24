import logging
from hashlib import md5
from time import time

from django.db import models
from django.shortcuts import reverse, redirect, resolve_url

logger = logging.getLogger(__name__)


class BaseBlogObject(models.Model):
    title = models.CharField(max_length=150, db_index=True, unique=True)
    instance_id = models.CharField(max_length=16, unique=True, null=True)

    singular_obj_name = 'объект'
    plural_obj_name = 'объекты'

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.instance_id = self.gen_instance_id(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        url = self.__class__.__name__.lower() + '_detail_url'
        logger.info(f"{url=}")
        return reverse(url, kwargs={'instance_id': self.instance_id})

    @staticmethod
    def gen_instance_id(title: str):
        raw_str = str(time()) + title
        return md5(raw_str.encode()).hexdigest()

    @classmethod
    def get_list_url(cls):
        list_url = cls.__name__.lower() + '_list_url'
        logger.info(f"{list_url=}")
        return reverse(list_url)

    @classmethod
    def get_create_url(cls):
        create_url = cls.__name__.lower() + '_create_url'
        logger.info(f"{create_url=}")
        return reverse(create_url)

    def get_update_url(self):
        url = self.__class__.__name__.lower() + '_update_url'
        logger.info(f"{url=}")
        return reverse(url, kwargs={'instance_id': self.instance_id})

    def get_delete_url(self):
        url = self.__class__.__name__.lower() + '_delete_url'
        logger.info(f"{url=}")
        return reverse(url, kwargs={'instance_id': self.instance_id})


class Post(BaseBlogObject):
    title = models.CharField(max_length=150, db_index=True, unique=True)
    instance_id = models.CharField(max_length=16, unique=True, null=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    singular_obj_name = 'пост'
    plural_obj_name = 'посты'

    class Meta:
        ordering = ['-date_pub']


class Tag(BaseBlogObject):
    title = models.CharField(max_length=50, unique=True)
    instance_id = models.CharField(max_length=16, unique=True, null=True)

    singular_obj_name = 'тэг'
    plural_obj_name = 'тэги'

    class Meta:
        ordering = ['title']

