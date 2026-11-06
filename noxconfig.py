"""
Nox project configuration for the sqlglot-toolbox package.

Defines paths, versioning, and tooling configuration used by nox sessions.
"""

from __future__ import annotations

from pathlib import Path

from exasol.toolbox.config import BaseConfig

PROJECT_CONFIG = BaseConfig(
    project_name="sqlglot_toolbox",
    root_path=Path(__file__).parent,
    exasol_versions=("2025.1.8",),
)
