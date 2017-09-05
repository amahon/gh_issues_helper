
import logging

import github
import requests

from .core import Epic

logger = logging.getLogger('gh_issues_helper')


def load_from_zenhub(config):
    logger.info('load_from_zenhub')

    gh = github.Github(config.GITHUB_USERNAME, config.GITHUB_ACCESS_TOKEN)
    repo = gh.get_repo(config.GITHUB_REPOSITORY)

    epics_json = requests.get(
        'https://api.zenhub.io/p1/repositories/{}/epics'.format(repo.id),
        headers={
            'X-Authentication-Token': config.ZENHUB_API_TOKEN
        }).json()

    return list(map(lambda x: Epic(repo, x['issue_number']), epics_json['epic_issues']))
