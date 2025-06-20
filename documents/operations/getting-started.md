# Getting Started Guide

Welcome to the VibeTown Design Product Management Automation System! This guide will help you set up and start using the system.

## Prerequisites

- Node.js 18+ installed
- API keys for services you want to connect (Notion, Linear, OpenAI, etc.)
- Basic knowledge of YAML for configuration files

## Initial Setup

### 1. Install Dependencies

```bash
npm install
```

### 2. Configure Environment

Copy the example environment file and add your API keys:

```bash
cp config/.env.example config/.env
```

Edit `config/.env` with your actual API keys:
- `NOTION_API_KEY`: Get from https://www.notion.so/my-integrations
- `LINEAR_API_KEY`: Get from Linear settings
- `OPENAI_API_KEY`: Get from OpenAI platform

### 3. Test Connections

Verify your connectors are working:

```bash
npm run connector:test
```

## Your First Automation

### 1. Create a Custom Prompt

Create a new prompt in `prompts/custom/my-first-prompt.yml`:

```yaml
name: My First Prompt
description: A simple prompt for testing
version: 1.0.0

variables:
  - name: topic
    description: The topic to write about
    required: true

prompt: |
  Write a brief summary about {{topic}}.
  Keep it under 100 words and make it engaging.
```

### 2. Create a Simple Workflow

Create `workflows/my-workflow.yml`:

```yaml
name: My First Workflow
description: Test workflow to try the system

triggers:
  - type: manual

steps:
  - id: create_note
    name: Create Note in Notion
    connector: notion
    action: createPage
    parameters:
      title: "Test Note - {{date}}"
      properties:
        Type:
          select:
            name: "Note"
      content: "This is a test note created by automation!"
```

### 3. Run Your Workflow

```bash
npm run workflow:run my-workflow
```

## Common Use Cases

### Document Processing
- Analyze meeting notes and extract action items
- Summarize weekly reports
- Generate documentation from templates

### Task Automation
- Sync tasks between Notion and Linear
- Create recurring documents
- Generate status reports

### Prompt Management
- Version control your prompts
- Test prompts with different variables
- Share prompts across workflows

## Best Practices

1. **Keep Prompts Modular**: Create small, reusable prompts
2. **Use Version Control**: Track changes to prompts and workflows
3. **Test Incrementally**: Start with simple workflows and build up
4. **Document Everything**: Use clear names and descriptions
5. **Secure Your Keys**: Never commit API keys to git

## Troubleshooting

### Connection Issues
- Check API keys in `.env`
- Verify service is enabled in `config/services.json`
- Check network connectivity

### Workflow Failures
- Check logs in `logs/` directory
- Verify all required variables are set
- Test individual steps separately

## Next Steps

1. Explore example workflows in `workflows/`
2. Create custom agents for your specific needs
3. Set up scheduled workflows with cron expressions
4. Integrate with your existing tools

## Getting Help

- Check documentation in `documents/`
- Review examples in each directory
- Test components individually before combining

Happy automating! 🚀 