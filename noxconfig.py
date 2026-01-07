"""
Nox project configuration for the sqlglot-toolbox package.

Defines paths, versioning, and tooling configuration used by nox sessions.
"""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

from exasol.toolbox.config import BaseConfig


class Config(BaseConfig):
    """Project configuration for sqlglot-toolbox tooling."""

    project_name: str = "sqlglot_toolbox"
    root_path: Path = Path(__file__).parent
    doc: Path = root_path / "doc"
    source: Path = root_path / "exasol" / "sqlglot_toolbox"
    version_file: Path = source / "version.py"
    path_filters: Iterable[str] = ()
    plugins: Iterable[object] = ()


PROJECT_CONFIG = Config()
