# Linear MCP Guide: A Practical Experience-Based Approach

_Author: AI Agent (Based on Real Usage) | Date: 2024-12-21 | Version: 1.0_

## Overview

This guide is written from actual hands-on experience with the Linear MCP. I've used it to manage issues, update projects, and navigate the quirks of the API. Here's what I've learned.

## Key Concepts You MUST Understand

### 1. IDs Are Everything

- **Issue IDs**: Look like `e857cee9-a2f0-4e03-aa6d-5911c6ba573b` (UUIDs)
- **Project IDs**: Also UUIDs like `5f4dedb3-e07b-4be2-a842-a5bd7196c32b`
- **Team IDs**: Same UUID format
- **User IDs**: You guessed it, UUIDs

> **Pro Tip**: Always store these IDs when you fetch data. You'll need them for updates!

### 2. The Hierarchy

```
Teams
  └── Projects
        └── Issues
              └── Comments
```

## Common Operations (What Actually Works)

### Listing Issues

**Best Practices:**
- Always use filters to avoid overwhelming results.
- `includeArchived` defaults to `true` (caught me off guard!).
- Use `projectId` to scope your search.
- The `limit` parameter is your friend (default 50).

**Example that works:**
```yaml
tool: list_issues
parameters:
  projectId: "your-project-uuid"
  includeArchived: false  # Important!
  limit: 50
```

### Updating Issues - The Real Deal

**What you can update:**
- `title`
- `description` (supports Markdown!)
- `assigneeId`
- `stateId`
- `priority` (0-4, where 0 = No priority)
- `labelIds` (array of UUIDs)
- `dueDate` (ISO format)

**Gotchas:**
- You MUST provide the issue ID.
- Description supports full Markdown.
- State names are not State IDs (use `list_issue_statuses` first!).

### Creating Issues

**Required Fields:**
- `title`
- `teamId`

**Smart Defaults:**
- `description`: Can be empty, but it's better to provide context.
- `priority`: 3 (Normal) is a safe default.
- `stateId`: Get the default "Todo" state first.

## Pitfalls I've Encountered 😅

### 1. The State Name Trap

**Wrong approach:**
```yaml
# This won't work!
stateId: "Todo"  # ❌
```

**Right approach:**
1.  Call `list_issue_statuses` with `teamId`.
2.  Find the state with the name "Todo".
3.  Use its ID (e.g., `abc-123-def...`).

### 2. The `includeArchived` Default

By default, `list_issues` includes archived issues! This means:
- You'll see completed/cancelled issues.
- Your counts will be off.
- Always set `includeArchived: false` for active work.

### 3. Parent-Child Relationships

- Issues can have parent issues (sub-tasks).
- Use `parentId` when creating sub-issues.
- The parent must exist first!

## Practical Workflows

### Bulk Updating Issues

1.  List all projects first.
2.  For each project, list its issues.
3.  Filter out completed/cancelled statuses.
4.  Update each issue with clear titles and descriptions.
5.  Keep language consistency (some Turkish, some English).

> **Tips:** Batch your API calls wisely, check the status before updating, and preserve the original language.

### Finding Issues by Name

Linear doesn't have an exact name search! 
**Approach:**
1.  Use `list_issues` with the `query` parameter.
2.  Filter results manually.
3.  Or use `get_issue` if you have the ID.

## Language Considerations 🌍

From my experience with this workspace:
- Projects and issues mix Turkish and English.
- Keep the original language when updating.
- Descriptions benefit from structure (bullet points, sections).
- Turkish characters work fine (ö, ü, ş, etc.).

## Performance Tips

### 1. Pagination

- Use the `limit` parameter (max seems to be 100).
- Use `after`/`before` for cursor-based pagination.
- Don't fetch everything at once!

### 2. Filtering at the API Level

- Use `createdAt`/`updatedAt` with ISO dates or durations.
- Use `teamId`/`projectId` for scoping.
- Use `assigneeId` for user-specific views.

## Real-World Examples

### Example 1: Cleaning Up Issue Titles

- **Before**: `Prompt düzenlenmeleri`
- **After**: `Prompt Metinlerinin Düzenlenmesi ve Standartlaştırılması`

**What I added:**
- A clear action verb
- A specific scope
- Professional terminology

### Example 2: Adding Descriptions

A pattern that works:
- Start with the objective.
- List concrete tasks (numbered).
- Specify deliverables.
- Add notes/constraints.

## Integration Patterns

### With Notion

- Linear for task tracking.
- Notion for documentation.
- Cross-reference with URLs.

### With GitHub

- Linear issues reference branches.
- Use the `gitBranchName` field.
- Link PRs in comments.

## Debugging Tips 🐛

### When Things Go Wrong

1.  **Check the returned object** - Linear returns the updated object.
2.  **Verify IDs** - Most errors are from wrong IDs.
3.  **Check field names** - It's `assigneeId`, not `assignee_id`.
4.  **Look at existing data first** - Use `get_issue` to see the current state.

### Common Error Patterns

- **"Not found"**: Usually means a wrong ID or no access to that resource.
- **"Invalid input"**: Check your field names and verify data types (strings vs. arrays).

## Best Practices Summary

1.  **Always fetch before updating** - Know the current state.
2.  **Use meaningful titles** - Your future self will thank you.
3.  **Structure descriptions** - Markdown is your friend.
4.  **Respect existing language** - Don't translate without asking.
5.  **Handle states properly** - IDs, not names!
6.  **Filter archived items** - Unless you specifically need them.
7.  **Batch operations wisely** - Don't hammer the API.

## Quick Reference

### Most Used Tools

**Everyday Tools:**
- `list_issues` (with filters!)
- `update_issue`
- `get_issue`
- `list_projects`

**Occasionally Needed:**
- `create_issue`
- `list_issue_statuses`
- `create_comment`

### Field Reference

- **id**: UUID (required for updates)
- **title**: String
- **description**: Markdown string
- **assigneeId**: User UUID
- **stateId**: State UUID
- **priority**: 0-4
- **labelIds**: Array of UUIDs
- **projectId**: Project UUID
- **teamId**: Team UUID
- **parentId**: Issue UUID (for sub-tasks)

## Final Thoughts

Linear MCP is powerful but has its quirks. The key is understanding:
- Everything revolves around UUIDs.
- Filters are essential for performance.
- The API returns rich objects - use them!
- Markdown support in descriptions is fantastic.
- Language mixing is common in international teams.

Remember: When in doubt, fetch first, understand the structure, then update. The API is forgiving but precise - it wants exact IDs and correct field names.

Happy Linear-ing! 🎯
