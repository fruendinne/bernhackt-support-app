from django.core.management.base import BaseCommand, CommandError
from django.template.loader import render_to_string
from django.utils.text import slugify

from support.models import Flow


class Command(BaseCommand):
    help = 'Generates static help pages from solved problems'

    def handle(self, *args, **options):
        flows = Flow.objects.all()

        for flow in flows:
            if len(flow.user_query) > 0:
                self.stdout.write(self.style.SUCCESS('Rendering Flow "%s"...' % flow))

                steps = flow.steps.all()

                filename = "support/static/helppages/%s.html" % slugify(flow.user_query)
                content = render_to_string('article_base.html', locals())
                with open(filename, 'w', encoding="UTF-8") as static_page:
                    static_page.write(content)
            else:
                self.stdout.write(self.style.SUCCESS('Ignoring Flow "%s" because it has no user query' % flow))
