# VibeTown Dashboard - AI Navigation Guide

*Streamlined guide for AI agents to efficiently interact with VibeTown Character Dashboard*

## Platform Overview
VibeTown is an **AI-powered interactive storytelling game** featuring:
- **90+ AI Characters** with unique personalities and conversation mechanics
- **47+ Locations** across the virtual town with media assets
- **Progressive storylines** with phase-based character behavior
- **Game mechanics**: Points, gems, levels, boosters, and user progression
- **Interactive personality traits** with video/media management
- **Location-based character interactions** and story progression

## Quick Start
- **Dashboard URL**: `https://vibetown.applion.us/admin/characters/{id}`
- **Example**: `https://vibetown.applion.us/admin/characters/262`
- **Admin Sections**: Users, Characters, Places, Levels, Boosters, Settings

## Button Selector Reference

### Primary Actions (Top-Right Buttons)
```css
/* Edit Character Button */
button:nth-of-type(1) /* "Edit" - Opens character edit form */

/* Profile Picture Button */  
button:nth-of-type(2) /* "PP" - Opens image upload (1080x1080) */

/* Activate/Deactivate Button */
button:nth-of-type(3) /* "Activate" - Toggles character status */
```

### Story Prompt Buttons (Precise Selectors)
```css
/* Core Story Configuration */
button[data-bs-target="#editCharacterModal"]         /* Edit Character */
a[data-bs-target="#editInstructionsModal"]          /* Persona Prompt */
button[data-bs-target="#editFirstStoryModal"]       /* First Story */
a[data-bs-target="#editFirstMessageModal"]          /* First Message */
a[data-bs-target="#editStoryPromptModal"]           /* Scenario Prompt */
a[data-bs-target="#editStorySuggestionPromptModal"] /* User Context */

/* Progressive Behavior Prompts */
a[data-bs-target="#editPhase1PromptModal"]          /* Phase 1 (0-33%) */
a[data-bs-target="#editPhase2PromptModal"]          /* Phase 2 (34-66%) */
a[data-bs-target="#editPhase3PromptModal"]          /* Phase 3 (67-100%) */
a[data-bs-target="#editFinalVictoryResponseModal"]  /* Final Victory */
a[data-bs-target="#editOngoingObjectivePreventionModal"] /* Objective Prevention */
```

### Game Feature Selectors
```css
/* Personality Trait Buttons (Video Management) */
.video-indicator           /* All personality trait buttons */
/* Available traits: Casual, Cool, Dramatic, Funny, Sarcastic, Charming, 
   Coming, Going, Story Invite, Story Success, Story Fail */

/* Location Navigation */
tbody tr td:nth-of-type(2) a  /* Location link in character table */

/* Character Activation (Bottom Section) */
div:nth-of-type(5) button     /* Story section edit/activate button */
```

### Universal Modal Selectors
```css
[data-bs-toggle="modal"]    /* Any modal trigger button */
[type="submit"].btn-success /* Any form submit button */
.modal-backdrop             /* Click to close modal */
```

## Essential Workflows

### 1. Edit Character Information
```markdown
1. Navigate to: `/admin/characters/{id}`
2. Click: `button:nth-of-type(1)` (Edit button)
3. Fill form fields: #edit_character_short_name, #edit_character_full_name, etc.
4. Submit: Click `.btn-success` button
5. Close: Click outside modal area
```

### 2. Edit Story Prompts
```markdown
1. Navigate to: `/admin/characters/{id}`
2. Click: `button[data-bs-target="#editFirstStoryModal"]` (or desired prompt)
3. Edit content in modal
4. Submit: Click `.btn-success` button  
5. Close: Click outside modal area
```

### 3. Configure Phase Behavior
```markdown
1. Navigate to: `/admin/characters/{id}`
2. Click: `a[data-bs-target="#editPhase1PromptModal"]` (or Phase 2/3)
3. Configure behavior for progress range
4. Submit: Click `.btn-success` button
5. Close: Click outside modal area
```

### 4. Upload Profile Picture
```markdown
1. Navigate to: `/admin/characters/{id}`
2. Click: `button:nth-of-type(2)` (PP button)
3. Select file: 1080x1080 image via #character_pp
4. Submit: Click `.btn-success` button
5. Close: Click outside modal area
```

### 5. Manage Personality Trait Videos
```markdown
1. Navigate to: `/admin/characters/{id}`
2. Click: `.video-indicator` (any personality trait button)
3. Upload: MP4 or WebM file for trait-specific content
4. Submit: Click `.btn-success` button
5. Close: Click outside modal area
```

### 6. Navigate to Character Location
```markdown
1. Navigate to: `/admin/characters/{id}`
2. Click: `tbody tr td:nth-of-type(2) a` (location link)
3. Result: Opens location management at `/admin/places/{id}`
4. View: Location media, background assets, character assignments
```

### 7. Activate/Deactivate Character
```markdown
1. Navigate to: `/admin/characters/{id}`
2. Scroll to: Bottom story section
3. Click: `div:nth-of-type(5) button` (story edit button)
4. Click: "Aktif Et" (Activate) in modal
5. Close: Click outside modal area
```

## Modal Automation Pattern

