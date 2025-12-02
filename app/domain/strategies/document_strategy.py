from pathlib import Path
from app.domain.strategies.base import IOrganizerStrategy
from app.domain.interfaces.has_metadata import IHasMetadata

class DocumentStrategy (IOrganizerStrategy) :
  DEFAUL_EXTENSIONS = {'.pdf', '.doc', '.docx', '.txt', '.md', '.odt'}

  def __init__(self, base_destination: Path, extensions: set[str] = None):
    self._base_destination = base_destination
    self._extension = extensions or self.DEFAUL_EXTENSIONS

  @property
  def priority (self ) -> int:
    return 10 # medium priority 
  
  def match (self, file: IHasMetadata) -> bool:
    return file.extension.lower() in self._extension;

  def destination(self, file: IHasMetadata) -> Path:
    return self._base_destination / 'Documents'