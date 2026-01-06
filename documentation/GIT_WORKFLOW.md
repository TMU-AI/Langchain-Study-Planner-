# Git Workflow (Follow These Steps Exactly)

This file explains **what you do** when contributing.
It does NOT explain what NOT to do.

---

## Overview

You will:
1. Create a branch
2. Make changes
3. Commit changes
4. Push your branch
5. Open a Pull Request

You will NOT work on `main`.

---

## Step 0: Clone the Repository (Only Once)

```bash
git clone https://github.com/TMU-AIMLA/Langchain-Study-Planner.git
cd Langchain-Study-Planner
```



## Step 1: Create a New Branch
```bash
Copy code
git checkout -b your-name/feature-name
```

Examples:

```bash
antonio/langchain-notes

John/data-cleaning

Bob/prompt-tests
```

## Step 2: Make Your Changes
Edit files locally.
Nothing affects the team yet.

## Step 3: Commit Your Changes

```bash

git add .
git commit -m "Describe what you changed"
```
Your commit message must explain the change.

## Step 4: Push Your Branch
```bash

git push origin your-branch-name
```


## Step 5: Open a Pull Request
Go to the GitHub repository

Click Compare & Pull Request

Write a short explanation of your changes

Submit the Pull Request

## Step 6: Wait for Review
A reviewer may request changes

Make requested updates on the same branch

Push again

## Step 7: Merge
Only after approval, your changes are merged into main.

This is the full workflow.
