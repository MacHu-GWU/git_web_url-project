.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


1.0.1 (2025-12-13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add ``relpath`` subcommand to print the relative path from the git repository root to a given file or folder.

**Breaking Changes**

- Refactor CLI to use subcommand structure. The previous ``gwu`` command is now ``gwu url``.
    - Before: ``gwu /path/to/file``
    - After: ``gwu url /path/to/file``


0.1.4 (2025-12-13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add ``branch`` parameter to ``get_web_url`` function, allowing users to specify which branch to use in the generated URL:
    - ``CURRENT_BRANCH``: use the current git branch (default behavior)
    - ``DEFAULT_BRANCH``: use the default branch (main/master), generates URL without explicit branch
    - Any string: use the specified branch name
- Add ``CURRENT_BRANCH`` and ``DEFAULT_BRANCH`` sentinel constants to the public API.
- Add ``--branch`` (or ``-b``) flag to CLI commands (``gwu`` and ``gitweburl``).

**Miscellaneous**

- Improve documentation with CLI usage examples and Python API usage examples.


0.1.3 (2023-10-03)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- Fix a bug that the relative path should not be "." when the git repo dir when you are already at the git repo dir.

**Miscellaneous**

- Improve code coverage test to 99%.


0.1.2 (2023-10-03)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- Fix a bug that cannot detect the git repo dir when you are already at the git repo dir.

**Miscellaneous**

- Add CLI help info.


0.1.1 (2023-10-03)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First release.
- Add support for AWS CodeCommit, BitBucket, BitBucket Enterprise, GitHub, GitHub Enterprise, GitLab, GitLab Enterprise.
- Add the following public API:
    - ``git_web_url.api.PlatformEnum``
    - ``git_web_url.api.ProtocolEnum``
    - ``git_web_url.api.get_web_url``
- Add the CLI command ``gitweburl`` or ``gwu``.
