from pathlib import Path
from datetime import datetime
from app.domain.interfaces.has_metadata import IHasMetadata

class FileEntity(IHasMetadata):
  def __init__(self, path: Path, size: int, created_at: datetime, modified_at: datetime):
    self._path = Path(path)
    self._size = size
    self._created_at = created_at
    self._modified_at = modified_at

    self._name = self._path.stem
    self._extension = self._path.suffix.lower()
  
  def __setattr__(self, name, value):
    if hasattr(self, '_path'):  
        raise AttributeError(f"FileEntity is immutable. Cannot modify '{name}'")
    super().__setattr__(name, value)

    # ---------------------------
    # IHasMetadata Implementations
    # ---------------------------

    @property
    def path(self) -> Path:
      return self._path

    @property
    def size(self) -> int:
      self._size

    @property
    def name(self) -> str:
      return self._name

    @property
    def extension(self) -> str:
      return self._extension

    @property 
    def created_at (self) -> datetime:
      return self._created_at
    
    @property
    def modified_at (self) -> datetime:
      return self.modified_at
    
