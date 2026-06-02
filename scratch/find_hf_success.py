import json

transcript_path = r"C:\Users\jeswin\.gemini\antigravity\brain\11dd433c-1156-488f-94fb-2e21b89b60ba\.system_generated\logs\transcript.jsonl"

print("Searching for Hugging Face success in transcript...")

with open(transcript_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        try:
            data = json.loads(line)
            content = data.get("content", "")
            if "[SUCCESS] Hugging Face API is working!" in content or "Hugging Face API is working!" in content:
                print(f"Line {i}, Step {data.get('step_index')}: {content[:300]}")
            # check system messages or other MODEL content
            for tc in data.get("tool_calls", []):
                pass
            # check results or outputs in transcript
            # Wait, let's search if the user ran python scratch/test_apis.py
            if "test_apis.py" in content or "test_apis.py" in str(data):
                print(f"Line {i}, Step {data.get('step_index')}: Found test_apis.py reference")
        except Exception as e:
            pass
