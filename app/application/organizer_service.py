from pathlib import Path
from typing import List
from app.domain.strategies.base import IOrganizerStrategy
from app.infra.filesystem_adapter import FileSystemAdapter
from app.domain.interfaces.i_file_mover import IFileMover

class OrganizerService:

  def handle_new_file(self, path: Path) -> None:
      """
      Main entry point: organize a newly detected file.
      """
      # Step 1: Load file metadata
      file_entity = self._metadata_provider.load_file(path)
      
      # Step 2: Find matching strategy
      
      # TODO: Loop through self._strategies and find first match
      
      # Step 3: Calculate destination
      # TODO: Call strategy.destination(file_entity)
      
      # Step 4: Move file
      # TODO: Call self._file_mover.move()
      
      # Step 5: Handle errors
      # TODO: What if no strategy matches?
      # TODO: What if FileExistsError is raised?

