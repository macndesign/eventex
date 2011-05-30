# -*- coding: utf-8 -*-
from datetime import time
from django.db import models
from django.utils.translation import ugettext as _

# Create your managers here.
class KindContactManager(models.Manager):
    def __init__(self, kind):
        super(KindContactManager, self).__init__()
        self.kind = kind

    def get_query_set(self):
        qs = super(KindContactManager, self).get_query_set()
        qs = qs.filter(kind=self.kind)
        return qs

# Create your models here.
class Speaker(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    url = models.URLField(verify_exists=False)
    description = models.TextField(blank=True)
    avatar = models.FileField(upload_to='palestrantes', blank=True, null=True)

    def __unicode__(self):
        return self.name

class Contact(models.Model):
    KINDS = (
        ('P', _(u'Telefone')),
        ('E', _(u'E-mail')),
        ('F', _(u'Fax')),
    )

    speaker = models.ForeignKey('Speaker', verbose_name=_(u'Palestrante'))
    kind = models.CharField(max_length=1, choices=KINDS)
    value = models.CharField(max_length=255)

    objects = models.Manager()
    phones = KindContactManager('P')
    emails = KindContactManager('E')
    faxes = KindContactManager('F')

    def __unicode__(self):
        return u'%s, %s' % (self.kind, self.value)

class PeriodManager(models.Manager):
    midday = time(12)

    def at_morning(self):
        qs = self.filter(start_time__lt=self.midday)
        qs = qs.order_by('start_time')
        return qs

    def at_afternoon(self):
        qs = self.filter(start_time__gte=self.midday)
        qs = qs.order_by('start_time')
        return qs

class Talk(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.TimeField(blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name=_(u'Palestrante'))

    objects = PeriodManager()

    class Meta:
        verbose_name = _(u'Palestra')

    def __unicode__(self):
        return unicode(self.title)

class Course(Talk):
    slots = models.IntegerField()
    notes = models.TextField()

    objects = PeriodManager()

class CodingCourse(Course):
    class Meta:
        proxy = True

    def do_some_python_stuff(self):
        return "Let's hack! at %s" % self.title

class Media(models.Model):
    MEDIAS = (
        ('SL', 'SlideShare'),
        ('YT', 'YouTube'),
    )

    talk = models.ForeignKey('Talk')
    type = models.CharField(max_length=3, choices=MEDIAS)
    title = models.CharField(_(u'Título'), max_length=255)
    media_id = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s - %s' % (self.talk.title, self.title)
