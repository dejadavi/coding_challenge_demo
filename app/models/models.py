from flask_marshmallow import Marshmallow
from types import SimpleNamespace
from json import dumps, loads, dump


class GithubRepoProfile(object):

    def __init__(self, **kwargs):

        self.__dict__.update(**kwargs)

    def __repr__(self):

        return dumps(self.__dict__)

    def __str__(self):

        obj_string = f"""
        <(
            source_id = {self.source_id},
            name = {self.name},
            private = {self.private},
            topics = {self.topics},
            forks = {self.forks},
            open_issues = {self.open_issues},
            watchers = {self.watchers},
            owner = {self.owner},
            size = {self.size},
            watchers_count = {self.watchers_count},
            language = {self.language}
        )>"""

        return obj_string


class GithubProfile(object):

    def __init__(self, orgname, repos, **kwargs):

        self.orgname = orgname
        self.repos = repos
        self.repo_count = len(self.repos)

    def __repr__(self):

        return dumps(self.__dict__)

    def __str__(self):

        repostring = "[\n"
        repostring += "\n".join([
            "\t\t"+repo.name+","
            for repo in self.repos
        ])

        repostring += "\n\t    ]"

        obj_string = f"""
        <(
            orgname = {self.orgname},
            repos = {repostring},
            repo_count = {self.repo_count}
        )>"""

        return obj_string


class BitBucketRepoProfile(object):

    def __init__(
        self, name, issues,
        watchers_count, langauge, private, **kwargs
    ):
        self.name = name
        self.issues = issues
        self.watchers_count = watchers_count
        self.langauge = langauge
        self.private = private

        #api currently doesn't support
        self.topics = []


class BitBucketProfile(object):

    def __init__(self, orgname, repos, **kwargs):
        self.orgname = orgname
        self.repos = repos
        self.repo_count = len(repos)

    def __repr__(self):

        return dumps(self.__dict__)

    def __str__(self):
        repostring = "[\n"
        repostring += "\n".join([
            "\t\t"+repo.name+","
            for repo in self.repos
        ])

        repostring += "\n\t    ]"

        obj_string = f"""
            <(
                orgname = {self.orgname},
                repos = {repostring},
                repo_count = {self.repo_count}
            )>"""

        return obj_string
