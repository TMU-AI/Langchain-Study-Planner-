# DEV ENVIRONMENT — 🐳Docker + VS Code Dev Containers

This project runs inside a Docker container.
Your laptop is just a keyboard and a screen.
If it runs in the container, it runs for everyone.

---

## INSTALL DOCKER

Docker Desktop is the engine that runs our development universe.

Download and install it from:
[https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

Launch Docker Desktop and make sure it is running.

If Docker is not running, nothing else matters.

---

## INSTALL VS CODE DEV CONTAINERS

Open VS Code and install:

Dev Containers (by Microsoft)
[https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

This extension lets VS Code attach to Docker like a spaceship docking with a station.

---

## OPEN THE PROJECT INSIDE THE CONTAINER

Open the project folder in VS Code.

Open the command palette:

```bash
# Mac
Cmd + Shift + P

# Windows / Linux
Ctrl + Shift + P
```

Type:

```bash
>Dev Containers: Open Folder in Container...
```

Select the project folder.

VS Code will now:

* Build the Docker image
* Start a Linux container
* Reopen the project inside it

This takes a few minutes the first time.

Check the bottom-left corner.
If you see something like:

```bash
Dev Container: <project-name>
```

You are inside the machine.

---

## INSTALL PROJECT DEPENDENCIES ON YOUR OWN MACHINE (Optional)

This step is completely optional, as Docker will have everything you need. If you would like to install everything on your own machine, please keep reading

Open a VS Code terminal (Terminal → New Terminal).
This terminal is running inside the container.

Run:

```bash
pip install -r requirements.txt
```

Do not run this on your host machine.
Only inside the container.

---

## RUN THE PROJECT

Inside the container terminal:

```bash
python main.py
```

(or whatever the project’s entry file is)

At this point you are running inside the same environment every developer uses.

---

## IF SOMETHING BREAKS

Rebuild the container:

```bash
Dev Containers: Rebuild and Reopen in Container
```

This resets the environment and fixes most issues.

---

## VERIFY EVERYTHING

Inside the container terminal:

```bash
python --version
pip list
```

If these work, the system is alive.

---

This setup eliminates “works on my machine.”
Your laptop becomes a terminal.
The container becomes the computer.

That’s the quiet power move of modern engineering.
