from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from guardian.shortcuts import assign_perm
from django.utils import timezone
# from django.contrib.contenttypes.models import ContentType
# from django.db.models import Q
# from guardian.models import UserObjectPermission, GroupObjectPermission


# def remove_perobject_permissions(sender, instance, **kwargs):
#     filters = Q(content_type=ContentType.objects.get_for_model(instance),
#                 object_pk=instance.pk)
#     UserObjectPermission.objects.filter(filters).delete()
#     GroupObjectPermission.objects.filter(filters).delete()


class Organisation(models.Model):
    class Meta:
        verbose_name = _('organisation')
        verbose_name_plural = _('organisations')
    name = models.CharField(_('name'), max_length=200,)
    strategy = models.TextField(_('strategy'), blank=True)
    middlemen = models.ManyToManyField('Member', related_name="middleman_organisations", blank=True,null=True,
                                      verbose_name=_("middle men"))
    representatives = models.CharField(_('Representative'), max_length=30, blank=True)

    found_via = models.CharField(_('Found via'), max_length=30, blank=True)
    contact = models.TextField(_('contact info'), blank=True)
    comment = models.TextField(_('comment'), blank=True)
    working_with = models.TextField(_('Also working with'), blank=True)

    is_sponsor = models.BooleanField(_('Has funding programme?'), default=False)
    is_provider = models.BooleanField(_('Provides free product?'), default=False)

    partnered_project = models.ForeignKey('Project', related_name="partners", blank=True, null=True, verbose_name=_("partnered project"))
    provided_help = models.TextField(_('Provided help'), blank=True)

class Skill(models.Model):
    class Meta:
        verbose_name = _('skill')
        verbose_name_plural = _('skills')
    name = models.CharField(_('name'), max_length=200,)

    def __unicode__(self):
        return self.name

class MemberType(models.Model):
    class Meta:
        verbose_name = _('member type')
        verbose_name_plural = _('member types')
    name = models.CharField(_('name'), max_length=200,)

    def __unicode__(self):
        return self.name

class Member(models.Model):
    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')
    DAILY = 'd'
    WEEKLY = 'w'
    EVERY_TWO_WEEKS = '2w'
    EVERY_MONTH = '1m'
    EVERY_QUARTER = '2w'
    CONTACT_FREQUENCY_CHOICE = (
        (DAILY, 'Almost every day'),
        (WEEKLY, 'Once a week'),
        (EVERY_TWO_WEEKS, 'Every two weeks'),
        (EVERY_MONTH, 'Once a month'),
        (EVERY_QUARTER, 'Once a couple of months'),
    )

    user = models.ForeignKey('User', related_name="member", blank=True, null=True)
    update_from_user = models.BooleanField(_('Daily sync from associated user?'), default=False)

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    name = models.CharField(_('name'), max_length=30, blank=False)
    email = models.EmailField(_('email address'), blank=True)
    facebook = models.CharField(_('facebook profile'), max_length=255, blank=True)
    working_on = models.ForeignKey('Project', related_name="working_members", blank=True, null=True, verbose_name=_("working on"))
    is_active = models.BooleanField(_('Active right now?'), default=False)
    skills = models.ManyToManyField('Skill', related_name="members", blank=True,
                                      verbose_name=_("skills"))

    intro = models.TextField(_('intro'), blank=True)
    comment = models.TextField(_('comment'), blank=True)
    offered_help = models.TextField(_('Type of helped offered'),
                                    blank=True,
                                    help_text=_("If it's a consultant or other non-member, you can add some description here"))

    is_available = models.BooleanField(_('Available for work?'), default=False)
    available_after = models.DateField(_('available after'), blank=True, null=True)

    last_contacted_at = models.DateField(_('last contact'), blank=True, null=True)
    latest_answer = models.TextField(_('latest answer'), blank=True)
    contact_frequency = models.CharField(max_length=2,
                                      choices=CONTACT_FREQUENCY_CHOICE,
                                      default=DAILY,
                                      verbose_name=_("Contact frequency"))

    will_help = models.BooleanField(_('Ever going to help?'), default=True)
    is_paid_only = models.BooleanField(_('Paid only'), default=False)
    types = models.ManyToManyField('MemberType', related_name="members", blank=True, verbose_name=_("Relation to Obshtestvo"))
    projects_interests = models.ManyToManyField('Project', blank=True, related_name="interested_members", verbose_name=_("Projects interested in"))

    def __unicode__(self):
        return self.name

    def sync_with(self, user):
        pass

    def override(self, user):
        pass

    def fill_gaps_to(self, user):
        pass

    def fill_gaps_from(self, user):
        pass

