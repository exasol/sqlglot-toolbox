from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

from exasol.toolbox.config import BaseConfig


class Config(BaseConfig):
    project_name: str = "sqlglot_toolbox"
    root_path: Path = Path(__file__).parent
    doc: Path = Path(__file__).parent / "doc"
    source: Path = root_path / "exasol" / "sqlglot_toolbox"
    version_file: Path = source / "version.py"
    path_filters: Iterable[str] = ()
    plugins: Iterable[object] = ()


PROJECT_CONFIG = Config()
