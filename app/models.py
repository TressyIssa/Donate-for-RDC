from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _
from django.utils import timezone

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """
    use_in_migrations = True
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        email = self.normalize_email(email)
        user = self.model(username=email, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    objects = UserManager()
    email = models.EmailField(_("email address"), unique=True)
    # Ajoutez related_name pour éviter les conflits avec le modèle par défaut de Django
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Nom personnalisé pour éviter les conflits
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Nom personnalisé pour éviter les conflits
        blank=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


class Projet(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
   
    
    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"

    def __str__(self):
       return self.name

class Don(models.Model):
    user = models.ForeignKey(User, related_name="don_user", on_delete=models.DO_NOTHING)
    sender = models.CharField(max_length=255, null=True, blank=True)
    receiver = models.CharField(max_length=255, null=True, blank=True)
    hash = models.CharField(max_length=255, null=True, blank=True, default="")
    montant = models.IntegerField(max_length=50, null=True, blank=True)
    projet = models.ForeignKey(Projet, related_name="projet", on_delete=models.DO_NOTHING, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    
    class Meta:
        verbose_name = "Don"
        verbose_name_plural = "Dons"



    
