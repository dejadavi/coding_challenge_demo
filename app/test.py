import unittest
from .app import app
from .models import GithubProfileSchema, GithubProfile,\
     BitBucketProfileSchema, BitBucketProfile


class TestSuite1(unittest.TestCase):

    def setUp(self):

        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_get_github_profile(self):

        result = self.app.get('/github/mailchimp')

        print(result)
    
        github_profile_schema = GithubProfileSchema()

        test_github_profile = github_profile_schema\
            .load(result.json)

        self.assertIsInstance(test_github_profile, GithubProfile)
        self.assertGreaterEqual(test_github_profile.repo_count, 0)

    def test_get_bitbucket_profile(self):

        result = self.app.get('/bitbucket/mailchimp')

        bitbucket_profile_schema = BitBucketProfileSchema()

        test_bitbucket_profile = bitbucket_profile_schema\
            .load(result.json)

        self.assertIsInstance(test_bitbucket_profile, BitBucketProfile)
        self.assertGreaterEqual(test_bitbucket_profile.repo_count, 0)




