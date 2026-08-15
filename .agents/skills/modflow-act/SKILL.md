---
name: modflow-act
description: "Use when running the MODFLOW-2005 GitHub Actions workflow locally with act. Useful for smoke-testing CI jobs without pushing to GitHub."
---

# MODFLOW-2005 act Workflow

Use the repository root as the working directory:

```bash
cd /home/pluck/Documents/DisciplinedSoftware/Modernization/Code/mf2005
```

## Prerequisites

Install `act` if it is not already available:

```bash
# macOS
brew install act

# Linux / other
curl -s https://raw.githubusercontent.com/nektos/act/master/install.sh | bash
```

Verify the install:

```bash
act --version
```

## Common usage

List the available jobs defined in the GitHub Actions workflow:

```bash
act -l
```

Run the default workflow locally using the default event payload:

```bash
act
```

Run a specific workflow job, for example a CI job or a test job:

```bash
act -j <job-name>
```

Use the platform image matching the repo's CI environment:

```bash
act -P ubuntu-latest=ghcr.io/catthehacker/ubuntu:act-latest
```

## Useful flags

Dry run without executing the job steps:

```bash
act -n
```

Run with verbose logs:

```bash
act -v
```

Use a specific event payload file:

```bash
act push -W .github/workflows/ci.yml
```

## Repository-specific notes

This repo uses GitHub Actions and local workflow validation is useful before pushing changes that affect:

- build configuration
- Meson or Pixi task definitions
- test routing
- coverage generation
- release packaging

If a workflow references secrets or external services, prefer `-n` for a dry run or use the minimum required environment variables and `--container-architecture linux/amd64` when necessary.

## Validation expectations

After changing CI-related config or local workflow validation steps:

1. Run `act -l` to confirm the workflow is discovered.
2. Use `act -n` for a safe dry run before a full local execution.
3. Run the relevant job with `act -j <job-name>` when validating actual CI behavior.
4. If workflow execution fails because of Docker/runner issues, confirm the container image and platform flags match the local environment.
