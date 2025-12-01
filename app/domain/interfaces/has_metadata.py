from abc import ABC, abstractmethod
from pathlib import Path
from datetime import datetime

class IHasMetadata (ABC):
  @property
  @abstractmethod
  def name (self) -> str:
    """Returns the file name without path"""
    pass

  @property
  @abstractmethod
  def extension (self) -> str:
    """Returns file extension ('.pdf', '.jpg')"""
    pass

  @property
  @abstractmethod
  def size (self) -> int:
    """Returns file size in bytes"""
    pass

  @property
  @abstractmethod
  def path (self) -> Path:
    """Returns full file path"""
    pass

  @property
  @abstractmethod
  def created_at (self) -> datetime:
    """Returns file creation timestamp"""
    pass

  @property
  @abstractmethod
  def modified_at (self) -> datetime:
    """Returns file modification timestamp"""
    pass