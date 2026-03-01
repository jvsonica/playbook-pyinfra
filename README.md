# playbook-pyinfra

Pyinfra playbooks for workstation setup.

## Prerequisites

- Python 3.11+
- `uv` installed (`pipx install uv` or see https://docs.astral.sh/uv/)

## Setup

```bash
uv venv
uv pip install pyinfra
```

## Run

```bash
uv run pyinfra inventory.py workstation.py
```

To run a different playbook, replace `workstation.py` with the file you want.

## Future work

- mise conf to install node and python 3.12 globally.
