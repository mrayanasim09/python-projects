"""
Tests for GUI/todo.py — Task dataclass and TaskStore (headless, no Tkinter).
"""

from __future__ import annotations

import json
import os

import pytest

from GUI.todo import Task, TaskStore

# ---------------------------------------------------------------------------
# Task dataclass
# ---------------------------------------------------------------------------


class TestTask:
    def test_to_dict_roundtrip(self):
        task = Task(
            title="Test",
            category="Work",
            details="Some details",
            due_date="2024-12-01",
            priority="High",
        )
        d = task.to_dict()
        restored = Task.from_dict(d)
        assert restored == task

    def test_from_dict_with_missing_keys_uses_defaults(self):
        """from_dict should tolerate partial dicts (missing keys → empty string)."""
        task = Task.from_dict({"title": "Only Title"})
        assert task.title == "Only Title"
        assert task.category == ""
        assert task.priority == ""


# ---------------------------------------------------------------------------
# TaskStore CRUD
# ---------------------------------------------------------------------------


class TestTaskStoreCRUD:
    def _make_task(self, title: str = "Task") -> Task:
        return Task(
            title=title, category="Cat", details="Det", due_date="2024-01-01", priority="Low"
        )

    def test_add_increases_length(self, tmp_tasks_file: str):
        store = TaskStore(tmp_tasks_file)
        store.add(self._make_task("A"))
        assert len(store) == 1

    def test_add_multiple(self, tmp_tasks_file: str):
        store = TaskStore(tmp_tasks_file)
        store.add(self._make_task("A"))
        store.add(self._make_task("B"))
        assert len(store) == 2

    def test_get_all_returns_copy(self, tmp_tasks_file: str):
        store = TaskStore(tmp_tasks_file)
        store.add(self._make_task("A"))
        tasks = store.get_all()
        tasks.clear()  # mutate the returned list
        assert len(store) == 1  # store is unaffected

    def test_delete_removes_by_index(self, tmp_tasks_file: str):
        store = TaskStore(tmp_tasks_file)
        store.add(self._make_task("A"))
        store.add(self._make_task("B"))
        store.delete(0)
        assert len(store) == 1
        assert store.get_all()[0].title == "B"

    def test_update_replaces_task(self, tmp_tasks_file: str):
        store = TaskStore(tmp_tasks_file)
        store.add(self._make_task("Original"))
        updated = Task(
            title="Updated", category="New", details="d", due_date="2025-01-01", priority="High"
        )
        store.update(0, updated)
        assert store.get_all()[0].title == "Updated"


# ---------------------------------------------------------------------------
# TaskStore persistence — atomic JSON serialisation
# ---------------------------------------------------------------------------


class TestTaskStorePersistence:
    def _make_task(self, title: str = "Task") -> Task:
        return Task(
            title=title, category="Cat", details="Det", due_date="2024-01-01", priority="Low"
        )

    def test_save_and_load_roundtrip(self, tmp_tasks_file: str):
        store = TaskStore(tmp_tasks_file)
        store.add(self._make_task("Buy milk"))
        store.add(self._make_task("Pay rent"))
        store.save()

        store2 = TaskStore(tmp_tasks_file)
        store2.load()
        assert len(store2) == 2
        assert store2.get_all()[0].title == "Buy milk"
        assert store2.get_all()[1].title == "Pay rent"

    def test_save_produces_valid_json(self, tmp_tasks_file: str):
        store = TaskStore(tmp_tasks_file)
        store.add(self._make_task("X"))
        store.save()
        with open(tmp_tasks_file, encoding="utf-8") as f:
            data = json.load(f)
        assert isinstance(data, list)
        assert data[0]["title"] == "X"

    def test_load_from_missing_file_starts_empty(self, tmp_path):
        filepath = str(tmp_path / "nonexistent.json")
        store = TaskStore(filepath)
        store.load()
        assert len(store) == 0

    def test_load_pre_populated_file(self, sample_tasks_file: str):
        store = TaskStore(sample_tasks_file)
        store.load()
        assert len(store) == 2
        titles = [t.title for t in store.get_all()]
        assert "Buy groceries" in titles
        assert "Submit report" in titles

    def test_atomic_write_does_not_leave_tmp_file(self, tmp_tasks_file: str):
        """After save(), no .tmp file should remain in the directory."""
        store = TaskStore(tmp_tasks_file)
        store.add(self._make_task("Test"))
        store.save()
        dir_path = os.path.dirname(os.path.abspath(tmp_tasks_file))
        tmp_files = [f for f in os.listdir(dir_path) if f.endswith(".tmp")]
        assert tmp_files == []

    def test_corrupt_json_raises_value_error(self, tmp_path):
        filepath = str(tmp_path / "tasks.json")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("{not valid json")
        store = TaskStore(filepath)
        with pytest.raises(ValueError, match="Could not parse"):
            store.load()
