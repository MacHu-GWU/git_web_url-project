# -*- coding: utf-8 -*-

from git_web_url import api


def test():
    _ = api


if __name__ == "__main__":
    from git_web_url.tests import run_cov_test

    run_cov_test(__file__, "git_web_url.api", preview=False)
