# VibeTown MCP Tools - AI Agent Guide

*Streamlined reference for AI agents to efficiently operate VibeTown character and story management*

## 🎯 Quick Navigation
- [Tool Categories](#-tool-categories)
- [Validation Quick Reference](#-validation-quick-reference)  
- [Common Workflows](#-common-workflows)
- [Function Reference](#-function-reference)

---

## 🎭 Platform Context

**VibeTown** is an AI-powered interactive storytelling game featuring:
- **90+ AI Characters** with dynamic personality progression
- **Story Phases**: Characters evolve behavior based on user progress (0-33%, 34-66%, 67-100%)
- **Game Mechanics**: Point systems, message limits, and progressive difficulty
- **47+ Locations** with character assignments and media assets

---

## 📂 Tool Categories

### 🎭 Character Core (1 tool)
**Purpose**: Define character personality and conversation style
- `edit_character_persona_prompt` - Core character personality definition

### 🏘️ Place Management (2 tools)
**Purpose**: Configure location names and environmental context
- `edit_place_name` - Location naming (2-25 characters)
- `edit_place_prompt` - Location environmental context (10-5000 characters)

### 📖 Story Configuration (12 tools)
**Purpose**: Complete story setup from introduction to completion

#### Story Basics (4 tools)
- `edit_character_first_story_title` - Quest name shown to player
- `edit_character_first_story_desc` - Story hook for player motivation
- `edit_character_first_story_target_point` - Difficulty/point requirement
- `edit_character_first_story_first_message` - Character's opening dialogue

#### Story Context (2 tools)
- `edit_character_first_story_scenario_prompt` - Environmental context setting
- `edit_character_first_story_user_context_setting` - User interaction guidelines

#### Progressive Behavior (3 tools)
- `edit_character_first_story_phase_1_prompt` - Early behavior (0-33% progress)
- `edit_character_first_story_phase_2_prompt` - Middle behavior (34-66% progress)  
- `edit_character_first_story_phase_3_prompt` - Late behavior (67-100% progress)

#### Story Completion (2 tools)
- `edit_character_first_story_final_victory_prompt` - Success completion message
- `edit_character_first_story_objective_prevention_prompt` - Failure/redirect handling

---

## ⚡ Validation Quick Reference

| Tool | Parameter | Constraint | Game Purpose |
|------|-----------|------------|--------------|
| `edit_place_name` | place_name | 2-25 characters | Location display name |
| `edit_place_prompt` | place_prompt | 10-5000 characters | Environmental context |
| `edit_character_first_story_title` | story_title | 5-25 characters | Quest name for player |
| `edit_character_first_story_desc` | story_desc | 10-100 characters | Player motivation text |
| `edit_character_first_story_target_point` | target_point | 5-500 points | Story difficulty level |
| `edit_character_first_story_first_message` | ai_first_message | 3-1000 characters | Opening dialogue |
| `edit_character_first_story_scenario_prompt` | scenario_prompt | 10-10000 characters | Environmental context |
| `edit_character_first_story_user_context_setting` | user_context_setting | 10-10000 characters | User interaction rules |
| `edit_character_first_story_phase_1_prompt` | phase_1_prompt | 10-10000 characters | Early behavior instructions |
| `edit_character_first_story_phase_2_prompt` | phase_2_prompt | 10-10000 characters | Middle behavior instructions |
| `edit_character_first_story_phase_3_prompt` | phase_3_prompt | 10-10000 characters | Late behavior instructions |
| `edit_character_first_story_final_victory_prompt` | final_victory_prompt | 10-1000 characters | Success message |
| `edit_character_first_story_objective_prevention_prompt` | objective_prevention_prompt | 10-1000 characters | Failure handling |

---

## 🚀 Common Workflows

### New Character Setup (Recommended Order)
```markdown
1. edit_character_persona_prompt → Core personality foundation
2. edit_character_first_story_title → Quest name (25 chars max)  
3. edit_character_first_story_desc → Player hook (100 chars max)
4. edit_character_first_story_target_point → Difficulty (5-500 range)
5. edit_character_first_story_first_message → Opening dialogue
```

### Story Flow Configuration (Sequential)
```markdown
1. edit_character_first_story_scenario_prompt → Environmental context
2. edit_character_first_story_user_context_setting → User interaction rules
3. edit_character_first_story_phase_1_prompt → Early behavior (0-33%)
4. edit_character_first_story_phase_2_prompt → Middle behavior (34-66%)
5. edit_character_first_story_phase_3_prompt → Late behavior (67-100%)
6. edit_character_first_story_final_victory_prompt → Success handling
7. edit_character_first_story_objective_prevention_prompt → Failure handling
```

### Location Management
```markdown
1. edit_place_name → Location display name
2. edit_place_prompt → Environmental context and atmosphere
```

---

## 📚 Function Reference

### Character Core

#### `edit_character_persona_prompt`
**Game Purpose**: Defines character's core personality, conversation style, and behavioral foundation across all story phases  
**AI Behavior Impact**: Controls how character responds throughout entire interaction  
**Required Parameters**: `username` (string), `persona_prompt` (string)  
**Example**: `"Gruff third-generation fisherman, guarded but wise, speaks in sea-bitten phrases"`

---

### Place Management

#### `edit_place_name`
**Game Purpose**: Sets the display name for locations where characters are assigned  
**Player Impact**: Location name shown in game interface and navigation  
**Required Parameters**: `place_id` (integer), `place_name` (string, 2-25 characters)  
**Example**: `"Fisherman's Jetty"`, `"Vibecoast Café"`

#### `edit_place_prompt`
**Game Purpose**: Defines environmental context and atmosphere for character interactions  
**AI Behavior Impact**: Provides setting context that influences character responses  
**Required Parameters**: `place_id` (integer), `place_prompt` (string, 10-5000 characters)  
**Example**: `"A weathered wooden jetty at sunrise. Fishing nets draped over railings, salt air, quiet morning atmosphere"`

---

### Story Configuration

#### `edit_character_first_story_title`
**Game Purpose**: Sets the quest name displayed to players when they discover the character  
**Player Impact**: First impression and story identification  
**Required Parameters**: `username` (string), `story_title` (string, 5-25 characters)  
**Example**: `"The Old Man and the Vibe"`, `"Welcome to Vibetown"`

#### `edit_character_first_story_desc`
**Game Purpose**: Provides story hook and motivation text shown to players  
**Player Impact**: Explains what the player will experience and accomplish  
**Required Parameters**: `username` (string), `story_desc` (string, 10-100 characters)  
**Example**: `"The ocean holds secrets, and so does Sergio. Earn his respect and maybe he'll share a tale."`

#### `edit_character_first_story_target_point`
**Game Purpose**: Sets point requirement for story completion, determining difficulty  
**Game Mechanics**: Higher points = harder story, affects phase progression thresholds  
**Required Parameters**: `username` (string), `target_point` (integer, 5-500)  
**Example**: `60` (moderate difficulty), `500` (very challenging)

#### `edit_character_first_story_first_message`
**Game Purpose**: Character's opening dialogue when player first interacts  
**Player Impact**: Sets tone and initiates the conversation  
**Required Parameters**: `username` (string), `ai_first_message` (string, 3-1000 characters)  
**Example**: `"Hmph. Another one blown in by the tourist tide, are ya?"`

#### `edit_character_first_story_scenario_prompt`
**Game Purpose**: Provides environmental context and setting for the AI character  
**AI Behavior Impact**: Influences character responses with situational awareness  
**Required Parameters**: `username` (string), `scenario_prompt` (string, 10-10000 characters)  
**Example**: `"You are at Fisherman's Jetty at sunrise, mending nets, absorbed in quiet work"`

#### `edit_character_first_story_user_context_setting`
**Game Purpose**: Defines user's role and context within the story scenario  
**AI Behavior Impact**: Helps character understand player's position and motivations  
**Required Parameters**: `username` (string), `user_context_setting` (string, 10-10000 characters)  
**Example**: `"USER is new to Vibetown, exploring at dawn, curious about the lone fisherman"`

#### `edit_character_first_story_phase_1_prompt`
**Game Purpose**: Controls character behavior during early story (0-33% point progress)  
**AI Behavior Impact**: Character is typically testing/evaluating the player  
**Required Parameters**: `username` (string), `phase_1_prompt` (string, 10-10000 characters)  
**Example**: `"You are testing the USER. Stay focused on work, short dismissive responses, see if they respect your space"`

#### `edit_character_first_story_phase_2_prompt`
**Game Purpose**: Controls character behavior during middle story (34-66% point progress)  
**AI Behavior Impact**: Character begins opening up, sharing small pieces of their world  
**Required Parameters**: `username` (string), `phase_2_prompt` (string, 10-10000 characters)  
**Example**: `"USER hasn't annoyed you. Share a tiny piece of your world, frame as challenge to their modern sensibilities"`

#### `edit_character_first_story_phase_3_prompt`
**Game Purpose**: Controls character behavior during late story (67-100% point progress)  
**AI Behavior Impact**: Character shows vulnerability, deeper connection potential  
**Required Parameters**: `username` (string), `phase_3_prompt` (string, 10-10000 characters)  
**Example**: `"Guard drops slightly. Hint at loneliness and history using sea metaphors. Seek quiet understanding"`

#### `edit_character_first_story_final_victory_prompt`
**Game Purpose**: Character's response when player successfully completes the story (100% points)  
**Player Impact**: Reward message showing relationship has been established  
**Required Parameters**: `username` (string), `final_victory_prompt` (string, 10-1000 characters)  
**Example**: `"You listen better than most. If you want to see a real catch, be here at dawn. Don't be late."`

#### `edit_character_first_story_objective_prevention_prompt`
**Game Purpose**: Character's response when player fails or takes story off-track  
**AI Behavior Impact**: Handles failure scenarios and redirects conversation  
**Required Parameters**: `username` (string), `objective_prevention_prompt` (string, 10-1000 characters)  
**Example**: `"You're all talk, no tide. Go bother the seagulls. I've got real work to do."`

---

## 💡 Best Practices for AI Agents

### Character Development Strategy
1. **Start with Persona**: Always begin with `edit_character_persona_prompt` to establish foundation
2. **Set Clear Goals**: Use appropriate `target_point` values (60-100 for beginners, 200+ for experienced)
3. **Progressive Revelation**: Design phases to gradually reveal character depth
4. **Consistent Voice**: Maintain character voice across all prompts

### Content Guidelines
- **Phase 1**: Character is guarded, testing player worthiness
- **Phase 2**: Character shares surface-level personal information  
- **Phase 3**: Character reveals vulnerability or deeper connection
- **Victory**: Character offers ongoing relationship or meaningful closure
- **Prevention**: Character maintains boundaries without being cruel

### Technical Considerations
- Always provide `username` parameter for character functions
- Use `place_id` (integer) for place functions, not place name
- Respect character limits to avoid validation errors
- Test story flow by considering point progression thresholds

---

*This guide enables efficient VibeTown character and story management through organized workflows and clear context understanding.* 