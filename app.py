
import argparse
import pprint
import logging

import config

from gh_issues_helper.loaders import load_from_zenhub
from gh_issues_helper.web import serve

PARSER = argparse.ArgumentParser(description='Github Issue Helper.')
PARSER.add_argument('action')
ARGS = PARSER.parse_args()


logger = logging.getLogger('gh_issues_helper')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)


def normalize_metadata():
    logger.info('normalize_metadata')

    epics = load_from_zenhub(config)
    pprint.pprint(epics)
    for epic in epics:
        epic.normalize_metadata()
        for issue in epic.issues:
            issue.normalize_metadata()
            issue.save()
        epic.save()


def generate_gantt():
    pass


def weekly_update():
    pass


def serve_web():
    serve(config)


if __name__ == "__main__":


    logger.debug('__main__')
    if ARGS.action == 'normalize':
        normalize_metadata()
    elif ARGS.action == 'gantt':
        generate_gantt()
    elif ARGS.action == 'weekly_update':
        weekly_update()
    elif ARGS.action == 'serve':
        serve_web()
