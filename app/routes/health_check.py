from flask import Flask, jsonify, Blueprint, current_app, Response


health_check_blueprint = Blueprint(
    'health_check',
    __name__
)


@health_check_blueprint.route("/health-check", methods=["GET"])
def health_check():
    """
    Endpoint to health check API
    """
    current_app.logger.info("Health Check!")
    return Response("I'm gucci.", status=200)
