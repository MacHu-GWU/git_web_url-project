import enum
from .assembla import AssemblaPlatform
from .aws_codecommit import AwsCodeCommitPlatform
from .base import BasePlatform
from .bitbucket import BitbucketPlatform
from .friendcode import FriendCodePlatform
from .github import GitHubPlatform
from .gitlab import GitLabPlatform


# Supported platforms
class PlatformEnum(str, enum.Enum):
    assembla = "assembla"
    aws_codecommit = "aws_codecommit"
    bitbucket = "bitbucket"
    friendcode = "friendcode"
    github = "github"
    gitlab = "gitlab"
    unknown = "unknown"


PLATFORMS = [
    # name -> Platform object
    (PlatformEnum.assembla.value, AssemblaPlatform()),
    (PlatformEnum.aws_codecommit.value, AwsCodeCommitPlatform()),
    (PlatformEnum.bitbucket.value, BitbucketPlatform()),
    (PlatformEnum.friendcode.value, FriendCodePlatform()),
    (PlatformEnum.github.value, GitHubPlatform()),
    (PlatformEnum.gitlab.value, GitLabPlatform()),
    # Match url
    ("base", BasePlatform()),
]
