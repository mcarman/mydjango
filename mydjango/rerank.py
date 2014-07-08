#!/usr/bin/env python
#rerank
#runs every 5 sec to update, set to 60 for now

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydjango.settings.dev")
from apps.linkengine.models import Link


def rank_all():
    for link in Link.with_votes.all():
        link.set_rank()

import time


def show_all():
    print "\n".join("%10s %0.2f" % (l.title, l.rank_score,
                    ) for l in Link.with_votes.all())
    print "----\n\n\n"

if __name__ == "__main__":
    while 1:
        print "---"
        rank_all()
        show_all()
        time.sleep(60)
