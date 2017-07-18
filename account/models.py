from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import  timezone
from django.db import IntegrityError
# Create your models here.




class UserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, email, password=None,username="default", **kwargs):
        try:
            user = self.model(
                email=self.normalize_email(email),
                is_active=True,
                **kwargs
            )
            user.set_password(password)
            user.save(using=self._db)
            return user
        except IntegrityError:
            return

    def create_superuser(self, email, password, **kwargs):
        user = self.model(
            email=email,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    USERNAME_FIELD = "email"
    email = models.EmailField(_('email address'), max_length=254, unique=True, db_index=True)
    username = models.CharField(_('username'), max_length=500, blank=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = "pb_user"

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class PbUserOauthToken(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="access_token")
    linkedin = models.CharField(max_length=1000,null=True,default=None)
    facebook = models.CharField(max_length=1000,null=True,default=None)
    twitter_access_token = models.CharField(max_length=1000,null=True,default=None)
    twitter_access_token_secret = models.CharField(max_length=1000, null=True, default=None)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


def photo_upload_path(instance,filename):
    return "".join(["%s%s%s%s" %("profile-photo/",str(instance.first_name),str(instance.last_name),"/"),filename])


class PbProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(blank=True, default="default_avatar.jpg", upload_to=photo_upload_path)

    class Meta:
        # managed = False
        db_table = 'pb_profile'

