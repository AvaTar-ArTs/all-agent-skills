---
name: agent-creation-guidance
description: Provides a structured approach and best practices for creating new agents, covering purpose definition, skill integration, context management, and iterative refinement. Use when initiating the development of a new AI agent.
---

# Agent Creation Guidance

## Overview

This guide outlines a systematic process for developing new AI agents, emphasizing clarity, modularity, and adherence to project standards. It covers the essential steps from defining the agent's purpose to its final deployment and iteration.

## Core Principles

1.  **Purpose-Driven Design:** Clearly define the agent's primary objective and scope before development begins. What problem does it solve? What are its key inputs and outputs?
2.  **Skill Integration:** Leverage existing skills and tools effectively. Agents should orchestrate these capabilities rather than reimplementing them. Identify necessary skills and ensure they are available and correctly invoked.
3.  **Context Management:** Design agents to handle context efficiently. This includes managing conversation history, user preferences, and external information sources.
4.  **Iterative Refinement:** Develop agents incrementally. Start with a minimal viable product (MVP) and iterate based on testing and feedback.
5.  **Modularity and Readability:** Write clean, well-documented code. Agents should be composed of distinct, testable components.

## Development Workflow

### 1. Define Objective and Scope

*   **Identify the Need:** What task or problem will the agent address?
*   **Define Goals:** What are the desired outcomes? Be specific and measurable.
*   **Set Boundaries:** What are the agent's limitations? What will it *not* do?

### 2. Design Agent Architecture

*   **Core Logic:** How will the agent process input, reason, and generate output?
*   **Tool/Skill Usage:** Which specific tools or skills will the agent utilize? How will they be invoked?
*   **State Management:** How will the agent maintain state across interactions?
*   **Error Handling:** How will the agent gracefully handle errors, failures, or unexpected inputs?

### 3. Implementation

*   **Scaffolding:** Set up the basic agent structure (e.g., main script, configuration files).
*   **Component Development:** Implement the core logic, tool/skill orchestration, and state management.
*   **Coding Standards:** Adhere to project conventions for style, naming, and commenting.

### 4. Testing and Verification

*   **Unit Tests:** Test individual components and functions.
*   **Integration Tests:** Verify the agent's interaction with skills and tools.
*   **End-to-End Tests:** Simulate user interactions to validate overall functionality.
*   **Adversarial Testing:** Test edge cases and failure scenarios.

### 5. Documentation

*   **Agent Description:** Clearly document the agent's purpose, capabilities, and usage instructions.
*   **Internal Comments:** Explain complex logic or design decisions within the code.
*   **`README.md`:** Provide a comprehensive overview for users and developers.

## Best Practices

-   **Favor Explicit Composition:** Prefer composing agents from existing skills and simpler components rather than complex inheritance.
-   **Clear Prompts:** If the agent uses LLM prompts, ensure they are clear, specific, and well-structured.
-   **Security:** Be mindful of security implications, especially when interacting with external systems or handling sensitive data. Sanitize inputs and validate outputs.
-   **Performance:** Consider the performance implications of complex reasoning chains or frequent tool calls. Optimize where necessary.

---

## Generalization Notes

The principles of agent creation—purpose definition, skill integration, context management, and iterative development—are universally applicable across different AI platforms and frameworks. While specific tool names or syntax might vary, the core methodology remains consistent.
