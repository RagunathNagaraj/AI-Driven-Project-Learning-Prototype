"""
AI-Driven Project Learning Prototype
------------------------------------
Project Recommendation Module

This script demonstrates how AI can recommend project topics
to students based on their interests and skills.
"""

import json
import random

# Load learner and project data
with open("../data/sample_learners.json", "r") as f:
    learners = json.load(f)

with open("../data/sample_projects.json", "r") as f:
    projects = json.load(f)

def recommend_projects(learner, top_n=2):
    """Recommend projects based on shared interests or required skills."""
    scored = []
    for p in projects:
        interest_overlap = len(set(learner["interests"]).intersection([p["category"]]))
        skill_overlap = len(set(learner["skills"]).intersection(p["required_skills"]))
        score = interest_overlap + skill_overlap
        scored.append((p["title"], score))
    ranked = sorted(scored, key=lambda x: x[1], reverse=True)
    return [p[0] for p in ranked[:top_n]]

print("\n=== AI-Based Project Recommendations ===")
for learner in learners:
    recs = recommend_projects(learner)
    print(f"\n{learner['name']} → Suggested Projects:")
    for r in recs:
        print(f"  - {r}")
