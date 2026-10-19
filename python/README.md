## Sample Python apps

This project uses [uv](https://docs.astral.sh/uv/) to manage Python, dependencies, and tooling.
Please use uv for everything in this exercise: don't use `pip install`, `poetry`, or a manually
created virtual environment for project dependencies.

Start the docker container, which gives you a bash prompt with this directory mounted
and uv already installed:

    ./docker.sh        # docker.bat on Windows

Inside the container, setup the environment:

    uv sync

The exercise has three parts. Run only the test for the part you're working on:

    # Part 1: openc3/get_env.py
    uv run pytest tests/test_get_env.py

    # Part 2: openc3/lookup.py
    uv run pytest tests/test_lookup.py

    # Part 3: implement openc3/request.py
    uv run pytest tests/test_request.py

Lint, format, and type check:

    uv run ruff check .
    uv run ruff format .
    uv run ty check

If you need to add a dependency, use uv so `pyproject.toml` and `uv.lock` stay in sync:

    uv add <package>
    uv add --dev <package>
