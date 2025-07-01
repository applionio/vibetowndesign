# Notion AI Integration Guide

**Version:** 1.0 | **Last Updated:** 2025-06-20

> A complete reference for using AI to manage your Notion workspace effectively.

## Quick Start

### Basic Page Operations

- **Create Page:** "Create a page called [Title] in [Database/Location]"
- **Update Content:** "Update the [Page Name] page with [new content]"
- **Search Content:** "Find pages about [topic]" or "Search for [keyword]"
- **Get Page Info:** "Show me the [Page Name] page"

### Database Operations

- **Add to Database:** "Add a new entry to [Database Name] with [properties]"
- **Create Database:** "Create a new database for [purpose]"
- **Move Pages:** "Move [Page Name] to [Database Name]"
- **List Entries:** "Show me all pages in [Database Name]"

## Workflows

### Creating Content

1.  Specify the target location (database/parent page).
2.  Provide the title and content.
3.  Set properties (status, category, etc.).
4.  Review and confirm the creation.

**Example:** "Create a tech spec called 'User Authentication' in Vibetown Docs with Draft status"

### Finding Information

1.  Use specific keywords related to your topic.
2.  Mention the database/area to search in.
3.  Ask for summaries if the content is lengthy.

**Example:** "Search Vibetown Docs for pages about the character memory system"

### Organizing Content

1.  Identify the content to move/organize.
2.  Specify the destination database.
3.  Update properties as needed.
4.  Verify the new organization.

**Example:** "Move the 'Combat System' page to the Tech Spec category"

## Pro-Tips

- **Be Specific:**
    - **Good:** "Create a PRD for the vibe selection feature in Vibetown Docs"
    - **Bad:** "Make a document"
- **Use Database Names:**
    - **Good:** "Add to Vibetown Docs database"
    - **Bad:** "Put it somewhere"
- **Include Properties:**
    - **Good:** "Set status to In Review and category to Tech Spec"
    - **Bad:** "Just create the page"
- **Batch Operations:**
    - **Efficient:** "Create 3 pages: [list] all in the same database"
    - **Slow:** Three separate requests

## Advanced Features

- **Smart Search:** Search across connected tools (Slack, Google Drive, etc.), use natural language (e.g., "What did we decide about the combat system?"), and search by date ("Show me documents updated this week").
- **Content Templates:** Request specific formats (e.g., "Create a PRD template"), use consistent structures, and include standard sections automatically.
- **Database Management:** Create relationships between databases, set up automated properties, and organize with tags and categories.

## Common Tasks & Commands

- **Create Meeting Notes:** "Create meeting notes for [date/topic] in Vibetown Docs"
- **Update Project Status:** "Update the [project] page status to In Progress"
- **Find Related Content:** "Show me all pages related to character development"
- **Create Task Lists:** "Create a task list for [project] with these items: [list]"
- **Generate Reports:** "Create a summary of all Tech Specs in Draft status"
- **Archive Content:** "Move completed projects to the archived section"

## Common Mistakes

- **Location Confusion:** Always specify WHERE to create content. When unsure, ask for the database.
- **Property Mismatches:** Check the database schema; use exact property names and values.
- **Search Limitations:** Try different keywords; be patient.
- **Batch Processing:** Don't request too many operations at once.

## Best Practices

### Content Creation

- Start with a purpose: What's this document for?
- Use templates to create reusable structures.
- Add metadata: Always fill in properties.
- Link related content for connections.

### Organization

- Use consistent, descriptive titles.
- Use database properties for proper categorization.
- Regularly archive outdated content.
- Use keywords strategically for search optimization.
- Maintain a clean, simple, clutter-free workspace.

### Collaboration

- Know who can access what (clear permissions).
- Keep statuses updated.
- Use comments for feedback and discussions.
- Track changes and updates (version control).

## Troubleshooting

### If Something Doesn't Work

- Check permissions: Do you have access?
- Verify the database: Does the target exist?
- Simplify the request: Break it into smaller steps.
- Try again: It might be a temporary issue.

### Getting Better Results

- Be more specific in your requests.
- Provide context about your goal.
- Ask for clarification when unsure.
- Use exact names from your workspace.

## Quick Reference

### Key Databases

- **Vibetown Docs:** Main documentation hub
- **Vibetown Professions:** Character/profession data
- **VibeTown Jobs:** Job/role information

### Essential Properties

- **Status:** Draft → In Review → Published → Outdated
- **Category:** Tech Spec, PRD, Guide, Best Practices, etc.
- **Feature Name:** Link to specific features
- **Author:** Track ownership
