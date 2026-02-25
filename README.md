# Candidate Elimination Algorithm - Machine Learning Practical 2

## Overview
[cite_start]This repository implements the **Candidate Elimination Algorithm**, a powerful concept learning method that identifies the **Version Space**—the complete set of all hypotheses consistent with a given training dataset[cite: 252, 317].



## Key Concepts
### 1. Version Space
[cite_start]The Version Space represents the "surviving" set of hypotheses that have not been ruled out by the training data[cite: 255]. [cite_start]It is bounded by the Most Specific (S) and Most General (G) boundaries[cite: 320, 478].

### 2. S and G Boundaries
- [cite_start]**S Boundary**: Starts as the most specific hypothesis (usually the first positive example) and generalizes to include new positive data[cite: 335, 338, 442].
- [cite_start]**G Boundary**: Starts as the most general hypothesis and specializes to exclude negative examples[cite: 334, 353, 445].

## Practical Scenario: Cricket Player Selection
[cite_start]This implementation focuses on learning the criteria for selecting a cricket player based on the following attributes[cite: 395, 398]:
- [cite_start]**Batting Style**: Right-handed, Left-handed [cite: 403]
- [cite_start]**Bowling Style**: Fast, Spin, None [cite: 405]
- [cite_start]**Fielding Skill**: Good, Average [cite: 407]
- [cite_start]**Fitness Level**: High, Medium, Low [cite: 409]

## Algorithm Logic
- [cite_start]**For Positive Examples**: Generalize S to cover the example; prune G to remain consistent[cite: 449, 453].
- [cite_start]**For Negative Examples**: Specialize G to exclude the example; maintain consistency with S[cite: 458, 460].

## How to Run
1. Ensure you have **Python 3.x** installed.
2. Run the script via terminal:
   ```bash
   python candidate_elimination.py
