# -*- coding: utf-8 -*-

from pathlib import Path
from git_web_url.find_web_url import get_web_url

dir_doc = Path.home().joinpath("Documents")


def _test_get_web_url():
    # Test with default branch parameter (None - uses current branch)
    print(get_web_url(Path(__file__)))
    print(get_web_url(Path(__file__).absolute().parent.parent))


def _test_get_web_url_with_branch():
    # Test with branch=None (current branch - same as default)
    url = get_web_url(Path(__file__), branch=None)
    print(f"branch=None: {url}")
    # URL should contain a branch name
    assert "/blob/" in url

    # Test with branch="_default" (default branch - URL without explicit branch)
    url = get_web_url(Path(__file__), branch="_default")
    print(f"branch='_default': {url}")
    # URL should be without branch, just repo_url/blob/relative_path
    assert "/blob/" in url

    # Test with branch="_default" for directory (repo root)
    url = get_web_url(Path(__file__).absolute().parent.parent, branch="_default")
    print(f"branch='_default' (repo root): {url}")
    # URL should be just repo_url without tree/branch
    assert url.endswith("git_web_url-project")

    # Test with specific branch
    url = get_web_url(Path(__file__), branch="main")
    print(f"branch='main': {url}")
    assert "/blob/main/" in url

    url = get_web_url(Path(__file__), branch="develop")
    print(f"branch='develop': {url}")
    assert "/blob/develop/" in url

    # Test with specific branch for directory
    url = get_web_url(Path(__file__).absolute().parent, branch="feature-branch")
    print(f"branch='feature-branch' (directory): {url}")
    assert "/tree/feature-branch/" in url


def _test_get_web_url_edge_case():
    print(get_web_url(dir_doc / "CodeCommit" / "multi_env-project" / "README.rst"))
    print(get_web_url(dir_doc / "BitBucket" / "public" / "license.txt"))
    print(get_web_url(dir_doc / "GitHub" / "afwf_github-project" / "main.py"))
    print(get_web_url(dir_doc / "GitLab" / "woob" / "README.rst"))


def test_get_repo_url():
    print("")
    _test_get_web_url()
    _test_get_web_url_with_branch()
    # _test_get_web_url_edge_case()


if __name__ == "__main__":
    from git_web_url.tests import run_cov_test

    run_cov_test(__file__, "git_web_url.find_web_url", preview=False)
