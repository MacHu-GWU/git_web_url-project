# -*- coding: utf-8 -*-

import typing as T
from urllib.parse import urlparse

from .vendor.giturlparse import parse, PlatformEnum


def parse_aws_codecommit_url(url: str) -> T.Tuple[str, str]:
    """
    :param url:
    :return: region, repo_name
    """
    if url.startswith("https://git-codecommit") or url.startswith(
        "ssh://git-codecommit"
    ):
        parse_result = urlparse(url)
        region = parse_result.netloc.split(".")[1]
        repo_name = parse_result.path.split("/")[-1]
    elif url.startswith("codecommit::"):
        paths = url.split(":")
        region, repo_name = paths[-2], paths[-1].lstrip("//")
    else:
        raise NotImplementedError
    return region, repo_name


def get_aws_codecommit_repo_url(region: str, repo_name: str) -> str:
    return f"https://{region}.console.aws.amazon.com/codesuite/codecommit/repositories/{repo_name}"


def get_repo_url_for_aws_codecommit(remote_origin_url: str) -> str:
    region, repo_name = parse_aws_codecommit_url(remote_origin_url)
    return get_aws_codecommit_repo_url(region, repo_name)


def get_repo_url(remote_origin_url: str) -> str:
    if remote_origin_url.startswith("codecommit::"):
        return get_repo_url_for_aws_codecommit(remote_origin_url)

    res = parse(remote_origin_url)

    # handler AWS Code Commit
    if res.platform == PlatformEnum.aws_codecommit:
        return get_repo_url_for_aws_codecommit(remote_origin_url)

    if "@" in res.host:
        host = res.host.split("@")[-1]
    else:
        host = res.host
    if host.startswith("bitbucket.") and (not host.startswith("bitbucket.org")):
        return f"https://{host}/projects/{res.owner}/repos/{res.name}"
    else:
        return f"https://{host}/{res.owner}/{res.name}"
