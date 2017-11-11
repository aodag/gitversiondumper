import logging
from .git import Git


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    git = Git()
    logger.debug(git.get_version())
