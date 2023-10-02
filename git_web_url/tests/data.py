# -*- coding: utf-8 -*-

import typing as T
import enum
import dataclasses

from ..constants import GitProviderEnum
from ..vendor.giturlparse import GitUrlParsed


def pretty_print_git_url_parsed(git_url_parsed: "GitUrlParsed"):  # pragma: no cover
    """
    Pretty print the ``giturlparser.GitUrlParsed`` object returned by
    ``giturlparser.parse`` function.
    """
    print(f"platform = {git_url_parsed.platform!r}")
    print(f"host = {git_url_parsed.host!r}")
    print(f"resource = {git_url_parsed.resource!r}")
    print(f"port = {git_url_parsed.port!r}")
    print(f"protocol = {git_url_parsed.protocol!r}")
    print(f"protocols = {git_url_parsed.protocols!r}")
    print(f"user = {git_url_parsed.user!r}")
    print(f"owner = {git_url_parsed.owner!r}")
    print(f"repo = {git_url_parsed.repo!r}")
    print(f"name = {git_url_parsed.name!r}")
    print(f"groups = {git_url_parsed.groups!r}")
    print(f"path = {git_url_parsed.path!r}")
    print(f"path_raw = {git_url_parsed.path_raw!r}")
    print(f"branch = {git_url_parsed.branch!r}")


@dataclasses.dataclass
class Case:
    """
    Represent a ground truth test case for a git url.

    :param origin_url: the remote origin url in the ``.git/config`` file.
    :param web_url: the desired web url.
    :param git_sys: the desired git system.
    """

    origin_url: str = dataclasses.field()
    web_url: str = dataclasses.field()
    git_sys: GitProviderEnum = dataclasses.field()


