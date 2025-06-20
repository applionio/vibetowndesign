# Technical Documentation Prompts

## API Documentation

```
Generate comprehensive API documentation for [ENDPOINT_NAME].

Context:
- Base URL: [BASE_URL]
- Authentication: [AUTH_TYPE]
- Purpose: [WHAT_IT_DOES]

Include:
1. Endpoint overview and purpose
2. HTTP method and full URL
3. Request parameters (query, path, body):
   - Parameter name
   - Type
   - Required/Optional
   - Description
   - Example values
4. Request headers
5. Example request (curl and programming language)
6. Response format:
   - Success response (200)
   - Error responses (4xx, 5xx)
   - Response schema
7. Rate limiting information
8. Common use cases
9. Related endpoints

Style: Developer-friendly, precise, with practical examples
```

## Code Documentation

```
Create detailed documentation for [CODE_FILE/FUNCTION/CLASS].

Code context:
[PASTE_CODE_HERE]

Generate:
1. Overview: What does this code do?
2. Architecture: How is it structured?
3. Key components:
   - Classes and their responsibilities
   - Important functions and methods
   - Data structures used
4. Dependencies and requirements
5. Configuration options
6. Usage examples
7. Common patterns and best practices
8. Error handling approach
9. Performance considerations
10. Testing approach

Format: Markdown with code blocks
Target audience: [junior developers/senior developers/architects]
```

## System Architecture Documentation

```
Document the system architecture for [SYSTEM_NAME].

System overview:
[PROVIDE_CONTEXT]

Cover:
1. High-level architecture diagram description
2. Component breakdown:
   - Component name and purpose
   - Technologies used
   - Interfaces/APIs
   - Data flow
3. Infrastructure requirements
4. Scalability considerations
5. Security measures
6. Deployment architecture
7. Monitoring and observability
8. Disaster recovery approach

Style: Technical but accessible, with clear explanations
Include: Mermaid diagrams where applicable
```

## Migration Guide

```
Create a migration guide from [OLD_VERSION/SYSTEM] to [NEW_VERSION/SYSTEM].

Context:
- Current state: [DESCRIBE_CURRENT]
- Target state: [DESCRIBE_TARGET]
- Major changes: [LIST_KEY_CHANGES]

Include:
1. Migration overview and timeline
2. Prerequisites and preparation steps
3. Step-by-step migration process
4. Data migration approach
5. Configuration changes required
6. Code changes needed
7. Testing strategy
8. Rollback procedure
9. Common issues and solutions
10. Post-migration verification

Format: Numbered steps with checkboxes
Tone: Clear, cautious, thorough
```