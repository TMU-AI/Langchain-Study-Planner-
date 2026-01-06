# Common Git Mistakes (Do Not Do These)

This file explains **what causes problems**.
It does NOT explain the workflow.

---

## ❌ Pushing to `main`

Never push directly to `main`.

Why this is bad:
- Breaks shared code
- Blocks teammates
- Creates merge conflicts

---

## ❌ Working Without a Branch

If you are not on your own branch, you are doing it wrong.

Check your branch:

```bash
git branch
```
If you see * main, stop.

 ## ❌ Skipping Commits
Working for a long time without committing:

Makes mistakes harder to fix

Makes reviews harder

Commit early.
Commit often.

## ❌ Vague Commit Messages
Bad:

```bash
sql
Copy code
update
final
stuff
```



Good:

```bash
sql
Copy code
Add LangChain prompt routing example
Fix typo in README
```

## ❌ Fear of Pull Requests
Pull Requests are required.

They are:

### Normal

### Expected

### How collaboration works

### __Not opening a PR is the mistake.__

## ❌ Ignoring Errors
If Git prints an error:

Stop

Read it

Ask for help

Ignoring errors makes things worse.

yaml
Copy code

---

This is now **operational documentation**, not teaching prose.

If someone messes up after reading this, it’s not a documentation problem — it’s a process enforcement problem (branch protection, required PRs). That’s the next lever once the repo goes live.






