"""
AI-Driven Project Learning Prototype
------------------------------------
Peer Matching Module

This script demonstrates how an AI-based system can form student groups
based on shared interests and complementary skills. The data used is synthetic
and stored in /data/sample_learners.json.
"""

import json
from itertools import combinations

# Load synthetic learner data
with open("../data/sample_learners.json", "r") as f:
    learners = json.load(f)

def interest_similarity(a, b):
    """Calculate overlap in interests."""
    common = len(set(a["interests"]).intersection(b["interests"]))
    total = len(set(a["interests"]).union(b["interests"]))
    return common / total if total > 0 else 0

def skill_diversity(a, b):
    """Measure complementarity of skills (more diverse = higher)."""
    overlap = len(set(a["skills"]).intersection(b["skills"]))
    total = len(set(a["skills"]).union(b["skills"]))
    return 1 - (overlap / total) if total > 0 else 0

def match_score(a, b, w_interest=0.6, w_skill=0.4):
    """Combine interest and skill diversity into a weighted score."""
    return w_interest * interest_similarity(a, b) + w_skill * skill_diversity(a, b)

# Generate pairwise matching scores
matches = []
for a, b in combinations(learners, 2):
    score = round(match_score(a, b), 2)
    matches.append({
        "pair": (a["name"], b["name"]),
        "score": score
    })

# Sort pairs by descending score
matches.sort(key=lambda x: x["score"], reverse=True)

# Print top potential matches
print("\n=== Top Peer Match Recommendations ===")
for m in matches:
    print(f"{m['pair'][0]} ↔ {m['pair'][1]}  |  Match Score: {m['score']}")