### Standard Modal Flow
```javascript
// 1. Trigger modal
click('[data-bs-toggle="modal"]')

// 2. Wait for modal to appear
waitFor('.modal.show')

// 3. Fill form (if needed)
fill('#form-field', 'value')

// 4. Submit
click('[type="submit"].btn-success')

// 5. Close modal
click('.modal-backdrop') // or coordinates like {x: 200, y: 300}
```

### Button Text Variations
- **Turkish**: "Düzenle", "Yükleniyor..."
- **English**: "Edit", "Loading..."
- **Submit**: Always has `.btn-success` class
- **Trigger**: Always has `.btn-warning` or similar

## Character Configuration Reference

### Story Prompt Types
| Prompt | Purpose | Progress Range |
|--------|---------|----------------|
| First Story | Initial story setup | - |
| First Message | Character introduction | - |
| Scenario Prompt | Environmental context | - |
| User Context | User interaction guidelines | - |
| Phase 1 Prompt | Early behavior | 0-33% |
| Phase 2 Prompt | Middle behavior | 34-66% |
| Phase 3 Prompt | Late behavior | 67-100% |
| Final Victory | Success message | 100% |
| Objective Prevention | Failure handling | Any |

### Form Field IDs
```css
#edit_character_short_name  /* Character short name */
#edit_character_full_name   /* Character full name */
#edit_character_username    /* Character username */
#edit_place_id             /* Location dropdown */
#edit_job_id               /* Job dropdown */
#character_pp              /* Profile picture upload */
```

## Game Mechanics Reference

### Character Configuration Limits

#### Basic Character Information
| Field | Purpose | Character Limit | Field ID |
|-------|---------|----------------|----------|
| Story Title | Quest title for player | **25 characters max** | - |
| Story Description | Detailed story for player | **100 characters max** | - |
| Short Name | Character display name | Variable | `#edit_character_short_name` |
| Full Name | Complete character name | Variable | `#edit_character_full_name` |
| Username | Unique character identifier | Variable | `#edit_character_username` |
| Max Message Count | Conversation limits per interaction | Configurable | - |
| Target Point | Success metrics for completion | Numeric value | - |

#### Story Prompt Content Limits
| Prompt Type | Purpose | Content Constraints |
|-------------|---------|-------------------|
| First Message | Character introduction | Text field - unlimited |
| Instructions/Persona Prompt | Character personality definition | Text area - unlimited |
| Scenario Prompt | Environmental context | Text area - unlimited |
| User Context Setting | User interaction guidelines | Text area - unlimited |
| Phase 1 Prompt | Initial behavior (0-33% progress) | Text area - unlimited |
| Phase 2 Prompt | Middle behavior (34-66% progress) | Text area - unlimited |
| Phase 3 Prompt | Final behavior (67-100% progress) | Text area - unlimited |
| Final Victory Response | Success completion message | Text area - unlimited |
| Ongoing Objective Prevention | Failure/redirect handling | Text area - unlimited |

#### Media Asset Requirements
| Asset Type | Requirements | Field ID |
|------------|--------------|----------|
| Profile Picture | **1080x1080 pixels exactly** | `#character_pp` |
| Personality Trait Videos | MP4 or WebM format | Various modals |
| Location Background | Photos/Audio supported | Location management |

### Personality Traits (Video-Enabled)
| Trait | Purpose | Media Type |
|-------|---------|------------|
| Casual, Cool, Dramatic | Character mood responses | MP4/WebM videos |
| Funny, Sarcastic, Charming | Interaction styles | MP4/WebM videos |
| Coming, Going | Location transitions | MP4/WebM videos |
| Story Invite, Success, Fail | Game state responses | MP4/WebM videos |

### Location System
- **47+ Venues**: Cafes, beach clubs, libraries, lighthouses, etc.
- **Media Assets**: Background photos, audio, video support
- **Character Assignment**: Each character tied to specific location
- **Navigation**: Click character location to manage venue

### User Management
- **Points & Gems**: Game currency and rewards
- **Premium Status**: Account tier tracking
- **Story Progress**: User-character interaction history
- **Device Tracking**: UID and device ID monitoring

## Troubleshooting

### If Buttons Don't Respond
1. **Refresh page** - Resets interface state
2. **Use coordinates** - Click at specific x,y position
3. **Check for overlays** - Modal might be blocking interaction
4. **Try direct URL** - Navigate directly to target

### If Modals Won't Close
1. **Click backdrop** - Outside modal area (most reliable)
2. **Use coordinates** - Click at {x: 200, y: 300}
3. **Escape key** - Press Escape
4. **Refresh page** - Last resort

### Quick Navigation URLs
```
# Core Management
/admin/characters           # Character list & management
/admin/characters/{id}      # Individual character details
/admin/places              # Location/venue management  
/admin/places/{id}         # Individual location details
/admin/users               # User account management
/admin/users/{id}/stories  # User story progression tracking

# Game Systems  
/admin/levels              # Game progression levels
/admin/boosters            # Enhancement items & rewards
/admin/instructions        # System guidance & tutorials
/admin/settings            # Platform configuration
/admin/waitlist            # User queue management
```

---

*This guide provides precise selectors and streamlined workflows for reliable VibeTown dashboard automation.* 