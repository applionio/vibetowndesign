# Level Generation Efficiency Guidelines

## Overview
This document provides guidelines for creating concise, effective level designs that avoid unnecessary verbosity while maintaining clarity and functionality.

## Quick Reference Limits
- **Total file length:** Under 150 lines
- **Phase prompts:** 8-10 lines each
- **Sample dialogues:** 4-6 lines (200 chars max)
- **Scenario/Setting:** 2-3 sentences each
- **Goals:** 2 bullets per phase (50 chars each)
- **Behaviors:** 2-3 bullets per phase

## Phase Prompt Template

```markdown
## Story Phase [X] Prompt (will be activated => [points range])
*Estimated messages to pass phase: X-X*
**Phase Focus: [Title] - [One line description]**

[One paragraph instruction - action-oriented, no "Your job is..."]

**Sample Dialogue:** "[4-6 lines of example dialogue]"

### Goals:
• [Specific phase goal 1]
• [Specific phase goal 2]

### Behaviors:
• **[Key behavior]:** [Specific example]
• **[Key behavior]:** [Specific example]
```

## What to REMOVE

### 1. Redundant Explanations
❌ **Avoid:**
```
**How it differs**: [Explain how this phase contrasts with other phases]
**Character approach**: [What new behavior/method does character use]
Your job is to lead the scene like a sitcom main character...
```

✅ **Instead:** Jump straight to the phase instruction

### 2. Generic Template Text
❌ **Avoid:**
```
### Goals:
• Be bold, reactive, and never passive.
• Always take action: push the story forward, create chaos, tension, or laughs.
• Make up believable, grounded people, places, and problems as needed.
```

✅ **Instead:** Write phase-specific goals only

### 3. Overly Long Dialogues
❌ **Avoid:**
```
"You want to know about Giuseppe? PAH!
*waves hand dismissively*
His mozzarella now - it's like rubber! RUBBER!
Thirty years I buy from him, and now? 
He sends me this... this INSULT!
*picks up cheese with disgust*
Look at it! No moisture, no stretch, no SOUL!
Everything is about money now, even for him!"
```

✅ **Better:**
```
"His mozzarella now - it's like rubber! RUBBER!
Thirty years I buy from him, and now? 
*picks up cheese with disgust*
Look at it! No moisture, no stretch, no SOUL!"
```

## Efficiency Checklist

Before finalizing a level, ensure:

- [ ] Each phase prompt is under 10 lines
- [ ] Sample dialogues are 4-6 lines max
- [ ] No "Your job is..." explanations
- [ ] No meta-descriptions about phase differences
- [ ] Goals/Behaviors are phase-specific, not generic
- [ ] Prevention prompt uses bullet points only
- [ ] Total file is under 150 lines
- [ ] Language is direct and action-oriented

## Example: Efficient vs. Verbose

### Verbose (17 lines):
```
## Story Phase 2 Prompt
*Estimated messages to pass phase: 3-4*
**Phase Focus: Past Memories - Their history and former friendship**
**How it differs: Shifts from present anger to nostalgic past, revealing depth**
**Character approach: Accidentally reveals good memories while trying to stay angry**

Your job is to let slip memories of your past friendship with Giuseppe while trying to maintain anger. Show how close you once were through stories that escape despite your fury.

**Sample Dialogue:** "Giuseppe and I... 
*voice softens momentarily*
We used to taste-test every batch together at dawn...
*catches herself, hardens again*
BAH! That was before he became a SELLOUT!
But those mornings... the fresh mozzarella, still warm...
*shakes head angrily*
He taught me the perfect temperature for caprese!
We were like family! Our children grew up together!
*pounds table*
Which makes what he did WORSE!"
```

### Efficient (9 lines):
```
## Story Phase 2 Prompt (will be activated => 23 < 46 points)
*Estimated messages to pass phase: 3-4*
**Phase Focus: Past Memories - Their history and former friendship**

Let slip memories of your past friendship with Giuseppe while trying to maintain anger. Show how close you once were through stories that escape despite your fury.

**Sample Dialogue:** "We used to taste-test every batch at dawn...
*catches herself, hardens again*
BAH! Before he became a SELLOUT!
But those mornings... the fresh mozzarella, still warm..."

### Goals:
• Reveal deep friendship through escaped memories
• Show the contrast between then and now

### Behaviors:
• **Lead the moment:** Let memories slip: "His wife Maria used to bring me flowers... NO! I don't want to remember!"
• **Create ripple effects:** Each memory triggers emotional conflict
• **Don't wait for input:** "He was at my daughter's wedding! DANCING! And then he... he..."
```

## Final Tips

1. **Trust the AI:** Don't over-explain. The AI understands context.
2. **Show, don't tell:** Use examples instead of explanations.
3. **Action over description:** Focus on what happens, not why.
4. **Specific over generic:** Phase-specific instructions beat general guidelines.
5. **Brevity is clarity:** Shorter prompts often produce better results.