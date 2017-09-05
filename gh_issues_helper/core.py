
import datetime
import logging
import re

import frontmatter

logger = logging.getLogger('gh_issues_helper')


class CustomYAMLHandler(frontmatter.default_handlers.YAMLHandler):

    FM_BOUNDARY = re.compile(r'^—{6,}$', re.MULTILINE)
    START_DELIMITER = END_DELIMITER = "——————"


class Issue():
    """ Represents an issue on Github. """

    repo = None
    issue = None
    body = None

    metadata = {
        "start_date": None,
        "end_date": None
    }

    def __init__(self, repo, issue_number):
        logger.info('Issue.__init__ {} {}'.format(repo.full_name, issue_number))
        self.repo = repo
        self.issue = self.repo.get_issue(issue_number)
        logger.debug(self.issue.body)
        self.body = frontmatter.loads(self.issue.body, handler=CustomYAMLHandler())

    def __str__(self):
        return self.issue.title

    def __unicode__(self):
        return self.issue.title

    def save(self):
        """ Saves issue back to Github """
        logger.info('Issue.save {}'.format(self))
        self.issue.edit(
            body=frontmatter.dumps(self.body)
        )

    def normalize_metadata(self):
        """ Ensures that all expected metadata fields exist. """
        logger.info('Issue.normalize_metadata {}'.format(self))
        if not hasattr(self.body.metadata, 'end_date'):
            self.body.metadata['end_date'] = datetime.date.today()
        if not hasattr(self.body.metadata, 'start_date'):
            self.body.metadata['start_date'] = datetime.date.today()



class Epic(Issue):
    """ Represents an epic on Github. """

    issues = []

    pass
