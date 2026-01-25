# Langchain-Study-Planner-

AI-powered study planner portfolio project (TMU AIMLA). Participants build beginner-friendly, industry-relevant portfolio work around **agentic AI** and study planning based on real course materials.

## What this repository is

This repo is intentionally organized in a non-standard way:

- **`main` is a template branch**: onboarding, environment setup, example scripts, and sanity tests.
- **Participant work happens on separate branches**: each person implements features on their own branch. `main` is not a development nor production branch, and will be used for onboarding and documentation only.

This design keeps a stable starting point for beginners while still supporting collaboration through merges between other branches.

## Branch model (read this first)

### `main` (template branch)

The `main` branch should stay beginner-safe and reproducible:

- Setup instructions
- Minimal example scripts
- Minimal tests / environment checks
- Project overview and participation guide
- (Later) a participants + contributions overview

### Participant branches

Each participant works mostly independently on their own branch.

Branch naming convention:

```text
your-name/short-feature-name
```

Examples:

```text
antonio/pdf-reader
jane/data-cleaning
bob/prompt-tests
```

## Quickstart

Install Git on your system and clone this repo. 

Navigate to the directory where you want to clone the repository using `cd /your-directory` and run:

```bash
git clone https://github.com/TMU-AI/Langchain-Study-Planner-.git
```

### Option A (preferred): VS Code Dev Container

If you are new to Python environments, use the Dev Container. It standardizes setup across contributors, is hard to break by accident, and is easy to use.

1. Install [VS Code](https://code.visualstudio.com/Download) + [Docker Desktop](https://www.docker.com/products/docker-desktop/) + [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
2. Open this repo in VS Code
3. Run command: **Dev Containers: Reopen in Container** on the project root folder

New packages can be tested safely using `pip install` in the container. Packages installed this way will be removed when the container is deleted, so feel free to experiment.

Packages can be made persistent by adding them to the `requirements.txt` file. 

Installed extensions can be made persistent by adding them to the `devcontainer.json` file.

### Option B (optional): Local Python venv + any IDE

Requirements:

- Python 3.10+ (recommended)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Environment variables

Some examples require an LLM provider API key.

Create a `.env` file in the repo root:

```bash
OPENAI_API_KEY=your_key_here
```

This project uses [`python-dotenv`](requirements.txt:4) so scripts can load `.env` automatically. 

Be sure not to commit `.env` to Git, otherwise your API key will be exposed. `.env` has already been added to `.gitignore`, so you shouldn't have to worry about this.

## Sanity checks (beginner-friendly)

These checks are intended to confirm your environment is working.

1) **Import check** (no API key required):

```bash
python -c "import langchain; import langchain_openai; print('imports_ok')"
```

2) **Hello-world LLM call** (requires `OPENAI_API_KEY`):

```bash
python scripts/hello_openai.py
```

<!-- 3) **Run tests** (recommended):

```bash
pytest
```

Notes:

- The `scripts/` and `tests/` directories are part of the template-branch plan; if they are not present yet, check the Issues/PRs for the latest template updates. -->

## How to participate (workflow)

If you are new to GitHub, start here:

- [`documentation/NEW_TO_GITHUB.md`](documentation/NEW_TO_GITHUB.md:1)

Then follow the required workflow:

- [`documentation/GIT_WORKFLOW.md`](documentation/GIT_WORKFLOW.md:1)

Avoid common mistakes:

- [`documentation/COMMON_MISTAKES.md`](documentation/COMMON_MISTAKES.md:1)

The rule that matters most:

- Do **not** push to `main`. Any commits or PRs to `main` will be rejected due to branch protection rules.
- Work on your branch only.

## Repository layout (template branch)

- [`README.md`](README.md:1): project overview (this file)
- [`requirements.txt`](requirements.txt:1): Python dependencies
- [`.devcontainer/`](.devcontainer/:1): Dev Container configuration (preferred setup)
- [`documentation/`](documentation/:1): onboarding and workflow docs
- `scripts/`: example scripts (environment check, hello-world LLM call, etc.)
- `tests/`: minimal tests to verify setup and regressions

## Communication

- Discord: <https://discord.gg/NJWWDRT62U>
- Club website: <https://aimla-website.vercel.app/>

## Participants (to be filled near project end)

This section will be expanded on `main` later to highlight participants and link to their work.

| Participant | Branch | Highlights |
|---|---|---|
| Name | `name/feature` | One-line summary |

## Project motivation (context)

This initiative is designed to help students gain industry-relevant experience by executing end-to-end projects:

- proposal → implementation → presentation
- exposure to software development best practices (version control, virtual environments/containers, API key management)
- exposure to real workflows (branches, PRs, reviews)
- practice with modern agentic AI patterns (tools, memory, planning)

## License

TBD
