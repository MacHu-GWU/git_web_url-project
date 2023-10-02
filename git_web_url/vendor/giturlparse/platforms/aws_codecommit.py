from .base import BasePlatform


class AwsCodeCommitPlatform(BasePlatform):
    PATTERNS = {
        # example: https://git-codecommit.us-east-1.amazonaws.com/v1/repos/repo-name
        "https": (
            r"(?P<protocols>(git\+)?(?P<protocol>https))://"
            r"(?P<domain>[^/]+?)/v1/repos/"
            r"((?P<repo>[^/]+?)(?:(\.git)?(/)?)(?P<path_raw>(/blob/|/tree/).+)?)$"
        ),
        # example: ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/repo-name
        "ssh": (
            r"(?P<protocols>(git\+)?(?P<protocol>ssh))?(://)?(?P<domain>.+?)/v1/repos/"
            r"((?P<repo>[^/]+?)(?:(\.git)?(/)?)(?P<path_raw>(/blob/|/tree/).+)?)$"
        ),
    }
    FORMATS = {
        # example: https://git-codecommit.us-east-1.amazonaws.com/v1/repos/repo-name
        "https": r"https://%(domain)s/v1/repos/%(repo)s%(dot_git)s%(path_raw)s",
        # example: ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/repo-name
        "ssh": r"ssh://%(domain)s/v1/repos/%(repo)s%(dot_git)s%(path_raw)s",
    }
    DOMAINS = (
        "^git-codecommit\.[a-z]{2}-[a-z]+-[0-9]\.amazonaws\.com$",
        # "git-codecommit.af-south-1.amazonaws.com",
        # "git-codecommit.ap-east-1.amazonaws.com",
        # "git-codecommit.ap-northeast-1.amazonaws.com",
        # "git-codecommit.ap-northeast-2.amazonaws.com",
        # "git-codecommit.ap-northeast-3.amazonaws.com",
        # "git-codecommit.ap-south-1.amazonaws.com",
        # "git-codecommit.ap-south-2.amazonaws.com",
        # "git-codecommit.ap-southeast-1.amazonaws.com",
        # "git-codecommit.ap-southeast-2.amazonaws.com",
        # "git-codecommit.ap-southeast-3.amazonaws.com",
        # "git-codecommit.ap-southeast-4.amazonaws.com",
        # "git-codecommit.ca-central-1.amazonaws.com",
        # "git-codecommit.eu-central-1.amazonaws.com",
        # "git-codecommit.eu-central-2.amazonaws.com",
        # "git-codecommit.eu-north-1.amazonaws.com",
        # "git-codecommit.eu-south-1.amazonaws.com",
        # "git-codecommit.eu-south-2.amazonaws.com",
        # "git-codecommit.eu-west-1.amazonaws.com",
        # "git-codecommit.eu-west-2.amazonaws.com",
        # "git-codecommit.eu-west-3.amazonaws.com",
        # "git-codecommit.il-central-1.amazonaws.com",
        # "git-codecommit.me-central-1.amazonaws.com",
        # "git-codecommit.me-south-1.amazonaws.com",
        # "git-codecommit.sa-east-1.amazonaws.com",
        # "git-codecommit.us-east-1.amazonaws.com",
        # "git-codecommit.us-east-2.amazonaws.com",
        # "git-codecommit.us-gov-east-1.amazonaws.com",
        # "git-codecommit.us-gov-west-1.amazonaws.com",
        # "git-codecommit.us-west-1.amazonaws.com",
        # "git-codecommit.us-west-2.amazonaws.com",
    )
    DEFAULTS = {"_user": "git"}

    @staticmethod
    def clean_data(data):
        data = BasePlatform.clean_data(data)
        if data["path_raw"].startswith("/browse/"):
            data["path"] = data["path_raw"].replace("/browse/", "")
        return data