def user_file_name(instance, filename):
    return '/'.join(['static/upload', 'user', filename])

class User(AbstractUser):
    profession = models.CharField(_('profession'), max_length=30, blank=False)
    is_available = models.BooleanField(_('Is the user available for work'), default=False)
    available_after = models.DateField(_('available after'), blank=True, null=True)
    has_confirmed_data = models.BooleanField(_('has confirmed custom data'), default=True)
    bio = models.TextField(_('biography'))
    avatar = models.FileField(_('avatar'), upload_to=user_file_name)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        abstract = False

class UserPointSpending(models.Model):
    person = models.ForeignKey('User', related_name="spendings")
    points = models.PositiveIntegerField(_('points'), max_length=10)
    product = models.CharField(_('profession'), max_length=30, blank=False)


# @receiver(post_save, sender=User)
# def user_perobject_permissions(sender, instance, **kwargs):
#     assign_perm('change_user', instance, instance)
#
#
# @receiver(pre_delete, sender=User)
# def remove_user_perobject_permissions(sender, instance, **kwargs):
#     UserObjectPermission.objects.filter(user_id=instance.pk).delete()
#     GroupObjectPermission.objects.filter(user_id=instance.pk).delete()


class UserActivity(models.Model):
    person = models.ForeignKey('User', related_name="activities")
    project_activity = models.ForeignKey('ProjectActivity',
                                         related_name="user_activities")
    progress = models.IntegerField(_('progress made'), max_length=3)
    is_active = models.BooleanField(_('active'), default=True)
    last_stopped_at = models.DateTimeField(_('last time user stopped working on this'),
                                           blank=True, null=True)
    needs_replacement = models.BooleanField(_('user needs replacement'), default=False)

    class Meta:
        unique_together = ('person', 'project_activity',)
        verbose_name_plural = "User Activities"

    def __unicode__(self):
        return unicode(self.person.get_full_name() + ' on ' + self.project_activity.name)


@receiver(post_save, sender=UserActivity)
def user_activity_perobject_permissions(sender, instance, **kwargs):
    assign_perm('change_useractivity', instance.person, instance)
    assign_perm('add_useractivity', instance.person, instance)


# pre_delete.connect(remove_perobject_permissions, UserActivity)

def project_file_name(instance, filename):
    return '/'.join(['static/upload', 'project', filename])


class Project(models.Model):
    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')
    name = models.CharField(_('name'), max_length=30, blank=False)
    strategy = models.TextField(_('strategy'), blank=True)
    description = models.TextField(_('description'), blank=True)

    facebook_group = models.CharField(_('facebook group'), max_length=255, blank=True)
    github_repo = models.CharField(_('github repository'), max_length=255, blank=True)
    pm_url = models.CharField(_('project management URL'), max_length=255, blank=True)
    url = models.CharField(_('url'), max_length=255, blank=True)
    slug = models.CharField(_('slug'), max_length=255, blank=True)
    is_featured = models.BooleanField(_('Is featured'),
                                            default=False)

    logo = models.FileField(_('logo'), upload_to=project_file_name, blank=True)
    logo_styled = models.FileField(_('logo styled to fit obshtestvo.bg'), upload_to=project_file_name, blank=True)
    cover_image = models.FileField(_('cover image'), upload_to=project_file_name, blank=True)
    order = models.PositiveIntegerField()

    def users(self):
        return User.objects.exclude(pauses__project=self).filter(
            project_activities__project=self,
            project_activities__user_activities__is_active=True).distinct()

    def __unicode__(self):
        return unicode(self.name)

