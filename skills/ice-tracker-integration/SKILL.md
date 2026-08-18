---
name: ice-tracker-integration
description: Use when working on ICE Tracker project development, needing Git AI assistance specific to this project, or analyzing project architecture
---

# ICE Tracker Assistant Skill

## Description
Provides specialized assistance for the ICE Tracker project, including development guidance, Git AI integration help, and project-specific knowledge.

## Capabilities

### 1. Project Analysis and Navigation
- Analyze the ICE Tracker project architecture and functionality
- Explain the different project variants (v2-v7) and their features
- Provide guidance on the technical stack (Next.js 14, React 18, TypeScript, Leaflet, rss-parser)

### 2. Git AI Integration Assistance
- Help with Git AI setup and configuration for the project
- Explain Git AI attribution tracking and best practices
- Assist with Git AI commands and workflows specific to the project
- Troubleshoot Git AI issues related to the project

### 3. Development Guidance
- Provide guidance on the project's codebase and structure
- Explain the mapping functionality and RSS feed integration
- Help with filtering and UI components
- Assist with variant-specific features (v2-v7)

### 4. Documentation and Best Practices
- Explain project-specific documentation
- Provide guidance on security and privacy considerations
- Share best practices for contributing to the project
- Explain the CI/CD workflows and automation

## Usage Patterns

### When to Use
- When working on ICE Tracker development
- When needing Git AI assistance specific to this project
- When analyzing project architecture or features
- When setting up development environment
- When troubleshooting project-specific issues

### Examples
- "How does the mapping functionality work?"
- "Explain the Git AI integration in this project"
- "What are the different project variants?" 
- "Help me understand the RSS feed integration"
- "How do I set up the development environment?"

## Project-Specific Knowledge

### Key Features
- Live news feed from ICE.gov RSS feeds (Enforcement & Removal, Breaking News)
- Interactive US map showing ERO field offices (blue markers) and enforcement news (red markers)
- Filtering by state and source
- Direct links to official ICE news releases and field office information

### Technical Architecture
- Next.js 14 with App Router
- React 18 and TypeScript
- Leaflet with react-leaflet for mapping
- rss-parser for consuming ICE RSS feeds
- Multiple project variants (v2-v7) with different capabilities

### Git AI Integration
- Line-level attribution tracking for AI vs human contributions
- Checkpoint system for tracking AI-assisted development
- CI workflow for maintaining attribution during squash/rebase merges
- Integration with Cursor and other AI development tools

## Best Practices for This Project

### Development
- Use standard Next.js development workflow (npm install, npm run dev)
- Leverage Git AI for tracking AI-assisted development
- Follow existing code patterns and architecture
- Maintain proper attribution tracking with Git AI

### Git AI Usage
- Run 'git-ai status' after AI edits to see attribution
- Use 'git-ai blame <file>' for line-level attribution during code reviews
- Run 'git-ai stats' to measure AI adoption in the project
- Keep hooks enabled to maintain proper attribution

### Security & Privacy
- Keep community reports stored locally in browser only
- Use proper credential management via ~/.env.d/github.env
- Maintain privacy controls for sensitive information

## Troubleshooting

### Common Issues
- Git AI hooks not recording: Run 'git-ai install-hooks'
- Attribution not showing: Verify hooks are working with 'git-ai status'
- Mapping issues: Check Leaflet configuration and API keys
- RSS feed problems: Verify feed URLs and parsing logic

### Verification Commands
- 'git-ai status' - Check Git AI setup and recent checkpoints
- 'git-ai stats' - View overall AI adoption metrics
- 'git-ai blame <file>' - Check line-level attribution
- 'git-ai diff HEAD' - See changes with AI attribution