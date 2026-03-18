from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from workflow_runner import PHASES, WorkflowRunner


class WorkflowRunnerTests(unittest.TestCase):
    def test_implementation_runs_all_prerequisite_phases(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            runner = WorkflowRunner(base_dir=Path(tmp))
            completed = runner.run("implementation")

            self.assertEqual(completed, PHASES)
            state = json.loads((Path(tmp) / ".superpowers/workflow/state.json").read_text())
            for phase in PHASES:
                self.assertTrue(state["phases"][phase]["completed"])
                self.assertTrue((Path(tmp) / ".superpowers/workflow" / f"{phase}.md").exists())

    def test_tdd_runs_only_up_to_tdd(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            runner = WorkflowRunner(base_dir=Path(tmp))
            completed = runner.run("tdd")

            self.assertEqual(completed, ["brainstorm", "plan", "tdd"])
            self.assertFalse(
                (Path(tmp) / ".superpowers/workflow" / "implementation.md").exists()
            )

    def test_running_again_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            runner = WorkflowRunner(base_dir=Path(tmp))
            runner.run("implementation")
            completed_again = runner.run("implementation")
            self.assertEqual(completed_again, [])

    def test_cli_enforces_phase_order(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(__file__).resolve().parents[1]
            result = subprocess.run(
                ["python", str(repo_root / "workflow_runner.py"), "plan", "--base-dir", tmp],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            state = json.loads((Path(tmp) / ".superpowers/workflow/state.json").read_text())
            self.assertIn("brainstorm", state["phases"])
            self.assertIn("plan", state["phases"])
            self.assertNotIn("tdd", state["phases"])


if __name__ == "__main__":
    unittest.main()
