# -*- coding: utf-8 -*-


from git_web_url.tests.data import CaseEnum
from git_web_url.find_web_url import get_repo_url


def test():
    for _, case_enum in CaseEnum.iter_items():
        repo_url = get_repo_url(case_enum.origin_url)
        assert repo_url == case_enum.web_url


if __name__ == "__main__":
    from git_web_url.tests import run_cov_test

    run_cov_test(__file__, "git_web_url.find_web_url", preview=False)
