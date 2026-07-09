"""
Base parser interface for all resume parsers.
"""

from abc import ABC, abstractmethod


class BaseParser(ABC):
    """
    Abstract base class for resume parsers.
    """

    @abstractmethod
    def parse(
        self,
        *args,
        **kwargs,
    ):
        """
        Execute parser.
        """
        pass