# -*- coding: utf-8 -*-

import enum
import dataclasses


@dataclasses.dataclass
class GitProvider:
    name: str = dataclasses.field()
    domain: str = dataclasses.field()


class GitProviderEnum(enum.Enum):
    unknown = GitProvider(
        name="unknown",
        domain="unknown.com",
    )
    github = GitProvider(
        name="github",
        domain="github.com",
    )
    gitlab = GitProvider(
        name="gitlab",
        domain="gitlab.com",
    )
    bitbucket = GitProvider(
        name="bitbucket",
        domain="bitbucket.org",
    )
    aws_codecommit = GitProvider(
        name="aws_codecommit",
        domain="git-codecommit.{region}.amazonaws.com",
    )
