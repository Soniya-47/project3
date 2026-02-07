
import os

def combine_markdown(source_dir, output_filename):
    chapters = [
        "01_executive_summary.md",
        "02_ai_security.md",
        "03_post_quantum.md",
        "04_space_security.md",
        "05_biotech_cognitive.md",
        "06_top_50_jobs.md",
        "07_roadmap_appendices.md"
    ]

    full_md_text = "# Cybersecurity Deep Research Report: Opportunities in New Domains (2025-2035)\n\n"
    
    for chapter in chapters:
        file_path = os.path.join(source_dir, chapter)
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                full_md_text += f.read() + "\n\n---\n\n"

    with open(output_filename, "w") as f:
        f.write(full_md_text)
    
    print(f"Combined markdown report generated: {output_filename}")

if __name__ == "__main__":
    combine_markdown("report_content", "Cybersecurity_Report_2025_2035.md")
