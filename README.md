# Langchain-Study-Planner

This repo is used to document an AI-powered study planner portfolio project, hosted by [TMU AIMLA](https://aimla-website.vercel.app/) (Artificial Intelligence & Machine Learning Association). Participants build **beginner-friendly**, **industry-relevant** portfolio work around **agentic AI** and study planning based on real course materials.

Questions? You can contact us through our [Discord](https://discord.gg/NJWWDRT62U) or through other channels listed on our [website](https://aimla-website.vercel.app/).

## Project Motivation

This initiative is designed to help beginning and intermediate students gain **industry-relevant experience** by executing **end-to-end** projects:

- proposal → implementation → presentation
- software engineering best practices (version control, virtual environments, API key safety)
- exposure to real workflows (branches, PRs, reviews)
- practice with modern agentic AI patterns (tools, memory, planning)

We consulted **experts in the field** (graduate students, junior/senior engineers, and senior managers) to determine what skills are most relevant and what experiences are most valuable. 

Here is what we determined:

- [Agentic AI](https://www.geeksforgeeks.org/artificial-intelligence/what-is-agentic-ai/) is one of the **latest industry trends** - AI programs capable of problem-solving for you. 
- Some examples: ChatGPT's [*Deep Research*](https://openai.com/index/introducing-deep-research/) feature; coding assistants like [Claude Code](https://claude.com/product/claude-code), [Github Copilot](https://github.com/features/copilot), [Kilo Code](https://kilo.ai/); search engine [AI summary](https://en.wikipedia.org/wiki/AI_Overviews) features.
- Undergraduate students are capable of Agentic AI because many undergraduates are Agentic AI interns **right now**.
- Agentic AI is **not math-heavy** and mostly depends on software engineering, which can be learned on the job (in fact the interns we spoke to did most of their learning on the job). 
- Targeting Agentic AI and developing experience with industry-standard software engineering practices will make your job application profile **much more competitive**.

## Repository Structure

This repo is intentionally organized in a non-standard way:

- **`main` is a template branch**: documentation, onboarding, environment setup, example scripts, and sanity tests.
- **Participant work happens on separate branches** `your-name/feature-name`: each person implements features on their own branch. 

This design keeps a stable starting point for beginners while still supporting collaboration through merges outside of `main`.


## How to Participate

1. Read and complete the [**intake form**](https://forms.gle/4W6WiGxsYbGJjBcY9) for more details. TMU email is required.

    *Not a TMU student but are interested? Contact the team!*

2. See the `Quickstart` section below to get started.

3. Read the `Project Proposal` section below to understand the project and how to contribute.

<!-- ## Branch model (read this first)

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
``` -->

## Quickstart

### Clone the repo 

 1. Install [Git](https://git-scm.com/install) on your machine
 2. Use your command line to **navigate to the directory** where you want to clone this repo
 3. Run the command below. This will create a copy of these files on your computer
```bash
git clone https://github.com/TMU-AI/Langchain-Study-Planner-.git
```

### Environment setup

#### Option A (preferred): VS Code Dev Container

If you are new to Python environments, use the [Dev Container](https://www.docker.com/blog/streamlining-local-development-with-dev-containers-and-testcontainers-cloud/). It standardizes setup across contributors, is hard to break accidentally, and is easy to use.

1. Install [VS Code](https://code.visualstudio.com/Download) + [Docker Desktop](https://www.docker.com/products/docker-desktop/) + [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
2. Open this repo in VS Code
3. Run command (`CTRL-SHIFT-P`): **Dev Containers: Reopen in Container** on the project root folder

New packages can be tested safely using `pip install` in the container. Packages installed this way will **be removed** when the container is deleted, so feel free to experiment.

Packages can be made **persistent** by adding them to the `requirements.txt` file. VSCode extensions can be made persistent by adding them to the `devcontainer.json` file.

#### Option B: Local Python venv + any IDE

If you prefer a more lightweight, traditional setup, you can use a local Python virtual environment (or use whatever environment manager you prefer - all requirements are listed in `requirements.txt`).

Requirements:

- Python 3.10+ (recommended)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Sanity checks

These checks are intended to confirm your environment is working.

1) **Import check** (no API key required):

```bash
python -c "import langchain; import langchain_openai; print('imports_ok')"
```

2) **Hello-world LLM call** (requires `OPENAI_API_KEY`, see below): 

```bash
python scripts/hello_openai.py
```

#### Environment variables

Some examples require an LLM provider API key. You can get one yourself from [OpenAI](https://platform.openai.com/api-keys), or reach out to the team for a shared key.

To set up your API key, open `.env` and add your key:

```bash
OPENAI_API_KEY=your_key_here
```

This project uses [`python-dotenv`](requirements.txt:4) so scripts can load `.env` automatically. 

<!-- Be sure not to commit `.env` to Git, otherwise your API key will be exposed. We have added `.env` to `.gitignore` to prevent this. -->

<!-- 3) **Run tests** (recommended):

```bash
pytest
```

Notes:

- The `scripts/` and `tests/` directories are part of the template-branch plan; if they are not present yet, check the Issues/PRs for the latest template updates. -->



<!-- ## Repository layout (template branch)

- [`README.md`](README.md:1): project overview (this file)
- [`requirements.txt`](requirements.txt:1): Python dependencies
- [`.devcontainer/`](.devcontainer/:1): Dev Container configuration (preferred setup)
- [`documentation/`](documentation/:1): onboarding and workflow docs
- `scripts/`: example scripts (environment check, hello-world LLM call, etc.)
- `tests/`: minimal tests to verify setup and regressions -->

## Project Proposal

This project is intended to help students practice their software engineering skills by solving a real problem using industry-relevant tools. 

### Problem Statement

Staying organized and on track with your studies is an ongoing challenge for many students. While there are many concerns about how AI is negatively affecting students' ability to learn, are there any positive use-cases where AI can be used to enhance students' learning?

### Solution 

We propose to build a LangChain agent that can help students stay organized and on track with their studies. The agent will be able to answer questions about the course material, structure their learning by providing a study plan based on their goals, and help students stay on track with their assignments. It will provide personalized recommendations by consulting course materials, syllabi, and other resources. 

### Proposed Roadmap

Good software is achieved through iterative development and incremental feature development. We suggest the following roadmap to develop the project: 

1. **Hello-world LLM call**
    - Set up your API key and run the provided test script
    - Understand the *basic structure* of an LLM prompt and how we will modify it

2. **Simple chatbot with chat history**
    - Build a simple chatbot that runs as a continuous program 
    - Understand how *context* is used to maintain state and how we will modify it 

3. **Simple chatbot with knowledge**
    - Implement a knowledge base for the chatbot to consult
    - Understand how *context* can be modified to steer the chatbot's behavior

4. **Chatbot with tools**
    - Implement tools for the chatbot to use to answer questions
    - Understand how *tools* are used to extend the capabilities of the chatbot

5. **Agentic chatbot with thinking**
    - Implement a thinking process for the chatbot to follow
    - Understand how *agents* are used to orchestrate the chatbot's behavior


## Project Guidelines

We will use a shared GitHub repo to give you exposure to **real workflows**, encourage you to keep track of your code changes, and to help you learn how to collaborate with others. 

If you are new to GitHub, start here: [`documentation/NEW_TO_GITHUB.md`](documentation/NEW_TO_GITHUB.md:1)

Review the project workflow: [`documentation/GIT_WORKFLOW.md`](documentation/GIT_WORKFLOW.md:1)

Avoid common mistakes: [`documentation/COMMON_MISTAKES.md`](documentation/COMMON_MISTAKES.md:1)

The rule that matters most:

- Do **not** push to `main`. Any commits to `main` will be rejected due to branch protection rules.
- Work on your branch  only.

## Participants (to be filled near project end)

| Participant | Branch | Highlights |
|---|---|---|
| Oliver Manuel (Project Lead) | `oliver/feature-name` | TBD |
| Antonio Souza (President) | `antonio/feature-name` | TBD |

## License

TBD
