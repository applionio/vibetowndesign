# Streamable MCP Server Guide

**Updated:** 2025-06-22

**Overview:**
`streamable-mcp-server` is an MCP server that exposes Chrome-automation tools for AI agents. Typical tasks: bookmark management, navigation & DOM interaction, scraping, screenshots, network capture, history & tab control.

## Bookmark Workflow

### Actions

#### Add
- **Tool:** `mcp7_chrome_bookmark_add`
- **Minimal Parameters:** `[url, title, parentId?, createFolder?]`
- **Example:**
  ```json
  {
    "tool": "mcp7_chrome_bookmark_add",
    "parameters": {
      "url": "https://example.com",
      "title": "Example",
      "parentId": "Bookmarks Bar/Docs",
      "createFolder": true
    }
  }
  ```

#### Delete
- **Tool:** `mcp7_chrome_bookmark_delete`
- **Minimal Parameters:** `[bookmarkId]` or `(url + title)`
- **Example:**
  ```json
  {
    "tool": "mcp7_chrome_bookmark_delete",
    "parameters": { "bookmarkId": "1207" }
  }
  ```

#### Search
- **Tool:** `mcp7_chrome_bookmark_search`
- **Minimal Parameters:** `[query, folderPath?, maxResults?]`
- **Example:**
  ```json
  {
    "tool": "mcp7_chrome_bookmark_search",
    "parameters": {
      "query": "",
      "maxResults": 1000
    }
  }
  ```

## Navigation & Interaction

**Tools:**
- `mcp7_chrome_navigate`: Open URL or refresh tab
- `mcp7_chrome_click_element`: Click by selector or coordinates
- `mcp7_chrome_fill_or_select`: Fill inputs / select options
- `mcp7_chrome_keyboard`: Send key presses
- `mcp7_chrome_get_interactive_elements`: List clickable elements with coords
- `mcp7_chrome_go_back_or_forward`: Navigate browser history

**Example:**
```javascript
// Navigate then click first story on HackerNews
{"tool":"mcp7_chrome_navigate","parameters":{"url":"https://news.ycombinator.com"}}
{"tool":"mcp7_chrome_click_element","parameters":{"selector":"a.storylink:first-of-type"}}
```

## Scraping & Screenshot

**Tools:**
- `mcp7_chrome_get_web_content`: Fetch HTML or visible text
- `mcp7_chrome_screenshot`: Capture full-page or element screenshot

**Example:**
```json
{"tool":"mcp7_chrome_get_web_content","parameters":{"selector":"h1","htmlContent":false}}
```

## Network & Debugging

- **Capture WebRequest:** `mcp7_chrome_network_capture_start` / `stop` (no response bodies)
- **Capture Debugger:** `mcp7_chrome_network_debugger_start` / `stop` (includes bodies)

## History & Tabs

**Tools:**
- `mcp7_chrome_history`: Query browsing history
- `mcp7_chrome_close_tabs`: Close tabs by id or URL
- `mcp7_get_windows_and_tabs`: Inspect open windows / tabs

## Best Practices

- Explain first, act second – state purpose before tool call.
- Be idempotent – search before add/delete.
- Limit results – tune `maxResults` to keep responses small.
- Prefer selectors over coordinates for clicks.
- Avoid destructive automation without confirmation.
- Chunk related calls to reduce tool-overhead.

## Troubleshooting

- **Symptom:** "No bookmark found when deleting"
  - **Cause:** Wrong id/url
  - **Fix:** Search first and ensure id matches
- **Symptom:** "timeout on click"
  - **Cause:** Selector missing or page still loading
  - **Fix:** Increase timeout or wait and re-query elements
- **Symptom:** "Empty textContent from get_web_content"
  - **Cause:** Element hidden/outside viewport
  - **Fix:** Use `htmlContent:true` or scroll first

## Reference Tools

- `mcp7_chrome_bookmark_add`
- `mcp7_chrome_bookmark_delete`
- `mcp7_chrome_bookmark_search`
- `mcp7_chrome_click_element`
- `mcp7_chrome_close_tabs`
- `mcp7_chrome_fill_or_select`
- `mcp7_chrome_get_interactive_elements`
- `mcp7_chrome_get_web_content`
- `mcp7_chrome_go_back_or_forward`
- `mcp7_chrome_history`
- `mcp7_chrome_keyboard`
- `mcp7_chrome_navigate`
- `mcp7_chrome_network_capture_start`
- `mcp7_chrome_network_capture_stop`
- `mcp7_chrome_network_debugger_start`
- `mcp7_chrome_network_debugger_stop`
- `mcp7_chrome_network_request`
- `mcp7_chrome_screenshot`
- `mcp7_get_windows_and_tabs`
- `mcp7_search_tabs_content`
