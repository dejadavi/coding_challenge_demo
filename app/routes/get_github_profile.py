from app.settings import retry_behaviour
from flask import Flask, jsonify, Blueprint, Response, current_app
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests import Session
from flask import current_app
from app.models import GithubProfileSchema
from json import dumps, loads


get_github_profile_blueprint = Blueprint(
    'get_github_profile',
    __name__
)


@get_github_profile_blueprint.route("/github/<org>", methods=["GET"])
def get_github(org):

    headers = {
        'Accept': "application/vnd.github.mercy-preview+json"
    }

    url = "https://api.github.com/users/{org}/repos"\
        .format(org=org)

    session = Session()

    session.mount(
        prefix='https://',
        adapter=HTTPAdapter(
            max_retries=retry_behaviour
        )
    )

    response = session\
        .get(
            url,
            headers=headers
        )
    github_profile_schema = GithubProfileSchema()

    github_profile = github_profile_schema\
        .load({
            "orgname": org,
            "repos": response.json()
        })

    result = github_profile_schema\
        .dump(github_profile)

    current_app.logger.debug(result)

    return jsonify(result), 200


