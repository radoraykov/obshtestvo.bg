from django.contrib import admin
from django.forms import ModelForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _
from suit.widgets import *
from pagedown.widgets import AdminPagedownWidget
from .models import *
from django import forms
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
import reversion
from suit.admin import SortableTabularInline, SortableModelAdmin
from django.db import models
from django.templatetags.static import static
from django.utils.html import urlize
from django.utils.html import format_html

def close_link(instance):
    if not instance.id:
        return ''
    url = reverse('admin:%s_%s_change' % (
        instance._meta.app_label,  instance._meta.module_name),  args=[instance.id] ) + 'tools/' + 'toolfunc'
    return mark_safe(u'<a href="{u}">Close</a>'.format(u=url))


def avatar(obj):
    if (obj.facebook):
        url = u'http://graph.facebook.com/%s/picture?width=40&amp;height=40' % obj.facebook.split('=' if 'profile.php' in obj.facebook else '/')[-1]
    else:
        url = static('img/user-silhouette.png')
    return mark_safe(u'<img width="40" height="40" src="%s" />' % url)


# from guardian.admin import GuardedModelAdmin
class UserActivityInline(admin.TabularInline):
    model = UserActivity
    suit_classes = 'suit-tab suit-tab-activities'
    extra = 1

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    inlines = (UserActivityInline,)
    add_form = MyUserCreationForm
    suit_form_tabs = (
        ('system', 'System'),
        ('common', 'Common'),
        ('activities', 'Activities'),
    )
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-system',),
            'fields': ('username', 'password')}
        ),
        (_('Personal info'), {
            'classes': ('suit-tab suit-tab-system',),
            'fields': ('first_name', 'last_name', 'email')}
        ),
        (_('Permissions'), {
            'classes': ('suit-tab suit-tab-system',),
            'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')

        }),
        (_('Important dates'), {
            'classes': ('suit-tab suit-tab-system',),
            'fields': ('last_login', 'date_joined')}
        ),
        (_('Custom'), {
            'classes': ('suit-tab suit-tab-common',),
            'fields': ('profession','is_available','available_after','bio', 'avatar')}
        ),
    )


class ProjectActivityFrom(ModelForm):
    class Meta:
        widgets = {
            'can_accomodate': EnclosedInput(append='icon-user', attrs={'class': 'input-mini'}),
        }

class ProjectActivityInline(SortableTabularInline):
    model = ProjectActivity
    suit_classes = 'suit-tab suit-tab-activities'
    sortable = 'order'
    extra = 0
    form = ProjectActivityFrom

    def advanced(self, instance):
        if not instance.id:
            return ''
        url = reverse('admin:%s_%s_change' % (
            instance._meta.app_label,  instance._meta.module_name),  args=[instance.id] )
        return mark_safe(u'<a href="{u}">Edit</a>'.format(u=url) + ' ' + close_link(instance))

    readonly_fields = ('advanced',)

class TaskInline(SortableTabularInline):
    model = Task
    suit_classes = 'suit-tab suit-tab-tasks'
    sortable = 'order'
    extra = 0


class ProjectMotiveInline(SortableTabularInline):
    model = ProjectMotive
    suit_classes = 'suit-tab suit-tab-motives'
    sortable = 'order'
    extra = 0


class ProjectMilestoneFrom(ModelForm):
    class Meta:
        widgets = {
            # 'percent': RangeInput(append='%', attrs={"min":1, "max":100}),
            'percent': EnclosedInput(append='%', attrs={'class': 'input-mini'}),
            'target_date': forms.TextInput(attrs={'class': 'input-mini'}),
        }

class ProjectMilestoneInline(SortableTabularInline):
    form = ProjectMilestoneFrom
    model = ProjectMilestone
    suit_classes = 'suit-tab suit-tab-milestones'
    sortable = 'order'
    extra = 0



