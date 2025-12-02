import shutil 
from pathlib import Path
from app.domain.interfaces.i_file_mover import IFileMover

class FileMover(IFileMover):
    """
    Concrete implementation of IFileMover using shutil.
    Only handles the mechanics of moving a file.
    Business rules (conflict handling, retry, renaming)
    are handled by the Application layer.
    """

    def move(self, source: Path, destination: Path) -> bool:
        if not source.exists():
            raise FileNotFoundError(f'Source file does not exist: {source}')
        
        destination_directory = destination.parent
        destination_directory.mkdir(parents=True, exist_ok=True)

        if destination.exists():
            raise FileExistsError(f'File already exists at destination: {destination}')
        
        try:
            shutil.move(str(source), str(destination))
            return True
        except PermissionError:
            raise
        except OSError as e:
            raise RuntimeError(f'Failed to move file: {e}')
        return super().move(source, destination)