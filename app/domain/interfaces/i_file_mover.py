from abc import ABC, abstractmethod
from pathlib import Path


class IFileMover(ABC):
    """
    Interface for moving files.
    Domain defines WHAT needs to be done, infra defines HOW.
    """

    @abstractmethod
    def move (self, source: Path, destination: Path) -> bool:
        """
        Move file from source to destination.
        
        Args:
            source: Current file path
            destination: Target file path
            
        Returns:
            True if successful, False otherwise
            
        Raises:
            PermissionError: If lacking permissions
            FileNotFoundError: If source doesn't exist
        """
        pass