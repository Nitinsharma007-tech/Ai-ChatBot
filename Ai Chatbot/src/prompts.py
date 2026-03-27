def apply_mode(text, mode):

    if mode == "Student":
        return f"""
Explain this in a structured way:

1. Simple explanation
2. Key points
3. Short notes
4. Important questions

Text:
{text}
"""

    elif mode == "Business":
        return f"""
Analyze this from a business perspective:

1. Summary
2. Key insights
3. Market impact
4. Opportunities

Text:
{text}
"""

    return text