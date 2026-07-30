# AI Coding Guidance for `summer-tech-2025-week-b`

This repository is intentionally minimal.  At the moment it contains only a `README.md` with a one-line description: "python coding".  There are no packages, modules, tests, or configuration files yet.  It's effectively a blank canvas for solving small Python exercises or building simple scripts for a summer tech week assignment.

These instructions are written for AI coding agents (Copilot/ChatGPT) that land in the workspace for the first time.

## Big picture

- **Purpose**: A collection of Python code samples / exercises for a week‑long program.  There is no overarching architecture or service boundaries; each new file is likely a standalone script or module for a single prompt.
- **Structure**: There is currently no `src/`, `tests/`, or package.  Feel free to create directories as needed (`src/`, `examples/`, etc.).  Naming conventions are up to the exercise owner, but follow normal Python module rules (`snake_case.py`, packages with `__init__.py`).
- **External dependencies**: None are declared.  If you introduce third‑party packages, add a `requirements.txt` or `pyproject.toml` and mention installation instructions in the README.

## Developer workflow

- There is no build system or test harness.  Use the Python interpreter directly (`python file.py`, `python -m pytest` if tests are added).
- When writing code, include a comment at the top describing the goal of the file/exercise.
- Tests are not required but encouraged; if you add them, create a `tests/` directory and run with pytest.
- If you create new files, make sure imports are relative and usable when running from the project root.

## Project-specific conventions

- All new Python files should be runnable as scripts (i.e. include a `if __name__ == "__main__"` block when appropriate).
- Use simple, self‑contained functions. Avoid complex frameworks or unnecessary abstractions for this repository.
- Document any non‑standard decisions in `README.md` or comments near the code.

## Changing the repository

- Add a `requirements.txt` when third‑party libraries are needed; otherwise keep dependencies to the standard library.
- If the project grows, consider introducing a package structure (`src/` or the repository name as a package) and update these instructions accordingly.

> **Note for AI agents:** Because the codebase is tiny, always ask clarifying questions when the user’s request is vague.  There is no preexisting business logic to infer from; assume you are starting from scratch and request additional context whenever necessary.


---

These instructions can be updated later if the repository develops more structure or conventions.