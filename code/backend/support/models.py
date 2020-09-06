from django.db import models
from fuzzywuzzy import process


class Tag(models.Model):
    name = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return "[Tag] %s" % self.name


class TroubleshootingLogicBlock(models.Model):
    SUCCESS_RATE_CHANGE_INTERVAL = 0.1

    title = models.CharField(blank=True, max_length=1000)
    content = models.TextField(blank=True)

    successors = models.ManyToManyField("self", blank=True, symmetrical=False)
    tags = models.ManyToManyField(Tag)
    success_rate = models.FloatField(default=1)

    def __str__(self):
        return "[TLB] %s" % self.title


class Flow(models.Model):
    OPEN = 0
    SUCCESSFUL = 1
    UNSUCCESSFUL = 2

    STATE_CHOICES = [
        (OPEN, 'Open'),
        (SUCCESSFUL, 'Closed - Successful'),
        (UNSUCCESSFUL, 'Closed - No success'),
    ]

    steps = models.ManyToManyField(TroubleshootingLogicBlock, through="FlowStep")
    state = models.IntegerField(choices=STATE_CHOICES, default=OPEN)

    user_query = models.TextField(blank=True)

    def __str__(self):
        return "[Flow] user_query=%s, status=%s" % (self.user_query, self.state)

    @property
    def steps_count(self):
        return self.steps.count()

    @property
    def last_step(self):
        flow_steps = FlowStep.objects.filter(flow=self, position=self.steps_count - 1)
        if flow_steps.count() > 0:
            return flow_steps.last()
        else:
            return None

    @property
    def flow_failed(self):
        if self.last_step:
            return self.last_step.tlb.successors.count() == 0
        else:
            return False

    def get_next_best_block(self):
        if self.steps_count > 0:
            last_step = self.last_step
            candidates = last_step.tlb.successors
        else:
            candidates = TroubleshootingLogicBlock.objects.all()

        if not self.flow_failed:
            if candidates.count() == 1:
                return candidates.first()
            else:
                scores = {}
                for candidate in candidates.all():
                    tags = [tag.name for tag in candidate.tags.all()]

                    # process.extract creates tuples (with the FuzzyWuzzy-plugin).
                    # The second value of the tuples contains the score for each tag.
                    # x[1] gets those scores; then they are summed with sum([....])
                    score = sum([x[1] for x in process.extract(self.user_query, tags)])
                    scores[candidate] = score * candidate.success_rate

                return max(scores, key=scores.get)
        else:
            self.state = Flow.UNSUCCESSFUL
            self.save()


class FlowStep(models.Model):
    tlb = models.ForeignKey(
        TroubleshootingLogicBlock,
        null=True,
        on_delete=models.SET_NULL
    )

    flow = models.ForeignKey(Flow, on_delete=models.CASCADE)

    position = models.IntegerField()

    def __str__(self):
        return "[FlowStep] tlb_title=%s, position=%s" % (self.tlb.title, self.position)