class ProjectMilestone(models.Model):
    class Meta:
        verbose_name = _('project milestone')
        verbose_name_plural = _('project milestones')
    project = models.ForeignKey('Project', related_name="milestones")
    description = models.TextField(_('description'))
    target_date = models.CharField(_('target date'), max_length=255, blank=True)
    date = models.DateField(_('actual date happened'), blank=True, null=True)
    is_done = models.BooleanField(_('done'), default=False)
    is_technical = models.BooleanField(_('technical'), default=False)
    percent = models.PositiveIntegerField(_('Show at'), max_length=3)
    order = models.PositiveIntegerField()




class UserProjectPause(models.Model):
    project = models.ForeignKey('Project', related_name="pauses")
    person = models.ForeignKey('User', related_name="pauses")

    class Meta:
        unique_together = ('project', 'person',)


@receiver(post_save, sender=UserProjectPause)
def user_pause_perobject_permissions(sender, instance, **kwargs):
    assign_perm('add_userprojectpause', instance.person, instance)
    assign_perm('delete_userprojectpause', instance.person, instance)
    assign_perm('change_userprojectpause', instance.person, instance)


# pre_delete.connect(remove_perobject_permissions, UserProjectPause)


class ProjectActivity(models.Model):
    project = models.ForeignKey('Project', related_name="activities", blank=True, null=True)
    users = models.ManyToManyField('User', through='UserActivity',
                                   related_name="project_activities")
    name = models.CharField(_('name'), max_length=140, blank=False)
    is_organisational = models.BooleanField(_('organisation related'),
                                            default=False)
    is_template = models.BooleanField(_('template activity'),
                                            default=False)
    can_accomodate = models.IntegerField(_('Max people'),
                                         max_length=3, default=1)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = _('project activity')
        verbose_name_plural = _('project activities')

    def __unicode__(self):
        return unicode(self.name)


class ProjectMotive(models.Model):
    class Meta:
        verbose_name = _('project motive')
        verbose_name_plural = _('project motives')
    project = models.ForeignKey('Project', related_name="motives")
    title = models.CharField(_('name'), max_length=30, blank=False)
    order = models.PositiveIntegerField()

    def __unicode__(self):
        return unicode(self.title)


class ProjectUsageExampleStep(models.Model):
    class Meta:
        verbose_name = _('project usage example step')
        verbose_name_plural = _('project usage example steps')
    project = models.ForeignKey('Project', related_name="example_steps")
    title = models.CharField(_('name'), max_length=140, blank=False)
    order = models.PositiveIntegerField()
    icon = models.CharField(_('icon'), max_length=30, blank=False)
    example_number = models.PositiveIntegerField(_('Example number'))

    def __unicode__(self):
        return unicode(self.title)


class Task(models.Model):
    class Meta:
        verbose_name = _('task')
        verbose_name_plural = _('tasks')
    activity = models.ForeignKey('ProjectActivity', related_name="tasks")
    name = models.CharField(_('name'), max_length=30, blank=False)
    points = models.PositiveIntegerField(_('points'), max_length=4, default=5)
    is_complete = models.BooleanField(_('is this complete'), default=False)
    order = models.PositiveIntegerField()


    # return RecycleSpot.objects.select_related("type").filter(materials__name__in=types).only(*cls.FIELDS).distinct()
    # return RecycleSpot.objects.select_related("type").filter(materials__name__in=types).only(*cls.FIELDS).distinct()

    # ref: https://docs.djangoproject.com/en/dev/ref/models/queries/
    # ref: https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet.select_related
    # .select_related('blog')