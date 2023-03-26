from django.db import models

from django.contrib.auth.models import AbstractUser


class CategoryCourse(models.Model):

    name = models.CharField('Название', max_length=255, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to='category_course_images/', null=True, blank=True)

    class Meta:
        verbose_name = 'Категория курса'
        verbose_name_plural = 'Категории курса'

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    
    name = models.CharField('Название', max_length=255, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateField('Дата создания', auto_now_add=True)
    description = models.TextField('Описание')
    duration_days = models.IntegerField('Длительность в днях', default=1)
    category = models.ForeignKey(CategoryCourse, related_name='cc_course', on_delete=models.PROTECT)
    is_stash = models.BooleanField('В архиве', default=False)
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class MyUser(AbstractUser):

    email = models.EmailField(unique=True, max_length=200)
    is_student = models.BooleanField('Студент', default=True)
    courses = models.ManyToManyField(Course, blank=True)


class CourseSchedule(models.Model):

    date = models.DateField('Дата')
    course = models.ForeignKey(Course, related_name='cs_course', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Расписание курсов'
        verbose_name_plural = 'Расписание курсов'


class Review(models.Model):

    rating = models.IntegerField('Рейтинг', default=1)
    description = models.TextField('Отзыв')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MyUser, related_name='review_user', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='review_course', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Faq(models.Model):

    question = models.CharField('Вопрос', max_length=255)
    answer = models.TextField('Ответ')

    class Meta:
        verbose_name = 'Вопрос/ответ'
        verbose_name_plural = 'Вопрос/ответ'


class News(models.Model):

    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self) -> str:
        return self.title
