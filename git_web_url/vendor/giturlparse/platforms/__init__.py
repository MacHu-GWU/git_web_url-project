from .assembla import AssemblaPlatform
from .aws_codecommit import AwsCodeCommitPlatform
from .base import BasePlatform
from .bitbucket import BitbucketPlatform
from .friendcode import FriendCodePlatform
from .github import GitHubPlatform
from .gitlab import GitLabPlatform

# Supported platforms
PLATFORMS = [
    # name -> Platform object
    ("assembla", AssemblaPlatform()),
    ("aws_codecommit", AwsCodeCommitPlatform()),
    ("bitbucket", BitbucketPlatform()),
    ("friendcode", FriendCodePlatform()),
    ("github", GitHubPlatform()),
    ("gitlab", GitLabPlatform()),
    # Match url
    ("base", BasePlatform()),
]
