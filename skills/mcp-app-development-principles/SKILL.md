---
name: mcp-app-development-principles
description: Guides the development of MCP applications with interactive UI widgets, covering MCP server architecture, tool integration, and widget communication.
---

# MCP Application Development Principles

## Overview

This skill provides principles for developing MCP applications that include interactive UI widgets rendered inline in the chat surface. It covers the architecture for remote MCP apps and locally packaged MCPB apps, focusing on how widgets attach to tools and communicate with the host. This skill aims to be general and independent of specific SDKs or frameworks.

## When to Use

*   When building MCP applications that require interactive UI elements.
*   For designing tools that need structured input (Forms) or user selection from lists (Pickers).
*   When implementing confirmation dialogs, visual previews, charts, maps, or live status displays.
*   When targeting environments that support the MCP Apps surface.

Avoid when:
*   Plain text or JSON output is sufficient.
*   The task does not require interactive UI elements.

## Core Concepts

*   **MCP App Architecture:** An MCP app is an MCP server that also serves UI resources. The UI layer is additive to the underlying MCP protocol.
*   **Deployment Shapes:**
    *   **Remote MCP App:** Hosted HTTP server; widgets served as resources, tool results reference them. The host fetches resources and brokers messages.
    *   **MCPB-packaged App:** Server runs locally within an MCPB bundle, used for driving local applications (e.g., file pickers, desktop app control).
*   **Widget Attachment:** Tools declare a UI resource via `_meta.ui.resourceUri`. The handler returns data; a separate resource serves the HTML. Communication occurs via `ontoolresult` and `sendMessage`.
*   **Widget Runtime (`App` Class):** Widgets use a standardized `App` class for bidirectional communication with the host and server.

## Best Practices

*   **Single Responsibility:** Keep widgets small and single-purpose (e.g., a picker picks, a chart displays).
*   **Data Flow:** Tools return data; widgets display it.
*   **Resource URI:** Use a standardized URI scheme (e.g., `ui://`) for widget resources.
*   **Mime Type:** Use the correct `RESOURCE_MIME_TYPE` (`"text/html;profile=mcp-app"`) for interactive rendering.
*   **Bundling:** Inline necessary JavaScript bundles to bypass Content Security Policy (CSP) restrictions in sandboxed iframes.
*   **Host Context:** Follow host theme (`light`/`dark`) using `app.getHostContext()` and CSS custom properties.
*   **Error Handling:** Widgets should degrade gracefully to text/JSON output if the host doesn't support the apps surface.

## Tool and Resource Registration

Tools declare UI resources via `_meta.ui.resourceUri`. Resources are registered separately to serve HTML content. The `App` class facilitates communication.

## Generalization Notes

The core concepts of MCP application architecture, widget communication, and tool/resource registration are general. Specific SDK imports or server implementations (like Express) are examples; focus on the MCP protocol and `App` class API for cross-platform compatibility. Abstract away platform-specific details when designing general skills.
