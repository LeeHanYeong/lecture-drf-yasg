from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel

__all__ = (
    'Post',
    'Comment',
)


class Post(TimeStampedModel):
    title = models.CharField('제목', max_length=50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='작성자', on_delete=models.CASCADE)
    content = models.TextField('내용', blank=True)
    is_published = models.BooleanField('발행여부', default=False)

    class Meta:
        verbose_name = '글'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return f'{self.author.username} | {self.title}'


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, verbose_name='글', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='작성자', on_delete=models.CASCADE)
    content = models.TextField('내용', blank=True)

    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return f'{self.post.title} | {self.content[:20]}'
