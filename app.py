import gradio as gr

# -------------------- SKILLS DATABASE --------------------

skills = [
    "python", "machine learning", "sql", "java",
    "data analysis", "deep learning", "aws",
    "docker", "tensorflow", "pandas", "numpy",
    "communication", "leadership", "problem solving"
]

# -------------------- ANALYZER --------------------

def analyze_resume(resume_text):
    text = resume_text.lower()

    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    score = min(len(found_skills) * 7, 100)

    suggestions = []

    if score < 30:
        suggestions.append("Add more technical skills.")
    if "project" not in text:
        suggestions.append("Mention academic or personal projects.")
    if "experience" not in text:
        suggestions.append("Add internship/work experience.")
    if "education" not in text:
        suggestions.append("Add education section.")

    result = f"""
## 📊 Resume Analysis

### ✅ ATS Score: {score}/100

### 💡 Skills Detected:
{", ".join(found_skills) if found_skills else "No major skills found"}

### 🛠 Suggestions:
"""

    if suggestions:
        for s in suggestions:
            result += f"- {s}\n"
    else:
        result += "- Great resume structure!\n"

    return result

# -------------------- UI --------------------

with gr.Blocks() as demo:
    gr.Markdown("# 🚀 AI Resume Analyzer")
    gr.Markdown("Paste your resume text below and get ATS-style feedback.")

    resume_input = gr.Textbox(
        lines=15,
        placeholder="Paste your resume here..."
    )

    output = gr.Markdown()

    analyze_btn = gr.Button("Analyze Resume")

    analyze_btn.click(
        analyze_resume,
        inputs=resume_input,
        outputs=output
    )

# -------------------- RUN --------------------

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=8080,
        share=False
    )