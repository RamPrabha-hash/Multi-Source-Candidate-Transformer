"""
Base Parser

Defines the interface that every parser
must implement.
"""

from abc import ABC, abstractmethod


class BaseParser(ABC):
    """
    Abstract base class for all parsers.
    """

    @abstractmethod
    def parse(self) -> dict:
        """
        Parse a data source and return the
        canonical candidate schema.
        """
        pass