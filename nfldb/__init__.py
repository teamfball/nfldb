"""
Module nfldb provides command line tools and a library for maintaining
and querying a relational database of play-by-play NFL data.
"""

from nfldb.db import __pdoc__ as __db_pdoc__
from nfldb.db import api_version, connect, set_timezone, schema_version
from nfldb.db import Tx
from nfldb.types import __pdoc__ as __types_pdoc__
from nfldb.types import Clock, Enums, Drive, FieldPosition, Game
from nfldb.types import PossessionTime, Team
from nfldb.version import __version__

__pdoc__ = __db_pdoc__
__pdoc__ = dict(__pdoc__, **__types_pdoc__)


# Export selected identifiers from sub-modules.
__all__ = [
    # nfldb.db
    'api_version', 'connect', 'set_timezone', 'schema_version',
    'Tx',

    # nfldb.types
    'Clock', 'Enums', 'Drive', 'FieldPosition', 'Game',
    'PossessionTime', 'Team',

    # nfldb.version
    '__version__',
]
