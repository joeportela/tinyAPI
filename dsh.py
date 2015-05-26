# ----- Info ------------------------------------------------------------------

__author__ = 'Michael Montero <mcmontero@gmail.com>'

# ----- Imports ---------------------------------------------------------------

from tinyAPI.base.data_store.persistent_connections \
    import DataStorePersistentConnections
from tinyAPI.base.data_store.provider \
    import DataStoreProvider

import tinyAPI

__all__ = [
    'dsh'
]

# ----- Public Functions  -----------------------------------------------------

def dsh():
    '''Returns a usable handle to the configured data store.'''
    if tinyAPI.env_cli() is False:
        return DataStorePersistentConnections().get()
    else:
        return DataStoreProvider().get_data_store_handle()
