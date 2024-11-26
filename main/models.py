from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError


# from django.core.validators import ImageValidator


class User(AbstractUser):
    pass


class Company(models.Model):
    name = models.CharField(max_length=500, verbose_name='Kompaniya Nomi')
    description = models.TextField(verbose_name='Batafsil')
    slogan = models.TextField(verbose_name='Shior', null=True, blank=True)
    aim = models.TextField(verbose_name='Maqsad', null=True, blank=True)
    main_tasks = models.TextField(verbose_name='Asosiy vazifalar', null=True, blank=True)

    def __str__(self):
        return self.name


def validate_url(url):
    # validate url using a library or function
    # for example, using validators.URLValidator
    from django.core.validators import URLValidator
    validator = URLValidator()
    validator(url)
    return True


class Videourl(models.Model):
    video_url = models.URLField(verbose_name='Video linki', validators=[validate_url], null=True, blank=True)
    telegram_channel_url = models.URLField(verbose_name='Telegram kanal linki', validators=[validate_url], null=True, blank=True)    
    telegram_account_url = models.URLField(verbose_name='Telegram account linki', validators=[validate_url], null=True, blank=True)
    def __str__(self):
        return str(self.video_url)
    
    class Meta:
        verbose_name = 'Video Havolasi'
        verbose_name_plural = 'Video Havolar'
        # ordering
        ordering = ['-id']


def validate_logo(logo):
    # print(logo.name)
    # print('-------------\n--------------')
    # print('-------------\n--------------')
    # print(type(logo.name))
    # print('--------------------\n----------------')
    # print('--------------------\n----------------')
    # # validate logo using a library or function
    # # for example, using validators.ImageValidator
    # # validator = ImageValidator()
    # # validator(logo)
    return True


class Logo(models.Model):
    logo = models.ImageField(verbose_name='Logo', upload_to='logo/', validators=[validate_logo])
    
    def __str__(self):
        return str(self.logo.name)
    
    class Meta:
        verbose_name = 'Kompaniya Logosi'
        verbose_name_plural = 'Kompaniya Logolari'
        # ordering
        ordering = ['-id']


class HeroTitle(models.Model):
    title = models.CharField(verbose_name='Sarlavha', max_length=255)
    
    def __str__(self):
        return str(self.title)


class Hamkorlar(models.Model):
    hamkor = models.CharField(verbose_name='Hamkor', max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='hamkorlar/', verbose_name='hamkor rasmi')
    
    def __str__(self):
        return str(self.hamkor)
    
    class Meta:
        verbose_name = 'Hamkor'
        verbose_name_plural = 'Hamkorlar'


class Activity(models.Model):
    activity_name = models.CharField(verbose_name='Faoliyat Nomi', max_length=255)
    activity_description = models.TextField(verbose_name='Faoliyat haqida')
    activity_photo = models.ImageField(upload_to='FaoliyatRasmlar/', verbose_name='Faoliyat rasmi')
    
    def __str__(self):
        return str(self.activity_name)
    
    class Meta:
        verbose_name = 'Vazifa'
        verbose_name_plural = 'Vazifalar'

class ActivityPhotos(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name='Faoliyat', related_name='photos')
    photo = models.ImageField(upload_to='FaoliyatRasmlar/', verbose_name='Faoliyat rasmi')
    
    def __str__(self):
        return str(self.activity.activity_name)
    
    class Meta:
        verbose_name = 'Faoliyat Rasmi'
        verbose_name_plural = 'Faoliyat Rasmlari'
        ordering = ['activity']


class Team(models.Model):
    full_name = models.CharField(max_length=300)
    position = models.CharField(max_length=300, verbose_name='Mutaxassisligi',null=True, blank=True)
    rank = models.CharField(max_length=250, verbose_name='Lavozim', null=True, blank=True)
    telegram_url = models.URLField(verbose_name='Telegram link', null=True, blank=True)
    facebook_url = models.URLField(verbose_name='Facebook link', null=True, blank=True)
    twitter_url = models.URLField(verbose_name='Twitter link', null=True, blank=True)
    instagram_url = models.URLField(verbose_name='Instagram link', null=True, blank=True)
    image = models.ImageField(upload_to='team/', validators=[validate_logo], default='user.png')

    def __str__(self):
        return self.full_name + " | " + self.rank
    
    class Meta:
        verbose_name = 'Jamoa'
        verbose_name_plural = 'Jamolar'
        ordering = ['rank']


# validate min 1 max 5 for rate field, MinValidator, MaxValudator
def validate_rate(value):
    if value < 1 or value > 5:
        raise ValidationError('Rate must be between 1 and 5')


class Reviews(models.Model):
    photo = models.ImageField(upload_to='mijozlar/', default='user.png', validators=[validate_logo], verbose_name='mijoz rasmi')
    full_name = models.CharField(max_length=300, verbose_name='Mijoz F.I.SH')
    type = models.CharField(max_length=300, verbose_name='Lavozimi/Yo\'nalishi', null=True, blank=True)
    rate = models.PositiveIntegerField(default=5, validators=[validate_rate])
    comment = models.TextField(verbose_name='Izoh')

    def __str__(self):
        return self.full_name +  "  :   " + self.comment[:20] 
    
    class Meta:
        verbose_name = 'Mijoz Izoh'
        verbose_name_plural = 'Mijozlar Izohlar'
        ordering = ['-id']


class FAQ(models.Model):
    question = models.CharField(max_length=500, verbose_name='Savol')
    answer = models.TextField(verbose_name='Javob')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question[:50] + "..."
    
    class Meta:
        verbose_name = 'FAQ Savol-Javob'
        verbose_name_plural = 'FAQ Savol-Javoblar'


class Contact(models.Model):
    address = models.CharField(max_length=400, verbose_name='Manzil', null=True, blank=True)
    phone_number = models.CharField(max_length=400, verbose_name='Telefon raqam', null=True, blank=True)
    email = models.CharField(max_length=400, verbose_name='Elektron pochta', null=True, blank=True)
    karta = models.URLField(validators=[validate_url], null=True, blank=True)

    def __str__(self):
        return "Manzil: " + self.address + "\nTelefon raqam: " + self.phone_number + "\nElektron pochta: " + self.email
    
    class Meta:
        verbose_name = 'Manzil'
        verbose_name_plural = 'Manzillar'


class SocialMedia(models.Model):
    telegram_url = models.URLField(verbose_name='Telegram link', null=True, blank=True)
    facebook_url = models.URLField(verbose_name='Facebook link', null=True, blank=True)
    twitter_url = models.URLField(verbose_name='Twitter link', null=True, blank=True)
    instagram_url = models.URLField(verbose_name='Instagram link', null=True, blank=True)

    def __str__(self):
        return "Telegram: " + self.telegram_url + "\nFacebook: " + self.facebook_url + "\nTwitter: " + self.twitter_url + "\nInstagram: " + self.instagram_url
    
    class Meta:
        verbose_name = 'Social Media Link'
        verbose_name_plural = 'Social Media Linklar'
    

class Takliflar(models.Model):
    full_name = models.CharField(max_length=500, verbose_name='F.I.SH')
    phone_number = models.CharField(max_length=500, verbose_name='Telefon raqam')
    message = models.TextField(verbose_name='Xabar')

    def __str__(self):
        return self.full_name + "  :   " + self.message[:20]
    
    class Meta:
        verbose_name = 'Taklif'
        verbose_name_plural = 'Takliflar'
        ordering = ['-id']
