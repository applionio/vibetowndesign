import yaml
import os
import datetime

# --- CONFIGURATION ---
# Get the absolute path of the directory containing this script to build robust paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))

DRAFT_TEMPLATE_PATH = os.path.join(PROJECT_ROOT, 'templates/game-design/Write Level Doc.yml')
REFINE_TEMPLATE_PATH = os.path.join(PROJECT_ROOT, 'templates/game-design/refine-level-prompt.yml')
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'outputs')

# --- PLACEHOLDER FOR AI CALLS ---
# In a real scenario, you would replace these with your actual API calls to an AI model.

def call_ai_for_draft(prompt, character, location):
    """Simulates calling an AI to get the first draft of a level."""
    print("\n🤖 AI is generating the first draft...")
    # The prompt is now a fully formatted YAML string with user input already included.
    # No more string replacement is needed here.
    # In a real scenario, you would pass the 'prompt' variable directly to the AI.

    # Simulated AI response
    simulated_draft = f"""Hey newcomer! 👋
Everyone's been buzzing about you joining us in {location}!
I'm {character} and I just HAD to say hi first! ✨
I've heard you're pretty cool. What's your vibe today?
"""
    print("✅ Draft generated.")
    return simulated_draft

def call_ai_for_refinement(prompt, draft_context):
    """Simulates calling an AI to refine the draft."""
    print("\n🤖 AI is refining the draft to be more 'TikTok-worthy'...")
    # In a real call, you'd insert the draft_context into the refinement prompt.
    # For this simulation, we'll just create a more stylized version.
    
    simulated_refinement = f"""Yo, you made it! The one and only. 😎

Word on the street is you're the new face in town. I'm {draft_context.split("I'm ")[1].split(' ')[0][:-1]}. Had to see the legend for myself.

Heard you've got skills. Don't be shy, show me what you got.

**SURPRISE TWIST:** Suddenly, the lights flicker and a mysterious note slides under the door.
"""
    print("✅ Draft refined.")
    return simulated_refinement

# --- MAIN WORKFLOW ---
def main():
    """Main function to run the automated level generation workflow."""
    print("🚀 Starting Level Generation Workflow...")

    # 1. Load the prompt templates
    try:
        with open(DRAFT_TEMPLATE_PATH, 'r') as f:
            draft_data = yaml.safe_load(f)
            # The entire YAML structure will be our prompt context

        with open(REFINE_TEMPLATE_PATH, 'r') as f:
            refine_data = yaml.safe_load(f)
            refine_prompt = refine_data['refinement_prompt']['task']
    except FileNotFoundError as e:
        print(f"❌ Error: Could not find a template file. {e}")
        return
    except yaml.YAMLError as e:
        print(f"❌ Error: Could not parse a YAML template file. {e}")
        return

    # 2. Get user input
    print("\n📝 Please provide initial details for the level:")
    character_name = input("Enter the character's name: ")
    location_name = input("Enter the level's location: ")

    # 3. Step 1: Generate the draft
    # Modify the loaded data with user input
    draft_data['game_level']['game_settings']['character'] = character_name
    draft_data['game_level']['game_settings']['location_name'] = location_name

    # Convert the modified dictionary back into a string for the AI
    draft_prompt_string = yaml.dump(draft_data)

    draft_output = call_ai_for_draft(draft_prompt_string, character_name, location_name)

    # 4. Step 2: Refine the draft
    final_output = call_ai_for_refinement(refine_prompt, draft_output)

    # 5. Save the final output
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"\n📁 Created output directory: '{OUTPUT_DIR}'")

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"{character_name.replace(' ', '_').lower()}_level_{timestamp}.txt"
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    with open(output_path, 'w') as f:
        f.write("--- DRAFT ---\n")
        f.write(draft_output)
        f.write("\n\n--- FINAL REFINED VERSION ---\n")
        f.write(final_output)

    print(f"\n✨ Success! Final level document saved to: {output_path}")

if __name__ == "__main__":
    main()
