
## def categorize_opportunity(opportunity):
#     tags = []
#     text = str(opportunity).lower()
#     if "women" in text:
#         tags.append("Women")
#     if "startup" in text:
#         tags.append("Startup")
#     if "student" in text:
#         tags.append("Student")
#     if "research" in text:
#         tags.append("Research")
#     opportunity["tags"] = tags
#     return opportunity

# def categorize(title: str) -> str:
#     if "Scholarship" in title:
#         return "Scholarship"
#     elif "Grant" in title:
#         return "Grant"
#     elif "Competition" in title:
#         return "Competition"
#     elif "Fellowship" in title:
#         return "Fellowship"
#     else:
#         return "Other"

def categorize(title: str) -> str:
    title_lower = title.lower()   # case-insensitive matching

    if "scholarship" in title_lower:
        return "Scholarship"
    elif "grant" in title_lower:
        return "Grant"
    elif "competition" in title_lower:
        return "Competition"
    elif "fellowship" in title_lower:
        return "Fellowship"
    elif "internship" in title_lower:
        return "Internship"
    elif "workshop" in title_lower:
        return "Workshop"
    elif "conference" in title_lower:
        return "Conference"
    elif "award" in title_lower:
        return "Award"
    else:
        return "Other"
