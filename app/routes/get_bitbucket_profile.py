from app.settings import retry_behaviour
from flask import Flask, jsonify, Blueprint, Response, current_app
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests import Session
from flask import current_app
from app.models import BitBucketProfileSchema
from json import dumps, loads


get_bitbucket_profile_blueprint = Blueprint(
    'get_bitbucket_profile',
    __name__
)

@get_bitbucket_profile_blueprint.route("/bitbucket/<org>", methods=["GET"])
def get_bitbucket(org):


    url = "https://api.bitbucket.org/2.0/repositories/{org}"\
        .format(org=org)

    headers = {}

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

    bitbucket_profile_schema = BitBucketProfileSchema()

    bitbucket_profile = bitbucket_profile_schema\
        .load({
            "orgname": org,
            "repos": response\
                .json()\
                .get('values', {})
        })

    result = bitbucket_profile_schema\
        .dump(bitbucket_profile)

    current_app.logger.debug(result)

    return jsonify(result), 200