class ProjectUsageExampleStepForm(ModelForm):
    class Meta:
        widgets = {
            # 'percent': RangeInput(append='%', attrs={"min":1, "max":100}),
            'example_number': EnclosedInput(attrs={'class': 'input-mini'}),
            'icon':EnclosedInput(append='icon-heart', attrs={'class': 'input-mini'}),
        }


class ProjectUsageExampleStepInline(SortableTabularInline):
    model = ProjectUsageExampleStep
    suit_classes = 'suit-tab suit-tab-usage-examples'
    sortable = 'order'
    extra = 0
    form = ProjectUsageExampleStepForm

class RangeInput(EnclosedInput):
    """HTML5 Range Input."""
    input_type = 'range'

class ProjectAdminForm(ModelForm):
    class Meta:
        widgets = {
            'url': EnclosedInput(prepend='icon-globe'),
            'pm_url': EnclosedInput(prepend='icon-globe'),
            'facebook_group': EnclosedInput(prepend='icon-globe'),
            'github_repo': EnclosedInput(prepend='icon-globe'),
            'strategy': AdminPagedownWidget(),
            'description': AdminPagedownWidget()
        }

class ProjectAdmin(reversion.VersionAdmin, SortableModelAdmin):
    list_display = ('name', 'users',)
    sortable = 'order'
    form = ProjectAdminForm
    search_fields = ['name']
    list_filter = ['is_featured']
    inlines = [
        ProjectActivityInline,
        ProjectMotiveInline,
        ProjectUsageExampleStepInline,
        ProjectMilestoneInline,
    ]
    suit_form_tabs = (
        ('general', 'General'),
        ('strategy', 'Strategy'),
        ('description', 'Description'),
        # ('advanced', 'Advanced Settings'),
        ('activities', 'Activities'),
        ('milestones', 'Milestones'),
        ('motives', 'Motives'),
        ('usage-examples', 'Usage examples steps'),
    )
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('name', 'slug', 'url',)
        }),
        ('Management', {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('pm_url', 'facebook_group', 'github_repo',)
        }),
        ('Media', {
            'classes': ('suit-tab suit-tab-general',),
            'fields': (
                'logo',
                'logo_styled',
                'cover_image',
            )
        }),
        ('Homepage', {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('is_featured',)
        }),
        (None, {
            'classes': ('suit-tab suit-tab-strategy',),
            'fields': ('strategy',)
        }),
        (None, {
            'classes': ('suit-tab suit-tab-description',),
            'fields': (
                'description',
            )}
        ),
    )



class ProjectActivityAdminBase(admin.ModelAdmin):
    inlines = (UserActivityInline, TaskInline)

    def tools(self, instance):
        return close_link(instance)

    list_display = ('name', 'project', 'tools')

    def toolfunc(self, request, obj):
        pass
    toolfunc.label = "Close"  # optional
    toolfunc.short_description = "This will be the tooltip of the button"  # optional
    objectactions = ('toolfunc', )


class ProjectActivityAdmin(ProjectActivityAdminBase, reversion.VersionAdmin):
    suit_form_tabs = (
        ('general', 'General'),
        ('tasks', 'Tasks'),
        ('activities', 'User activities'),
    )

    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('name', 'project',)
        }),
        ('Settings', {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('is_organisational', 'is_template', 'can_accomodate', )
        }),
    )

# template, prepopulated forms:
# http://stackoverflow.com/questions/2223375/multiple-modeladmins-views-for-same-model-in-django-admin
# http://stackoverflow.com/questions/936376/prepopulate-django-non-model-form
class ProjectActivityTemplate(ProjectActivity):
    class Meta:
        proxy = True

class ProjectActivityTemplateForm(forms.ModelForm):
    class Meta:
        model = ProjectActivityTemplate
    is_template = forms.BooleanField(widget=forms.HiddenInput(), initial=1)
    order = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

