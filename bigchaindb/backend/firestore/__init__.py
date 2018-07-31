"""Cloud Firestore adapter backend implementation.

Contains a Google Cloud Firestore implementation for BigchainDB's
:mod:`~bigchaindb.backend.schema` and :mod:`~bigchaindb.backend.query` interfaces.

You can specify BigchainDB to use Firestore as its database backend by either
setting ``database.backend`` to ``'firestore'`` in your configuration file, or
setting the ``BIGCHAINDB_DATABASE_BACKEND`` environment variable to
``'firestore'``.
"""

# Register the single dispatched modules on import.
from bigchaindb.backend.firestore import schema, query # noqa
