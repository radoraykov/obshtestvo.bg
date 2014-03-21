# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Organisation'
        db.create_table(u'projects_organisation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('strategy', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('representatives', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('found_via', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('contact', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('working_with', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('is_sponsor', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('partnered_project', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='partners', null=True, to=orm['projects.Project'])),
            ('provided_help', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'projects', ['Organisation'])

        # Adding M2M table for field middlemen on 'Organisation'
        m2m_table_name = db.shorten_name(u'projects_organisation_middlemen')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organisation', models.ForeignKey(orm[u'projects.organisation'], null=False)),
            ('member', models.ForeignKey(orm[u'projects.member'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organisation_id', 'member_id'])

        # Adding model 'Skill'
        db.create_table(u'projects_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'projects', ['Skill'])

        # Adding model 'MemberType'
        db.create_table(u'projects_membertype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'projects', ['MemberType'])

        # Adding model 'Member'
        db.create_table(u'projects_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='member', null=True, to=orm['projects.User'])),
            ('update_from_user', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('intro', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('offered_help', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('is_available', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('available_after', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('last_contacted_at', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('latest_answer', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('contact_frequency', self.gf('django.db.models.fields.CharField')(default='d', max_length=2)),
            ('will_help', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_paid_only', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'projects', ['Member'])

        # Adding M2M table for field skills on 'Member'
        m2m_table_name = db.shorten_name(u'projects_member_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm[u'projects.member'], null=False)),
            ('skill', models.ForeignKey(orm[u'projects.skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['member_id', 'skill_id'])

        # Adding M2M table for field types on 'Member'
        m2m_table_name = db.shorten_name(u'projects_member_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm[u'projects.member'], null=False)),
            ('membertype', models.ForeignKey(orm[u'projects.membertype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['member_id', 'membertype_id'])

        # Adding M2M table for field projects_interests on 'Member'
        m2m_table_name = db.shorten_name(u'projects_member_projects_interests')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm[u'projects.member'], null=False)),
            ('project', models.ForeignKey(orm[u'projects.project'], null=False))
        ))
        db.create_unique(m2m_table_name, ['member_id', 'project_id'])

        # Adding model 'User'
        db.create_table(u'projects_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('profession', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('is_available', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('available_after', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('has_confirmed_data', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('avatar', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'projects', ['User'])

        # Adding M2M table for field groups on 'User'
        m2m_table_name = db.shorten_name(u'projects_user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'projects.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        m2m_table_name = db.shorten_name(u'projects_user_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'projects.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'permission_id'])

        # Adding model 'UserPointSpending'
        db.create_table(u'projects_userpointspending', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='spendings', to=orm['projects.User'])),
            ('points', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=10)),
            ('product', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'projects', ['UserPointSpending'])

        # Adding model 'UserActivity'
        db.create_table(u'projects_useractivity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='activities', to=orm['projects.User'])),
            ('project_activity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_activities', to=orm['projects.ProjectActivity'])),
            ('progress', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('last_stopped_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('needs_replacement', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'projects', ['UserActivity'])

        # Adding unique constraint on 'UserActivity', fields ['person', 'project_activity']
        db.create_unique(u'projects_useractivity', ['person_id', 'project_activity_id'])

        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('strategy', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('facebook_group', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('github_repo', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('pm_url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('logo', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('logo_styled', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('cover_image', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'projects', ['Project'])

        # Adding model 'ProjectMilestone'
        db.create_table(u'projects_projectmilestone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='milestones', to=orm['projects.Project'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('target_date', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('is_done', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_technical', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('percent', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=3)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'projects', ['ProjectMilestone'])

        # Adding model 'UserProjectPause'
        db.create_table(u'projects_userprojectpause', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pauses', to=orm['projects.Project'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pauses', to=orm['projects.User'])),
        ))
        db.send_create_signal(u'projects', ['UserProjectPause'])

        # Adding unique constraint on 'UserProjectPause', fields ['project', 'person']
        db.create_unique(u'projects_userprojectpause', ['project_id', 'person_id'])

        # Adding model 'ProjectActivity'
        db.create_table(u'projects_projectactivity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='activities', null=True, to=orm['projects.Project'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('is_organisational', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_template', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('can_accomodate', self.gf('django.db.models.fields.IntegerField')(default=1, max_length=3)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
        ))
        db.send_create_signal(u'projects', ['ProjectActivity'])

        # Adding model 'ProjectMotive'
        db.create_table(u'projects_projectmotive', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='motives', to=orm['projects.Project'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'projects', ['ProjectMotive'])

        # Adding model 'ProjectUsageExampleStep'
        db.create_table(u'projects_projectusageexamplestep', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='example_steps', to=orm['projects.Project'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('example_number', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'projects', ['ProjectUsageExampleStep'])

        # Adding model 'Task'
        db.create_table(u'projects_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tasks', to=orm['projects.ProjectActivity'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('points', self.gf('django.db.models.fields.PositiveIntegerField')(default=5, max_length=4)),
            ('is_complete', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'projects', ['Task'])


    def backwards(self, orm):
        # Removing unique constraint on 'UserProjectPause', fields ['project', 'person']
        db.delete_unique(u'projects_userprojectpause', ['project_id', 'person_id'])

        # Removing unique constraint on 'UserActivity', fields ['person', 'project_activity']
        db.delete_unique(u'projects_useractivity', ['person_id', 'project_activity_id'])

        # Deleting model 'Organisation'
        db.delete_table(u'projects_organisation')

        # Removing M2M table for field middlemen on 'Organisation'
        db.delete_table(db.shorten_name(u'projects_organisation_middlemen'))

        # Deleting model 'Skill'
        db.delete_table(u'projects_skill')

        # Deleting model 'MemberType'
        db.delete_table(u'projects_membertype')

        # Deleting model 'Member'
        db.delete_table(u'projects_member')

        # Removing M2M table for field skills on 'Member'
        db.delete_table(db.shorten_name(u'projects_member_skills'))

        # Removing M2M table for field types on 'Member'
        db.delete_table(db.shorten_name(u'projects_member_types'))

        # Removing M2M table for field projects_interests on 'Member'
        db.delete_table(db.shorten_name(u'projects_member_projects_interests'))

        # Deleting model 'User'
        db.delete_table(u'projects_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table(db.shorten_name(u'projects_user_groups'))

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table(db.shorten_name(u'projects_user_user_permissions'))

        # Deleting model 'UserPointSpending'
        db.delete_table(u'projects_userpointspending')

        # Deleting model 'UserActivity'
        db.delete_table(u'projects_useractivity')

        # Deleting model 'Project'
        db.delete_table(u'projects_project')

        # Deleting model 'ProjectMilestone'
        db.delete_table(u'projects_projectmilestone')

        # Deleting model 'UserProjectPause'
        db.delete_table(u'projects_userprojectpause')

        # Deleting model 'ProjectActivity'
        db.delete_table(u'projects_projectactivity')

        # Deleting model 'ProjectMotive'
        db.delete_table(u'projects_projectmotive')

        # Deleting model 'ProjectUsageExampleStep'
        db.delete_table(u'projects_projectusageexamplestep')

        # Deleting model 'Task'
        db.delete_table(u'projects_task')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'projects.member': {
            'Meta': {'object_name': 'Member'},
            'available_after': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contact_frequency': ('django.db.models.fields.CharField', [], {'default': "'d'", 'max_length': '2'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_paid_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_contacted_at': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'latest_answer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'offered_help': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'projects_interests': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'interested_members'", 'blank': 'True', 'to': u"orm['projects.Project']"}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'members'", 'blank': 'True', 'to': u"orm['projects.Skill']"}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'members'", 'blank': 'True', 'to': u"orm['projects.MemberType']"}),
            'update_from_user': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'member'", 'null': 'True', 'to': u"orm['projects.User']"}),
            'will_help': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'projects.membertype': {
            'Meta': {'object_name': 'MemberType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'projects.organisation': {
            'Meta': {'object_name': 'Organisation'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contact': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'found_via': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_sponsor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'middlemen': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'middleman_organisations'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['projects.Member']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'partnered_project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'partners'", 'null': 'True', 'to': u"orm['projects.Project']"}),
            'provided_help': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'representatives': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'strategy': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'working_with': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'cover_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'facebook_group': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'github_repo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'logo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'logo_styled': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pm_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'strategy': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'projects.projectactivity': {
            'Meta': {'object_name': 'ProjectActivity'},
            'can_accomodate': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_organisational': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_template': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'activities'", 'null': 'True', 'to': u"orm['projects.Project']"}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'project_activities'", 'symmetrical': 'False', 'through': u"orm['projects.UserActivity']", 'to': u"orm['projects.User']"})
        },
        u'projects.projectmilestone': {
            'Meta': {'object_name': 'ProjectMilestone'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_technical': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'percent': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '3'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'milestones'", 'to': u"orm['projects.Project']"}),
            'target_date': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'projects.projectmotive': {
            'Meta': {'object_name': 'ProjectMotive'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'motives'", 'to': u"orm['projects.Project']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'projects.projectusageexamplestep': {
            'Meta': {'object_name': 'ProjectUsageExampleStep'},
            'example_number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'example_steps'", 'to': u"orm['projects.Project']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'projects.skill': {
            'Meta': {'object_name': 'Skill'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'projects.task': {
            'Meta': {'object_name': 'Task'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tasks'", 'to': u"orm['projects.ProjectActivity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'points': ('django.db.models.fields.PositiveIntegerField', [], {'default': '5', 'max_length': '4'})
        },
        u'projects.user': {
            'Meta': {'object_name': 'User'},
            'available_after': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'avatar': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            'has_confirmed_data': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'projects.useractivity': {
            'Meta': {'unique_together': "(('person', 'project_activity'),)", 'object_name': 'UserActivity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_stopped_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'needs_replacement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'activities'", 'to': u"orm['projects.User']"}),
            'progress': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'project_activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_activities'", 'to': u"orm['projects.ProjectActivity']"})
        },
        u'projects.userpointspending': {
            'Meta': {'object_name': 'UserPointSpending'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'spendings'", 'to': u"orm['projects.User']"}),
            'points': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '10'}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'projects.userprojectpause': {
            'Meta': {'unique_together': "(('project', 'person'),)", 'object_name': 'UserProjectPause'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pauses'", 'to': u"orm['projects.User']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pauses'", 'to': u"orm['projects.Project']"})
        }
    }

    complete_apps = ['projects']