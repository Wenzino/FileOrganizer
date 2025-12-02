from pathlib import Path
from typing import List
from app.domain.strategies.base import IOrganizerStrategy
from app.infra.filesystem_adapter import FileSystemAdapter
from app.domain.interfaces.i_file_mover import IFileMover