from django.core.management.base import NoArgsCommand

from jobs.models import Job, Meetup


class Command(NoArgsCommand):
    help = "Populates database with meetups and job offers."

    def add_meetup(self, title, city, country, description, meetup_date):
        meetup, created = Meetup.objects.get_or_create(
            title=title,
            contact_email='example@example.com',
            city=city,
            country=country,
            description=description,
            ready_to_publish=True,
            meetup_date=meetup_date,
        )
        return meetup

    def add_job(self, title, company, website, city, country, description):
        job, created = Job.objects.get_or_create(
            title=title,
            company=company,
            contact_email='example@example.com',
            city=city,
            country=country,
            description=description,
            ready_to_publish=True,
        )
        return job

    def handle_noargs(self, **options):
        # Adding some meetups with future dates.
        self.add_meetup(
            title='Django Girls Warsaw',
            city='Warsaw',
            country='PL',
            description='description',
            meetup_date='2015-04-01'
        )
        self.add_meetup(
            title='Women in Technology',
            city='London',
            country='GB',
            description='description',
            meetup_date='2015-05-15'
        )
        self.add_meetup(
            title='Learn javascript',
            city='Paris',
            country='FR',
            description='description',
            meetup_date='2015-06-12'
        )

        self.add_meetup(
            title='Python breakfast',
            city='Berlin',
            country='DE',
            description='description',
            meetup_date='2015-07-01'
        )

        self.add_meetup(
            title='Girls Meetup',
            city='New York',
            country='US',
            description='description',
            meetup_date='2015-08-01'
        )

        # Adding some job offers.
        self.add_job(
            title='Intern',
            company='Google',
            website='http://www.google.pl/about/careers/students/',
            city='London',
            country='GB',
            description='description',
        )

        self.add_job(
            title='Software Development Engineer - Paid Internship',
            company='Amazon',
            website='http://www.amazon.jobs/team-category/university-recruiting',
            city='Gdansk',
            country='PL',
            description='description',
        )

        self.add_job(
            title='Software Engineer, Front End',
            company='Digital Ocean',
            website='https://careers.digitalocean.com/',
            city='New York',
            country='US',
            description='description',
        )

        def print_created_objects(model):
            """Prints created objects on terminal."""
            for created_object in model.objects.all():
                self.stdout.write('-{0}'.format(created_object))

        # Publishing meetups and job offers.
        for meetup in Meetup.objects.filter(ready_to_publish=True):
            meetup.publish()
        for job in Job.objects.filter(ready_to_publish=True):
            job.publish()

        print_created_objects(Meetup)
        print_created_objects(Job)
