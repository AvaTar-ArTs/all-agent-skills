---
name: git-ai-cursor-integration
description: Use when integrating Git AI tracking with Cursor workflows, setting up automatic checkpoint creation, or configuring attribution logging
---

# Git AI and Cursor Integration Skill

## Overview

Integrates Git AI tracking capabilities with Cursor's agent system for comprehensive AI-assisted development workflow. Combines Git AI's attribution tracking with Cursor's structured skill system and agent capabilities.

## Core Capabilities

### 1. Git AI Tracking Integration
- Automatic checkpoint creation during Cursor agent operations
- Line-level AI attribution tracking
- Commit history with AI model identification
- Statistics on AI vs human contributions

### 2. Cursor-Agent Workflow Integration
- Hooks for file editing and prompt submission
- Skill creation with Git AI tracking
- Agent execution with attribution logging
- Command integration with Git AI checkpoints

### 3. Multi-Ecosystem Coordination
- Coordinates between Git AI, Cursor, and other AI systems
- Maintains consistent attribution across platforms
- Integrates with systematic methodologies from Codex and Codex
- Ensures quality assurance across all systems

## Integration Process

### Phase 1: Setup and Configuration
- Verify Git AI installation and accessibility
- Configure Cursor hooks for Git AI integration
- Set up automatic checkpoint creation
- Validate cross-platform compatibility

### Phase 2: Workflow Integration
- Integrate Git AI checkpoints with Cursor agent operations
- Set up automatic tracking for file edits
- Configure prompt tracking and attribution
- Establish consistent attribution standards

### Phase 3: Skill and Agent Enhancement
- Create skills that leverage Git AI tracking
- Develop agents with built-in attribution logging
- Integrate systematic methodologies with attribution tracking
- Ensure quality processes include attribution validation

### Phase 4: Monitoring and Optimization
- Monitor attribution accuracy and completeness
- Optimize tracking performance
- Refine integration based on usage patterns
- Maintain consistent attribution standards

## Hook Integration

### File Editing Hook
Configured in hooks.json to run:
```
"~/.git-ai/bin/git-ai checkpoint cursor --hook-input stdin"
```

Triggers automatically when files are edited in Cursor, creating checkpoints that track AI contributions.

### Prompt Submission Hook
Also configured for before-submit-prompt events, ensuring all AI interactions are tracked.

## Usage Patterns

### 1. Skill Development with Attribution
When creating skills in Cursor, Git AI automatically tracks:
- AI-generated skill content
- Human modifications and refinements
- Iterative improvements and changes
- Model-specific contributions

### 2. Agent Operation Tracking
During agent operations, Git AI captures:
- AI decision-making processes
- Code generation and modifications
- Problem-solving approaches
- Solution implementations

### 3. Quality Assurance with Attribution
Combines with systematic methodologies to:
- Track quality improvements
- Attribute fixes to specific AI models
- Monitor effectiveness of different approaches
- Validate attribution accuracy

## Quality Standards

### Attribution Accuracy
- Ensure all AI contributions are properly attributed
- Maintain human vs AI distinction clearly
- Track model-specific contributions accurately
- Verify attribution completeness

### Integration Reliability
- Maintain consistent hook operation
- Ensure Git AI availability during Cursor operations
- Handle errors gracefully without disrupting workflow
- Preserve performance during tracking

### Cross-Ecosystem Consistency
- Maintain consistent attribution standards across systems
- Coordinate with other AI platforms (Codex, Codex, etc.)
- Ensure compatibility with systematic methodologies
- Support quality assurance processes

## Best Practices

### 1. Automatic Checkpoint Management
- Leverage Cursor hooks for automatic Git AI checkpoints
- Ensure consistent attribution without workflow disruption
- Monitor checkpoint frequency and relevance

### 2. Skill Development Tracking
- Track skill evolution from conception to refinement
- Attribute different AI models' contributions to skill development
- Monitor skill effectiveness over time

### 3. Agent Performance Monitoring
- Track agent effectiveness and improvement over time
- Attribute successful approaches to specific models/methodologies
- Monitor integration performance and reliability

## Integration with Systematic Methodologies

### With Codex Systematic Approaches
- Track systematic debugging processes
- Attribute root-cause analysis to specific contributors
- Monitor effectiveness of systematic methodologies

### With Codex Quality Processes
- Integrate quality assurance with attribution tracking
- Track validation and testing processes
- Monitor iterative refinement effectiveness

## Success Metrics

- Accurate and complete AI attribution tracking
- Seamless integration with Cursor workflow
- Consistent attribution standards across systems
- Reliable hook operation without performance impact
- Effective tracking of skill and agent development
- Successful integration with systematic methodologies

## Troubleshooting

### Common Issues
- Git AI not accessible: Verify installation and PATH
- Hooks not triggering: Check hooks.json configuration
- Attribution not appearing: Verify Git AI tracking is enabled
- Performance issues: Optimize checkpoint frequency

### Validation Steps
- Test hook functionality with sample operations
- Verify attribution appears in Git AI stats
- Confirm cross-platform consistency
- Validate systematic methodology integration