# -*- coding: utf-8 -*-


from git_web_url.tests.data import CaseEnum
from git_web_url.parser import parse


def _test_get_repo_url_all():
    for name, case in CaseEnum.iter_items():
        # print(f"{name}: {case.origin_url}")
        result = parse(case.origin_url)
        assert result.protocol == case.protocol
        assert result.platform == case.platform
        assert result.domain == case.domain
        assert result.owner == case.owner
        assert result.repo == case.repo


def _test_get_repo_url_edge_case():
    case = CaseEnum.aws_codecommit_grc.value
    result = parse(case.origin_url, debug=True)
    print(f"protocol: {[result.protocol, case.protocol]}")
    print(f"platform: {[result.platform, case.platform]}")
    print(f"domain: {[result.domain, case.domain]}")
    print(f"owner: {[result.owner, case.owner]}")
    print(f"repo: {[result.repo, case.repo]}")


def test_get_repo_url():
    print("")
    _test_get_repo_url_all()
    # _test_get_repo_url_edge_case()


if __name__ == "__main__":
    from git_web_url.tests import run_cov_test

    run_cov_test(__file__, "git_web_url.parser", preview=False)
