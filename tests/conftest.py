"""
Shared pytest fixtures for the python-projects test suite.
"""

from __future__ import annotations

import json
import os

import pytest


@pytest.fixture
def tmp_tasks_file(tmp_path: os.PathLike[str]) -> str:
    """Return a path to a temporary (empty) tasks JSON file."""
    filepath = str(tmp_path / "tasks.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump([], f)
    return filepath


@pytest.fixture
def sample_tasks_file(tmp_path: os.PathLike[str]) -> str:
    """Return a path to a tasks JSON file pre-populated with two tasks."""
    filepath = str(tmp_path / "tasks.json")
    data = [
        {
            "title": "Buy groceries",
            "category": "Personal",
            "details": "Milk, eggs, bread",
            "due_date": "2024-12-01",
            "priority": "High",
        },
        {
            "title": "Submit report",
            "category": "Work",
            "details": "Q3 financial report",
            "due_date": "2024-11-30",
            "priority": "Critical",
        },
    ]
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return filepath
