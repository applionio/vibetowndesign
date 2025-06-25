# Streamable MCP Server Guide

**Updated:** 2025-01-25 (Version 3.0)

**Overview:**
`streamable-mcp-server` is an MCP server that exposes Chrome-automation tools for AI agents. Common tasks include: navigation, DOM interaction, scrolling, screenshots, network capture, bookmark management, and tab control.

## 🚀 Quick Start

### Essential Tools You'll Use Most:
1. `mcp_streamable-mcp-server_chrome_navigate` - Navigate to URLs
2. `mcp_streamable-mcp-server_chrome_inject_script` - **CRITICAL: Used for scrolling and DOM manipulation**
3. `mcp_streamable-mcp-server_chrome_screenshot` - Capture page state
4. `mcp_streamable-mcp-server_chrome_get_web_content` - Extract page content
5. `mcp_streamable-mcp-server_chrome_click_element` - Interact with elements

## 📜 Scrolling (JavaScript Injection Only)

**⚠️ IMPORTANT:** Scrolling ONLY works reliably through JavaScript injection. Keyboard methods (PageDown, ArrowKeys) do NOT work.

### Basic Scrolling Commands

All scrolling must use `mcp_streamable-mcp-server_chrome_inject_script` with `type: "MAIN"`:

```json
// Scroll down by pixels
{
  "tool": "mcp_streamable-mcp-server_chrome_inject_script",
  "parameters": {
    "type": "MAIN",
    "jsScript": "window.scrollBy(0, 500); // Scrolls down 500 pixels"
  }
}

// Scroll to specific position
{
  "tool": "mcp_streamable-mcp-server_chrome_inject_script",
  "parameters": {
    "type": "MAIN",
    "jsScript": "window.scrollTo(0, 1000); // Scrolls to 1000px from top"
  }
}

// Scroll to bottom of page
{
  "tool": "mcp_streamable-mcp-server_chrome_inject_script",
  "parameters": {
    "type": "MAIN",
    "jsScript": "window.scrollTo(0, document.body.scrollHeight);"
  }
}

// Scroll to top of page
{
  "tool": "mcp_streamable-mcp-server_chrome_inject_script",
  "parameters": {
    "type": "MAIN",
    "jsScript": "window.scrollTo(0, 0);"
  }
}
```

### Verifying Scroll Works - Visual Confirmation

To confirm scrolling is working, inject a visual indicator:

```json
{
  "tool": "mcp_streamable-mcp-server_chrome_inject_script",
  "parameters": {
    "type": "MAIN",
    "jsScript": "// Create scroll position indicator\nconst indicator = document.createElement('div');\nindicator.id = 'scroll-pos';\nindicator.style.cssText = 'position:fixed;top:20px;right:20px;background:#000;color:#fff;padding:10px;z-index:999999;font-family:monospace;';\nindicator.textContent = 'Scroll: 0px';\ndocument.body.appendChild(indicator);\n\n// Update on scroll\nwindow.addEventListener('scroll', () => {\n  indicator.textContent = 'Scroll: ' + window.pageYOffset + 'px';\n});"
  }
}
```

### Common Scrolling Patterns

```json
// Smooth scrolling
{
  "tool": "mcp_streamable-mcp-server_chrome_inject_script",
  "parameters": {
    "type": "MAIN",
    "jsScript": "window.scrollTo({ top: 1000, behavior: 'smooth' });"
  }
}

// Scroll to element
{
  "tool": "mcp_streamable-mcp-server_chrome_inject_script",
  "parameters": {
    "type": "MAIN",
    "jsScript": "document.querySelector('#section-id').scrollIntoView();"
  }
}

// Get current scroll position
{
  "tool": "mcp_streamable-mcp-server_chrome_inject_script",
  "parameters": {
    "type": "MAIN",
    "jsScript": "console.log('Current scroll:', window.pageYOffset);"
  }
}
```

## 🌐 Navigation & Basic Interaction

### Navigate to URL
```json
{
  "tool": "mcp_streamable-mcp-server_chrome_navigate",
  "parameters": {
    "url": "https://example.com"
  }
}
```

### Click Elements
```json
// Click by selector
{
  "tool": "mcp_streamable-mcp-server_chrome_click_element",
  "parameters": {
    "selector": "button.submit"
  }
}

// Click by coordinates
{
  "tool": "mcp_streamable-mcp-server_chrome_click_element",
  "parameters": {
    "coordinates": { "x": 100, "y": 200 }
  }
}
```

### Fill Forms
```json
{
  "tool": "mcp_streamable-mcp-server_chrome_fill_or_select",
  "parameters": {
    "selector": "input#email",
    "value": "user@example.com"
  }
}
```

