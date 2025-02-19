# Make sure to place exceptions first as they're dependencies of other imports.
from ._exceptions import VersionMismatch as VersionMismatch
from ._exceptions import DaggerError as DaggerError
from ._exceptions import ProvisionError as ProvisionError
from ._exceptions import DownloadError as DownloadError
from ._exceptions import SessionError as SessionError
from ._exceptions import ClientError as ClientError
from ._exceptions import ClientConnectionError as ClientConnectionError
from ._exceptions import TransportError as TransportError
from ._exceptions import ExecuteTimeoutError as ExecuteTimeoutError
from ._exceptions import InvalidQueryError as InvalidQueryError
from ._exceptions import QueryError as QueryError
from ._exceptions import ExecError as ExecError

# We need the star import since this is a generated module.
from .client.gen import *

# Make sure Config is first as it's a dependency in Connection.
from ._config import Config as Config
from ._connection import Connection as Connection

# Re-export imports so they look like they live directly in this package.
for _value in list(locals().values()):
    if getattr(_value, "__module__", "").startswith("dagger."):
        _value.__module__ = __name__
