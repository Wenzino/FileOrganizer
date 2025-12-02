from pathlib import Path
from datetime import datetime
from app.domain.entities.file_entity import FileEntity


class FileSystemAdapter:
    """
    Infrastructure adapter that reads file metadata from the OS.
    Converts OS-level data into domain FileEntity objects.
    """

    def load_file(self, path: Path) -> FileEntity:
      path  = Path(path)

      if not path.exists() or not path.is_file():
        raise FileNotFoundError(f'File not found: {path}')
      
      stats = path.stat()

      size = stats.st_size
      created_at = datetime.fromtimestamp(stats.st_ctime)
      modified_at = datetime.fromtimestamp(stats.st_mtime)

      return FileEntity (
          path = path,
          size = size,
          created_at = created_at,
          modified_at = modified_at,
      )
