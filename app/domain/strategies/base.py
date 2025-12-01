from abc import ABC, abstractmethod
from pathlib import Path

class IOrganizerStrategy (ABC):
  @abstractmethod
  def match (self, file) -> bool:
    """Returns True if this strategy applies to the given file"""
    pass

  @abstractmethod
  def destination (self, file) -> Path:
    """Returns the destination path for the file"""
    pass

  @property
  @abstractmethod
  def priority (self) -> int:
    """Higher priority wins on conflict"""
    pass
  