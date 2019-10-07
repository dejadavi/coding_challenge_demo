from app.app import ma
from app.settings import retry_behaviour
from flask import Flask, jsonify, Blueprint, Response, current_app
from marshmallow import Schema, EXCLUDE, INCLUDE, RAISE, post_load, pre_load,\
    SchemaOpts, post_dump
from marshmallow.fields import String, Boolean,\
    Integer, URL, List, Nested, Method, Field, Function,\
    Mapping, DateTime, Date
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests import Session
from types import SimpleNamespace
from .models import BitBucketProfile, GithubProfile, GithubRepoProfile,\
    BitBucketProfile


class _OwnerSchema(ma.Schema):

    class Meta:
        unknown = EXCLUDE
        fields = (
            "id", 'url'
        )

    login = String(required=True)
    id = Integer(required=True)
    node_id = String(required=False)
    avatar_url = URL(required=False)
    url = URL(required=False)
    html_url = URL(required=False)
    followers_url = URL(required=False)
    following_url = URL(required=False)
    gists_url = URL(required=False)
    starred_url = URL(required=False)
    subscriptions_url = URL(required=False)
    organizations_url = URL(required=False)
    repos_url = URL(required=False)
    events_url = URL(required=False)
    received_events_url = URL(required=False)
    type = String(required=False)
    site_admin = Boolean(required=False)


class BitBucketRepoProfileSchema(ma.Schema):

    class Meta:
        unknown = EXCLUDE

    fields = (
        "name",
        "has_issues",
        "watchers_count",
        "langauge",
        "private"
    )

    name = String(required=True)
    scm = String()
    website = URL()
    language = String(required=True)
    full_name = String(load_only=True)
    has_issues = Boolean(required=True)

    slug = String(load_only=True)
    private = Boolean(
        data_key='is_private',
        attribute='private',
        required=True
    )


class BitBucketProfileSchema(ma.Schema):

    class Meta:
        unknown = EXCLUDE

    orgname = String()
    repos = Nested(BitBucketRepoProfileSchema, many=True, required=True)
    repo_count = Integer(dump_only=True, required=True)

    @post_load
    def hydrate(self, data, **kwargs):

        profile = BitBucketProfile(**data)

        return profile


class GithubRepoProfileSchema(ma.Schema):

    class Meta:
        unknown = EXCLUDE

        fields = (
            "name",
            'has_issues'
            "topics",
            "watchers_count",
            "langauge",
            "private"
        )

    source_id = Integer(data_key='id', attribute='source_id', required=True)
    name = String(data_key='full_name', attribute='name', required=True)
    private = Boolean(required=True)
    topics = List(String(), required=False)
    forks = Integer(required=False)
    open_issues = Integer(required=True)
    watchers = Integer(required=False, missing=None)
    watchers_count = Integer(required=False, missing=None)
    language = String(required=False, missing=None)
    has_issues = Boolean(required=False)
    open_issues_count = Integer(required=False)
    topic_count = Integer(dump_only=True, required=False)

    @post_load
    def hydrate(self, data, **kwargs):
        """
        Post load. Create object class we work with in application
        """
        profile = GithubRepoProfile(**data)

        return profile

    @post_dump
    def dehydrate(self, data, **kwargs):

        return data


class GithubProfileSchema(ma.Schema):

    class Meta:
        unknown = EXCLUDE

    orgname = String()
    repos = Nested(
        GithubRepoProfileSchema,
        required=True,
        many=True
    )

    repo_count = Integer(required=True, dump_only=True)

    @post_load
    def hydrate(self, data, **kwargs):

        return GithubProfile(**data)

    @post_dump
    def dehydrate(self, data, **kwargs):

        return data
