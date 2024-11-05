#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for GithubOrgClient.
    """

    @patch("client.GithubOrgClient.get_json")
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        test_payload = {"org": org_name}
        mock_get_json.return_value = test_payload
        client = GithubOrgClient(org_name)

        result = client.org
        self.assertEqual(result, test_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch(
        "client.GithubOrgClient._public_repos_url",
        return_value=["repo1", "repo2"]
    )
    @patch("client.GithubOrgClient.get_json")
    def test_public_repos(self, mock_get_json, mock_public_repos_url):
        """
        Test that public_repos returns the expected repos.
        """
        mock_get_json.return_value = {"repos": ["repo1", "repo2"]}
        client = GithubOrgClient("google")

        result = client.public_repos()
        self.assertEqual(result, ["repo1", "repo2"])
        mock_get_json.assert_called_once()
        mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test has_license method.
        """
        client = GithubOrgClient("google")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
