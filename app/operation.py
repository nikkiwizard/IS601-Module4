"""Compatibility shim exposing `Operation`.

Some parts of the test suite import `app.operation.Operation` while
the implementation lives in `app.operations.Operations`. Re-export the
class here to avoid changing many imports.
"""
from app.operations import Operations as Operation

__all__ = ["Operation"]
