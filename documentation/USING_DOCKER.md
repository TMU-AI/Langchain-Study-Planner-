

## `README.md` — Development Environment (Docker + VS Code Dev Containers)

```md
# 🐳 Development Environment (Docker + VS Code Dev Containers)

This project uses **Docker + VS Code Dev Containers** to provide a **fully reproducible development environment**.  
You do **not** install Python, libraries, or system packages on your own machine. Everything runs inside a container.

If your code runs in the container, it runs for everyone.

---

## 1️⃣ Install Docker Desktop

Docker Desktop is the engine that runs our development container.

Download and install:
https://www.docker.com/products/docker-desktop/

After installation:
- Open Docker Desktop
- Make sure it is running (you should see the Docker whale in your system tray)

---

## 2️⃣ Install VS Code Dev Containers Extension

Open **VS Code**, then install this extension:

> **Dev Containers** (by Microsoft)

You can find it in the Extensions tab or here:  
https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers

This extension lets VS Code open our project *inside* Docker instead of on your laptop.

---

## 3️⃣ Open the Project in a Dev Container

1. Open **VS Code**
2. Open the project folder normally (File → Open Folder)
3. Press:

```

Cmd + Shift + P   (Mac)
Ctrl + Shift + P  (Windows/Linux)

```

This opens the VS Code command palette.

4. Type:

```

Dev Containers: Open Folder in Container...

````

5. Select the **project folder**

VS Code will now:
- Build the Docker image
- Start the container
- Reopen the project inside it

This may take several minutes the first time.

You’ll know it worked when you see something like:

> `Dev Container: <project-name>`

in the bottom left corner of VS Code.

---

## 4️⃣ Install Python Dependencies (Inside the Container)

Once the container is running:

Open a terminal in VS Code (**Terminal → New Terminal**)

Run:

```bash
pip install -r requirements.txt
````

This installs all Python packages defined for the project.

⚠️ **Important**
Do NOT run this on your host machine.
Only run it inside the Dev Container terminal.

---

## 5️⃣ Running the Project

From the VS Code terminal inside the container, you can now run:

```bash
python main.py
```

(or whatever entry point the project uses)

Everything is now isolated, reproducible, and consistent across all machines.

---

## 🧠 Why We Use This

Without containers:

* Everyone has different Python versions
* Different OS libraries
* Random bugs that only appear on some laptops

With Dev Containers:

* Everyone runs the same Linux OS
* Same Python
* Same libraries
* Same behavior

Your laptop becomes just a keyboard and screen. The container does the real work.

---

## 🧯 If Something Breaks

Try rebuilding the container:

Open the command palette:

```
Dev Containers: Rebuild and Reopen in Container
```

This fixes 90% of issues.

---

## 🧪 Verify Everything Is Working

Run:

```bash
python --version
pip list
```

If these work, your environment is alive and healthy.

```