class CaseEnum(enum.Enum):
    # GitHub Saas
    github_saas_http = Case(
        origin_url="https://github.com/user-name/repo-name.git",
        web_url="https://github.com/user-name/repo-name",
        git_sys=GitProviderEnum.github,
    )
    github_saas_token = Case(
        origin_url="https://my_github_token@github.com/user-name/repo-name.git",
        web_url="https://github.com/user-name/repo-name",
        git_sys=GitProviderEnum.github,
    )
    github_saas_ssh = Case(
        origin_url="ssh://git@github.com:user-name/repo-name.git",
        web_url="https://github.com/user-name/repo-name",
        git_sys=GitProviderEnum.github,
    )

    # GitHub Enterprise
    github_enterprise_http = Case(
        origin_url="https://github.mycompany.net/team-name/repo-name.git",
        web_url="https://github.mycompany.net/team-name/repo-name",
        git_sys=GitProviderEnum.github,
    )
    github_enterprise_token = Case(
        origin_url="https://my_github_token@github.mycompany.net/team-name/repo-name.git",
        web_url="https://github.mycompany.net/team-name/repo-name",
        git_sys=GitProviderEnum.github,
    )
    github_enterprise_ssh = Case(
        origin_url="ssh://git@github.mycompany.net:team-name/repo-name.git",
        web_url="https://github.mycompany.net/team-name/repo-name",
        git_sys=GitProviderEnum.github,
    )

    # GitLab Saas
    gitlab_saas_http = Case(
        origin_url="https://gitlab.com/user-name/repo-name.git",
        web_url="https://gitlab.com/user-name/repo-name",
        git_sys=GitProviderEnum.gitlab,
    )
    gitlab_saas_token = Case(
        origin_url="https://oauth2:my_gitlab_token@gitlab.com/user-name/repo-name.git",
        web_url="https://gitlab.com/user-name/repo-name",
        git_sys=GitProviderEnum.gitlab,
    )
    gitlab_saas_ssh = Case(
        origin_url="ssh://git@gitlab.com:user-name/repo-name.git",
        web_url="https://gitlab.com/user-name/repo-name",
        git_sys=GitProviderEnum.gitlab,
    )

    # GitLab Enterprise
    gitlab_enterprise_http = Case(
        origin_url="https://my.enterprise.com/user-name/repo-name.git",
        web_url="https://my.enterprise.com/user-name/repo-name",
        git_sys=GitProviderEnum.unknown,
    )
    gitlab_enterprise_token = Case(
        origin_url="https://oauth2:my_gitlab_token@my.enterprise.com/user-name/repo-name",
        web_url="https://my.enterprise.com/user-name/repo-name",
        git_sys=GitProviderEnum.unknown,
    )
    gitlab_enterprise_ssh = Case(
        origin_url="ssh://git@my.enterprise.com:1234/user-name/repo-name.git",
        web_url="https://my.enterprise.com/user-name/repo-name",
        git_sys=GitProviderEnum.unknown,
    )

    # BitBucket Saas
    bitbucket_saas_http = Case(
        origin_url="https://bitbucket.org/user-name/repo-name.git",
        # example: https://bitbucket.org/astanin/python-tabulate
        web_url="https://bitbucket.org/user-name/repo-name",
        git_sys=GitProviderEnum.bitbucket,
    )
    bitbucket_saas_ssh = Case(
        origin_url="git@bitbucket.org:user-name/repo-name.git",
        web_url="https://bitbucket.org/user-name/repo-name",
        git_sys=GitProviderEnum.bitbucket,
    )

    # BitBucket Enterprise
    bitbucket_enterprise_http = Case(
        origin_url="https://account-name@bitbucket.prod.mycompany.com/user-name/repo-name.git",
        web_url="https://bitbucket.prod.mycompany.com/projects/user-name/repos/repo-name",
        git_sys=GitProviderEnum.unknown,
    )
    bitbucket_enterprise_ssh = Case(
        origin_url="ssh://git@bitbucket.prod.mycompany.com:7999/user-name/repo-name.git",
        web_url="https://bitbucket.prod.mycompany.com/projects/user-name/repos/repo-name",
        git_sys=GitProviderEnum.bitbucket,
    )

    # AWS CodeCommit
    aws_codecommit_http = Case(
        origin_url="https://git-codecommit.us-east-1.amazonaws.com/v1/repos/repo-name",
        web_url="https://us-east-1.console.aws.amazon.com/codesuite/codecommit/repositories/repo-name",
        git_sys=GitProviderEnum.aws_codecommit,
    )
    aws_codecommit_ssh = Case(
        origin_url="ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/repo-name",
        web_url="https://us-east-1.console.aws.amazon.com/codesuite/codecommit/repositories/repo-name",
        git_sys=GitProviderEnum.aws_codecommit,
    )
    # aws_codecommit_grc = Case(
    #     origin_url="codecommit::us-east-1://repo-name",
    #     web_url="https://us-east-1.console.aws.amazon.com/codesuite/codecommit/repositories/repo-name",
    #     git_sys=GitProviderEnum.aws_codecommit,
    # )

    @classmethod
    def iter_items(cls) -> T.Iterable[T.Tuple[str, "Case"]]:
        for member in cls:
            yield member.name, member.value

    @classmethod
    def iter_items_by_git_system(
        cls, git_system: GitProviderEnum
    ) -> T.Iterable[T.Tuple[str, "Case"]]:
        for member in cls:
            if member.value.git_sys.value.name == git_system.name:
                yield member.name, member.value

    @classmethod
    def iter_github_items(cls) -> T.Iterable[T.Tuple[str, "Case"]]:  # pragma: no cover
        yield from cls.iter_items_by_git_system(GitProviderEnum.github.value)

    @classmethod
    def iter_gitlab_items(cls) -> T.Iterable[T.Tuple[str, "Case"]]:  # pragma: no cover
        yield from cls.iter_items_by_git_system(GitProviderEnum.gitlab.value)

    @classmethod
    def iter_bitbucket_items(
        cls,
    ) -> T.Iterable[T.Tuple[str, "Case"]]:  # pragma: no cover
        yield from cls.iter_items_by_git_system(GitProviderEnum.bitbucket.value)

    @classmethod
    def iter_aws_codecommit_items(
        cls,
    ) -> T.Iterable[T.Tuple[str, "Case"]]:  # pragma: no cover
        yield from cls.iter_items_by_git_system(GitProviderEnum.aws_codecommit.value)
