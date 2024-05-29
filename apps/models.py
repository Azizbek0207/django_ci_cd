import uuid
from uuid import UUID

from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db.models import Model, CharField, SlugField, ForeignKey, CASCADE, ImageField, IntegerField, DateTimeField, \
    TextField, UUIDField, FileField, ManyToManyField, OneToOneField, TextChoices
from django.forms import EmailField
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


class MainModel(Model):
    title = CharField(max_length=255)
    uuid = UUIDField(unique=True, default=uuid.uuid4, editable=False)
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Category(MainModel):
    pass


class Product(MainModel):
    price = IntegerField()
    description = CKEditor5Field()
    status = CharField(max_length=255)
    email = EmailField()
    location = CharField(max_length=255)
    category = ForeignKey('apps.Category', CASCADE)


class ProductImage(Model):
    product = ForeignKey('apps.Product', on_delete=CASCADE)
    image = ImageField(upload_to='products/')


class Course(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=255, unique=True)
    price = IntegerField()
    description = CKEditor5Field()
    video = FileField(upload_to='videos/', validators=[FileExtensionValidator(['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    category = ForeignKey('apps.CourseCategory', on_delete=CASCADE)
    users = ManyToManyField('apps.User', related_name='courses')


class CourseCategory(Model):
    name = CharField(max_length=255, unique=True)
    slug = SlugField(unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += ','
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class User(AbstractUser):
    class Status(TextChoices):
        ADMIN = 'admin', 'Admin'
        STUDENT = 'student', 'Student'
        TEACHER = 'teacher', 'Teacher'

    image = ImageField(upload_to='users/', blank=True)
    status = CharField(max_length=255, choices=Status.choices, default=Status.ADMIN)


class StudentProxyUser(User):
    class Meta:
        proxy = True
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class TeacherProxyUser(User):
    class Meta:
        proxy = True
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class AdminProxyUser(User):
    class Meta:
        proxy = True
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'