## 📸 Screenshots & Content Extraction

### Take Screenshot
```json
// Visible viewport only
{
  "tool": "mcp_streamable-mcp-server_chrome_screenshot",
  "parameters": {
    "fullPage": false,
    "storeBase64": true
  }
}
```

### Get Page Content
```json
// Get text content
{
  "tool": "mcp_streamable-mcp-server_chrome_get_web_content",
  "parameters": {
    "textContent": true
  }
}
```

## 🔖 Bookmark Management

### Search Bookmarks
```json
{
  "tool": "mcp_streamable-mcp-server_chrome_bookmark_search",
  "parameters": {
    "query": "docs",
    "maxResults": 50
  }
}
```

### Add Bookmark
```json
{
  "tool": "mcp_streamable-mcp-server_chrome_bookmark_add",
  "parameters": {
    "url": "https://example.com",
    "title": "Example Site",
    "parentId": "Bookmarks Bar"
  }
}
```

## 💡 Complete Example: Scrolling Through a Page

Here's a full workflow showing how to navigate, add scroll indicator, and scroll:

```json
// 1. Navigate to a long page
{
  "tool": "mcp_streamable-mcp-server_chrome_navigate",
  "parameters": {
    "url": "https://en.wikipedia.org/wiki/JavaScript"
  }
}

// 2. Add visual scroll indicator
{
  "tool": "mcp_streamable-mcp-server_chrome_inject_script",
  "parameters": {
    "type": "MAIN",
    "jsScript": "const div = document.createElement('div');\ndiv.style.cssText = 'position:fixed;top:10px;right:10px;background:red;color:white;padding:10px;z-index:9999';\ndiv.id = 'scroll-indicator';\ndiv.textContent = 'Position: 0';\ndocument.body.appendChild(div);\nwindow.addEventListener('scroll', () => {\n  div.textContent = 'Position: ' + Math.round(window.pageYOffset) + 'px';\n});"
  }
}

// 3. Scroll down 500 pixels
{
  "tool": "mcp_streamable-mcp-server_chrome_inject_script",
  "parameters": {
    "type": "MAIN",
    "jsScript": "window.scrollBy(0, 500);"
  }
}

// 4. Take screenshot showing scroll position
{
  "tool": "mcp_streamable-mcp-server_chrome_screenshot",
  "parameters": {
    "fullPage": false
  }
}
```

## ⚠️ Important Notes

1. **Scrolling ONLY works with JavaScript injection** - Do not attempt to use keyboard methods
2. **Always use `type: "MAIN"`** in inject_script parameters
3. **Visual indicators help confirm scrolling** - Use them when debugging
4. **Some sites may have custom scroll containers** - You may need to target specific elements

## 🛠️ All Available Tools Reference

- `mcp_streamable-mcp-server_chrome_navigate`
- `mcp_streamable-mcp-server_chrome_inject_script` ⭐ (Required for scrolling)
- `mcp_streamable-mcp-server_chrome_screenshot`
- `mcp_streamable-mcp-server_chrome_get_web_content`
- `mcp_streamable-mcp-server_chrome_click_element`
- `mcp_streamable-mcp-server_chrome_fill_or_select`
- `mcp_streamable-mcp-server_chrome_bookmark_add`
- `mcp_streamable-mcp-server_chrome_bookmark_search`
- `mcp_streamable-mcp-server_chrome_bookmark_delete`
- `mcp_streamable-mcp-server_chrome_get_interactive_elements`
- `mcp_streamable-mcp-server_chrome_go_back_or_forward`
- `mcp_streamable-mcp-server_chrome_close_tabs`
- `mcp_streamable-mcp-server_chrome_history`
- `mcp_streamable-mcp-server_chrome_console`
- `mcp_streamable-mcp-server_chrome_network_capture_start/stop`
- `mcp_streamable-mcp-server_chrome_network_debugger_start/stop`
- `mcp_streamable-mcp-server_chrome_network_request`
- `mcp_streamable-mcp-server_get_windows_and_tabs`
- `mcp_streamable-mcp-server_search_tabs_content`

## 📚 Troubleshooting

**Scroll not working?**
- Ensure you're using `mcp_streamable-mcp-server_chrome_inject_script`
- Verify `type: "MAIN"` is set
- Check if page has custom scroll containers
- Add visual indicator to confirm

**Can't see scroll happen?**
- Use the visual indicator code above
- Take before/after screenshots
- Check console for errors with `mcp_streamable-mcp-server_chrome_console`
