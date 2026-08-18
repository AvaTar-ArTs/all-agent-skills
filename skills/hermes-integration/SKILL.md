---
name: hermes-integration
description: Manage, configure, and operate the Hermes Agent as an isolated containerized service within the Superpowers ecosystem.
platforms: [linux, macos, windows]
prerequisites:
  commands: [docker]
---

# Hermes Integration Skill

## Description
Manage, configure, and operate the Hermes Agent as an isolated containerized service within the Superpowers ecosystem.

## Usage
- `hermes-manage start` - Start Hermes Agent in a Docker container.
- `hermes-manage stop` - Stop the Hermes Agent container.
- `hermes-manage status` - Check container status.
- `hermes-manage logs` - View logs.
- `hermes-manage config` - Sync configuration files between host and agent container.

## Prerequisites
- Docker installed and running.
- Hermes Agent codebase at `~/.hermes/hermes-agent`.

## Workflow Integration
This skill bridges the Hermes Agent CLI with the Superpowers management tools.
