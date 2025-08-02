def build_prompt(topic: str, tone: str, platform: str) -> str:
    style_instruction = {
        "Instagram": "Use emojis and a catchy tone. Add a strong hook and keep it visually appealing.",
        "Twitter": "Be witty and concise. Emojis are okay if they enhance impact.",
        "LinkedIn": "Use emojis sparingly and only if relevant. Keep it professional but engaging and informative .",
    }.get(platform, "Use emojis if appropriate for the tone and platform.")

    return f"""
You are a professional social media content writer.

Generate a single catchy **caption** for a post.

Context:
- Platform: {platform}
- Tone: {tone}
- Topic or Theme: {topic}

Instructions:
- {style_instruction}
- Add 5-7 relevant **hashtags** at the end based on the theme.
- Include **emojis** naturally based on platform and tone.
- Do NOT include explanations, titles, or formatting.

Output:
"""
