import logging
import os

from cliff.lister import Lister


class ListFiles(Lister):
    """Show a list of files in the current directory.

    The file name and size are printed by default.
    """

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        columns = ("Name", "Size")

        return (columns, ((n, os.stat(n).st_size) for n in os.listdir(".")))
