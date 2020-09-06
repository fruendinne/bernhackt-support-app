# Create your views here.
from django.contrib.staticfiles.storage import StaticFilesStorage
from django.contrib.staticfiles.utils import get_files
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from support.models import TroubleshootingLogicBlock, Flow, FlowStep

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import datetime


class TLBSerializer(serializers.ModelSerializer):
    class Meta:
        model = TroubleshootingLogicBlock
        fields = ['title', 'content', 'tags', 'success_rate']
        depth = 2


class FlowSerializer(serializers.ModelSerializer):
    steps = TLBSerializer(read_only=True, many=True)
    flow_failed = serializers.ReadOnlyField()

    class Meta:
        model = Flow
        fields = ['pk', 'user_query', 'state', 'steps', 'flow_failed']


@api_view()
def start_flow(request):
    flow = Flow.objects.create(
        user_query=request.GET.get('user_query')
    )
    FlowStep.objects.create(
        flow=flow,
        tlb=flow.get_next_best_block(),
        position=flow.steps_count,
    ).save()

    serializer = FlowSerializer(flow)

    return Response(serializer.data)


@api_view()
def next_tlb(request, pk):
    flow = Flow.objects.get(pk=pk)

    next_block = flow.get_next_best_block()

    FlowStep.objects.create(
        flow=flow,
        tlb=next_block,
        position=flow.steps_count,
    ).save()

    serializer = FlowSerializer(flow)
    return Response(serializer.data)


@api_view()
def set_success(request, pk):
    flow = Flow.objects.get(pk=pk)

    flow.state = Flow.SUCCESSFUL
    flow.save()

    serializer = FlowSerializer(flow)
    return Response(serializer.data)


def helppages_index(request):
    s = StaticFilesStorage()
    pages = list(get_files(s, location='helppages'))

    slugs = [x[10:-5] for x in pages]
    pks = [x[10:-1].split('_')[0] for x in pages]

    return render(request, 'article_index.html', locals())


# A Test-view for exploring a simple view including FuzzyWuzzy search
# See also https://www.geeksforgeeks.org/fuzzywuzzy-python-library/
def test_stuff(request):
    now = datetime.datetime.now()
    fuzzy1 = fuzz.ratio('geeksforgeeks', 'geeksgeeks')
    fuzzy2 = fuzz.partial_ratio("geeks for geeks", "geeks geeks")

    query = 'geeks for geeks'
    choices = ['geek for geek', 'geek geek', 'g. for geeks']
    # Get a list of matches ordered by score, default limit to 5
    list_ordered = process.extract(query, choices)
    # If we want only the top one
    top_one = process.extractOne(query, choices)

    # html = "<html>" \
    #        "<body><p>It is now %s.</p>" \
    #        "<p>fuzzy1 = %s</p>" \
    #        "<p>fuzzy2 = %s</p>" \
    #        "<p>list_ordered = %s</p>" \
    #        "<p>top_one = %s</p>" \
    #        "</body>" \
    #        "</html>" \
    #        % (now, fuzzy1, fuzzy2, list_ordered, top_one)
    # print(fuzzy2)
    # return HttpResponse(html)

    # return JsonResponse(list_ordered, safe=False)
    data = {'now': now, 'fuzzy1': fuzzy1, 'fuzzy2': fuzzy2, 'list_ordered': list_ordered, 'top_one': top_one}
    return JsonResponse(data)

