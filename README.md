# 🚀 Clone All My Repos (Because There Are Just Too Many)

You know that feeling when someone says:

> "Hey, can you send me your GitHub projects?"

And you reply:

> "Which 47?"

Yeah. Exactly.

There are simply too many legendary repositories to clone manually.  
So I made a script that clones **all my public GitHub repositories** in one go.

Because typing `git clone` 100 times is not scalable.  
And we like scalable things.

---

## 😎 What This Does

- Fetches all public repositories of **ryu878**
- Clones them via SSH
- Drops them into your current directory
- Makes you look efficient and slightly dangerous

It uses the GitHub API + standard `git clone`.

---

## ⚙️ Requirements

- Python 3.8+
- `git`
- `requests` library

Install dependency:

```bash
pip install requests
```

## 🧠 How It Works

### 1. Calls GitHub API:

```bash
https://api.github.com/users/ryu878/repos
```
### 2. Collects repository names (with pagination).

### 3. Runs:
```bash
git clone git@github.com:ryu878/REPO_NAME.git
```

For. Every. Repo.

No manual suffering required.

## 🏎️ Usage

Just run it inside the directory where you want everything cloned:

```bash
python clone_all.py
```
Example:
```bash
mkdir ryu-world
cd ryu-world
python clone_all.py
```

Boom 💥
All repos cloned into **ryu-world/**.
