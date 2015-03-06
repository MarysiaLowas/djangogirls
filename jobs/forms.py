from django import forms

from .models import Job, Company, Meetup


class JobForm(forms.ModelForm):

    show_overwrite = False
    company_name = forms.CharField(label='Company',
                                   max_length=500,
                                   required=True)
    website = forms.URLField(label='Company website', required=True)

    class Meta:
        model = Job
        fields = ('company_name', 'website', 'contact_email', 'title',
                  'description', 'city', 'country')
        # custom labels
        labels = {
            'title': 'Job title'
        }


class MeetupForm(forms.ModelForm):

    class Meta:
        model = Meetup
        exclude = ['reviewer', 'review_status', 'reviewers_comment',
            'ready_to_publish', 'published_date', 'created', 'expiration_date'
        ]
        widgets = {
            'meetup_date': forms.DateTimeInput(format='%d-%m-%Y'),
        }
