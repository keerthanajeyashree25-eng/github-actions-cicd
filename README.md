# Automated CI/CD Pipeline with GitHub Actions

Automated CI/CD pipeline using GitHub Actions, Python, Flask, pytest, and Docker.

A beginner-friendly Flask project that runs linting and unit tests on every
push to `main` and pull request targeting `main`. After both checks pass,
GitHub Actions builds a Docker image. Pushes to `main` also publish that image
to GitHub Container Registry (GHCR).

![CI/CD workflow](https://github.com/keerthanajeyashree25-eng/github-actions-cicd/actions/workflows/ci-cd.yml/badge.svg)

## Project structure

```text
github-actions-cicd/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── .dockerignore
├── .flake8
├── .gitignore
├── Dockerfile
├── README.md
├── requirements-dev.txt
└── requirements.txt
```

## Technologies

- Python 3.12 and Flask
- pytest for unit tests
- Flake8 for linting
- Docker for containerizing the application
- GitHub Actions for continuous integration and delivery
- GitHub Container Registry (GHCR) for published images

## Run locally

Run these commands from the project directory. Python 3.12 is recommended.

### 1. Create and activate a virtual environment

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux, activate it with:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### 2. Install application and development dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

### 3. Run the application

```bash
python -m app.main
```

Open `http://127.0.0.1:5000/` for the welcome JSON or
`http://127.0.0.1:5000/health` for the health JSON. Stop the server with
Ctrl+C.

## Tests and linting

Run the unit tests and see each test result:

```bash
python -m pytest -v
```

Run Flake8 over the application and tests:

```bash
python -m flake8 app tests
```

The Flake8 settings, including an 88-character line limit, are in `.flake8`.

## Build and run with Docker

Build the image from the project directory:

```bash
docker build -t flask-cicd-demo .
```

Start the container and map port 5000:

```bash
docker run --rm -p 5000:5000 flask-cicd-demo
```

Visit `http://127.0.0.1:5000/` or `http://127.0.0.1:5000/health`, then stop
the container with Ctrl+C.

## GitHub Actions workflow

The workflow is defined in `.github/workflows/ci-cd.yml`.

1. **Lint** checks out the code, installs dependencies, and runs Flake8.
2. **Test** checks out the code, installs dependencies, and runs pytest with
   verbose test output.
3. **Build and publish Docker image** starts only after lint and test pass. It
   builds an image for pushes and pull requests, and logs in to GHCR and pushes
   `latest` and commit-SHA tags only for a push to `main`.

The workflow uses the built-in `GITHUB_TOKEN`; no password or personal access
token is stored in the repository. The Docker job has the `packages: write`
permission needed to publish images. Pull requests do not publish images.

## Publish from GitHub

### 1. Create the repository and push this project

On GitHub, create a **public** repository named `github-actions-cicd`. Do not
initialize it with a README, license, or `.gitignore`, because this project
already includes those files. In a terminal opened in this project directory,
run:

```bash
git init
git add .
git commit -m "Add Flask CI/CD example"
git branch -M main
git remote add origin https://github.com/keerthanajeyashree25-eng/github-actions-cicd.git
git push -u origin main
```

If Git is already initialized, skip `git init`; if `origin` already exists,
update it with
`git remote set-url origin https://github.com/keerthanajeyashree25-eng/github-actions-cicd.git`.

### 2. Allow Actions to publish packages

In the repository, open **Settings → Actions → General**. Under **Workflow
permissions**, allow read and write permissions (or ensure the workflow's
`packages: write` permission is permitted by your organization policy), then
save. GitHub Actions is enabled by default; if prompted, enable it under the
repository's **Actions** tab.

### 3. Check the workflow

Open the **Actions** tab and select **CI/CD** to view the run and its job logs.
Wait for the Lint, Test, and Build and publish Docker image jobs to finish.
Green checkmarks indicate that the run succeeded. Pull requests also run all
three jobs, but do not push an image.

### 4. Find the published image

After a successful push to `main`, the image is available as:

```text
ghcr.io/keerthanajeyashree25-eng/github-actions-cicd:latest
```

The workflow also publishes a tag containing the commit SHA. Find the package
under your GitHub profile or organization **Packages** page. To let anyone pull
it, open the package's settings and set its visibility to **Public** if it is
not already public. Then pull and run it with:

```bash
docker pull ghcr.io/keerthanajeyashree25-eng/github-actions-cicd:latest
docker run --rm -p 5000:5000 ghcr.io/keerthanajeyashree25-eng/github-actions-cicd:latest
```
