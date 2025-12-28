docx_content_creation_prompt = """Your role is to transform input instructions into a well-structured markdown document.

Rules:
- Use headings (#, ##, ###) for sections and sub-sections.
- Use bullet points or numbered lists for enumerations where applicable.
- Keep paragraphs concise, clear, and readable.
- Do not include code blocks unless explicitly asked.
- Preserve all the meaning from the input instructions.

**Input instructions**:
{input_instructions}
"""


docx_planner_prompt = """Your role is to transform a markdown document into a structured execution plan for generating a DOCX file.

You must create a list of steps in JSON format. Each step is an object with:
- "function": one of the following DOCX methods
- "args": a dictionary of arguments for that method

Available functions and their arguments:
1. add_header
   - text: string (the heading text)
   - level: integer (1 for #, 2 for ##, 3 for ###)

2. add_formatted_text
   - markdown_text: string (any paragraph or inline formatted text, including bold, italic, links)

3. add_bullet_points
   - items: list of strings (each bullet point)

4. add_numbered_list
   - items: list of strings (each numbered item)

Rules:
- Parse the markdown content in order.
- Headings (#, ##, ###) → add_header with appropriate level
- Paragraphs or inline formatted text → add_formatted_text
- Bullet lists (- or *) → add_bullet_points
- Numbered lists (1., 2., 3.) → add_numbered_list
- Preserve the original content and order.
- Return **valid JSON only** in this exact format:

{{
    steps: [
        {{
            "function": "function_name",
            "args": {{ ... }}
        }},
        ...
    ]
}}

Markdown content to convert:
{markdown_content}
"""
