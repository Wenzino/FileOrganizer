from pathlib import Path
from app.domain.strategies.base import IOrganizerStrategy
from app.domain.interfaces.has_metadata import IHasMetadata

class DocumentStrategy (IOrganizerStrategy) :
  def __init__(self, base_destination: Path):
    self._base_destination = base_destination;

  @property
  def priority (self ) -> int:
    return 10 # medium priority 
  
  def match (self, file: IHasMetadata) -> bool:
    # TODO: implement this ...
    # should return true if extension is .pdf, .docx, .txt, etc.
    pass

  def destination(self, file: IHasMetadata) -> Path:
    # TODO: implement this ...
    # should return base_destination / "Documents"
    pass