# VibeTown Dashboard - Button Mappings Reference

*Detailed button mapping reference for AI automation of VibeTown Character Dashboard*

## Character Dashboard Actions

### Primary Character Management

#### Edit Character
- **Button**: `<button class="mb-2 me-2 btn btn-warning" data-bs-toggle="modal" data-bs-target="#editCharacterModal">`
- **Text**: "Karakter Düzenle"
- **Action**: Opens character edit modal
- **Accept**: `<button type="submit" class="btn btn-success btn-block">Düzenle</button>`
- **Close**: Click outside modal area

#### Persona Prompt Management
- **Button**: `<a class="mb-2" data-bs-toggle="modal" data-bs-target="#editInstructionsModal">`
- **Text**: "Persona Prompt"
- **Action**: Opens persona prompt editor
- **Accept**: `<button type="submit" class="btn btn-success btn-block">Düzenle</button>`
- **Close**: Click outside modal area

## Story Prompt Management

### Core Story Elements

#### First Story
- **Button**: `<button class="mb-2 me-2 btn btn-warning" data-bs-toggle="modal" data-bs-target="#editFirstStoryModal">`
- **Accept**: `<button type="submit" class="btn btn-success btn-block">Edit</button>`
- **Close**: Click outside modal area

#### First Message
- **Button**: `<a class="mb-2" data-bs-toggle="modal" data-bs-target="#editFirstMessageModal">`
- **Accept**: `<button type="submit" class="btn btn-success btn-block">Edit</button>`
- **Close**: Click outside modal area

#### Scenario Prompt
- **Button**: `<a class="mb-2" data-bs-toggle="modal" data-bs-target="#editStoryPromptModal">`
- **Accept**: `<button type="submit" class="btn btn-success btn-block">Edit</button>`
- **Close**: Click outside modal area

#### User Context Setting
- **Button**: `<a class="mb-2" data-bs-toggle="modal" data-bs-target="#editStorySuggestionPromptModal">`
- **Accept**: `<button type="submit" class="btn btn-success btn-block">Edit</button>`
- **Close**: Click outside modal area

### Phase-Based Prompts

#### Phase 1 Prompt
- **Button**: `<a class="mb-2" data-bs-toggle="modal" data-bs-target="#editPhase1PromptModal">`
- **Accept**: `<button type="submit" class="btn btn-success btn-block">Edit</button>`
- **Close**: Click outside modal area

#### Phase 2 Prompt
- **Button**: `<a class="mb-2" data-bs-toggle="modal" data-bs-target="#editPhase2PromptModal">`
- **Accept**: `<button type="submit" class="btn btn-success btn-block">Edit</button>`
- **Close**: Click outside modal area

#### Phase 3 Prompt
- **Button**: `<a class="mb-2" data-bs-toggle="modal" data-bs-target="#editPhase3PromptModal">`
- **Accept**: `<button type="submit" class="btn btn-success btn-block">Edit</button>`
- **Close**: Click outside modal area

### Completion Prompts

#### Final Victory Response
- **Button**: `<a class="mb-2" data-bs-toggle="modal" data-bs-target="#editFinalVictoryResponseModal">`
- **Accept**: `<button type="submit" class="btn btn-success btn-block">Edit</button>`
- **Close**: Click outside modal area

#### Ongoing Objective Prevention
- **Button**: `<a class="mb-2" data-bs-toggle="modal" data-bs-target="#editOngoingObjectivePreventionModal">`
- **Accept**: `<button type="submit" class="btn btn-success btn-block">Edit</button>`
- **Close**: Click outside modal area

## Modal Target References

### Quick Modal Mapping
- **#editCharacterModal**: Basic character information
- **#editInstructionsModal**: Persona prompt settings
- **#editFirstStoryModal**: Initial story setup
- **#editFirstMessageModal**: Character's first message
- **#editStoryPromptModal**: Scenario prompt configuration
- **#editStorySuggestionPromptModal**: User context settings
- **#editPhase1PromptModal**: Early interaction behavior
- **#editPhase2PromptModal**: Mid-interaction behavior
- **#editPhase3PromptModal**: Late interaction behavior
- **#editFinalVictoryResponseModal**: Success completion message
- **#editOngoingObjectivePreventionModal**: Failure/redirect handling

## AI Navigation Tips

### Modal Automation Pattern
1. Click button with `data-bs-toggle="modal"`
2. Wait for modal to appear
3. Fill form fields
4. Click submit button with `btn-success` class
5. Click outside modal area to close

### Button Text Variations
- **Turkish**: "Düzenle", "Yükleniyor..."
- **English**: "Edit", "Loading..."
- **Success Class**: Always `btn-success`
- **Warning Class**: Always `btn-warning`

### Reliable Selectors
- Modal triggers: `[data-bs-toggle="modal"]`
- Submit buttons: `[type="submit"]`
- Success buttons: `.btn-success`
- All buttons: `.btn`

---

*Use this reference for precise button targeting in VibeTown dashboard automation.*