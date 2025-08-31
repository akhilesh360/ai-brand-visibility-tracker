# pipeline/actions_briefs.py

BRIEF_TMPL = """\
Brand: {brand}
Gap: {topic} on {platform} (AVS {avs:.2f}{vs_text})

Target user intent: {intent}
Working title: {title}

H2 Outline:
- What is {topic_label} and when to seek help
- Evidence-based options (CBT, teletherapy, medication management)
- Insurance & affordability
- How {brand} supports {topic_label}
- FAQs

Facts & citations to include:
- NIMH overview on {topic_label}
- APA guidance and treatment modalities
- Crisis resources: 988 Lifeline / SAMHSA

Required schema/metadata:
- MedicalWebPage + FAQPage
- Author credentials (licensed clinician), last reviewed date
- Clear HIPAA/privacy statement

Internal actions:
- Create/update landing page on {topic} with above outline
- Link from related blog and care pages
- Add structured data & canonical, ensure indexability

Measurement plan:
- Track AVS for prompts tagged {topic}
- Target: +0.08 AVS and +20% owned citation share within 4 weeks
"""

def generate_brief(row: dict, intent: str = "informational"):
    """
    row should contain at least: brand, platform, AVS, topic
    optional: competitor_avg
    """
    topic_label = row.get("topic", "topic").replace("_", " ")
    title = f"Evidence-based help for {topic_label}: options, costs, and how to start"
    comp_avg = row.get("competitor_avg")
    vs_text = "" if comp_avg is None else f" vs competitor avg {comp_avg:.2f}"
    return BRIEF_TMPL.format(
        brand=row["brand"],
        topic=row["topic"],
        platform=row["platform"],
        avs=row["AVS"],
        vs_text=vs_text,
        intent=intent,
        title=title,
        topic_label=topic_label,
    )
