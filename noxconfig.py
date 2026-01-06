from __future__ import annotations

from pathlib import Path
from typing import Iterable

from exasol.toolbox.config import BaseConfig


class Config(BaseConfig):
    project_name: str = "sqlglot-toolbox"
    root_path: Path = Path(__file__).parent
    doc: Path = Path(__file__).parent / "doc"
    source: Path = Path("sqlglot_toolbox")
    version_file: Path = (
            Path(__file__).parent
            / "sqlglot_toolbox"
            / "version.py"
    )
    path_filters: Iterable[str] = ()
    plugins: Iterable[object] = ()

PROJECT_CONFIG = Config()