class ProjectActivityTemplateAdmin(ProjectActivityAdminBase):
    form = ProjectActivityTemplateForm
    inlines = []
    fields = ('name', 'is_organisational', 'can_accomodate', 'order', 'is_template',)
    def queryset(self, request):
        return self.model.objects.filter(is_template=True)


class MemberAdminFrom(forms.ModelForm):
    class Meta:
        widgets = {
            'facebook':EnclosedInput(prepend='icon-share'),
            'email':EnclosedInput(prepend='icon-envelope'),
            # 'types': autocomplete_light.MultipleChoiceWidget(autocomplete='MemberTypeAutocomplete'),
            # 'skills': autocomplete_light.MultipleChoiceWidget(autocomplete='SkillAutocomplete'),
            # 'projects_interests': autocomplete_light.MultipleChoiceWidget(autocomplete='ProjectAutocomplete'),
        }

class MemberAdmin(admin.ModelAdmin):
    model = Member
    form = MemberAdminFrom
    search_fields = ['name']
    list_editable = ('is_active','is_available')
    list_filter = ('projects_interests','is_active','is_available','types','skills','last_contacted_at','is_paid_only')
    list_display = (avatar, 'name', 'facebook_as_link', 'email', 'is_active', 'is_available')
    suit_form_tabs = (
        ('general', _('General')),
        ('specifics', _('Specifics')),
        # ('integration', _('System')),
    )
    formfield_overrides = {
        models.TextField: {'widget': AutosizedTextarea(attrs={'rows':2, 'cols':50})},
        models.DateTimeField: {'widget': SuitSplitDateTimeWidget},
        models.DateField: {'widget': SuitDateWidget},
    }

    def facebook_as_link(self, obj):
        return format_html(urlize(obj.facebook))
    facebook_as_link.short_description = 'Facebook'

    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('name', 'facebook', 'email', 'date_joined',)
        }),
        (_('Expectations'), {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ( 'is_active', 'is_available', 'available_after', )
        }),
        (_("Member's preferences"), {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('skills', 'types', 'projects_interests','offered_help', )
        }),
        (_('Self-description & Comments'), {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('intro', 'comment')
        }),
        (None, {
            'classes': ('suit-tab suit-tab-specifics',),
            'fields': ('will_help',)
        }),
        (_('Conditions'), {
            'classes': ('suit-tab suit-tab-specifics',),
            'fields': ('is_paid_only',)
        }),
        (_('Communication'), {
            'classes': ('suit-tab suit-tab-specifics',),
            'fields': ('last_contacted_at', 'latest_answer', 'contact_frequency', )
        }),
        # ('User', {
        #     'classes': ('suit-tab suit-tab-integration',),
        #     'fields': ('user', 'update_from_user')
        # }),
    )



class OrganisationAdmin(admin.ModelAdmin):
    model = Organisation
    list_filter = ('middlemen','is_sponsor')
    list_display = ('name','representatives','is_sponsor')
    search_fields = ['name']
    suit_form_tabs = (
        ('general', _('General')),
    )
    formfield_overrides = {
        models.TextField: {'widget': AutosizedTextarea(attrs={'rows':3, 'cols':70})},
        models.DateTimeField: {'widget': SuitSplitDateTimeWidget},
        models.DateField: {'widget': SuitDateWidget},
    }

    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('name', 'is_sponsor', 'strategy')
        }),
        (_('Contact'), {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('middlemen', 'representatives', 'contact', )
        }),
        (_('About'), {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('comment', 'found_via', 'working_with', )
        }),
        (_('Partner'), {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ('partnered_project', 'provided_help',)
        }),
    )

admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(MemberType)
admin.site.register(Skill)
admin.site.register(UserProjectPause)
admin.site.register(ProjectActivity, ProjectActivityAdmin)
admin.site.register(ProjectActivityTemplate, ProjectActivityTemplateAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(User, MyUserAdmin)
admin.site.register(UserActivity)
