# Features: [Batting Style, Bowling Style, Fielding Skill, Fitness Level]
# Defined globally so the function can find it
cricket_data = [
    ['Right-handed', 'Fast', 'Good', 'High', 'Yes'],   # Ex 1: Positive
    ['Left-handed', 'Spin', 'Good', 'Medium', 'Yes'], # Ex 2: Positive
    ['Right-handed', 'None', 'Average', 'Low', 'No'], # Ex 3: Negative
    ['Right-handed', 'Spin', 'Good', 'High', 'Yes']   # Ex 4: Positive
]

def candidate_elimination(data):
    # Initialize S with first positive example [cite: 335, 442]
    s = data[0][:-1].copy()
    # Initialize G with most general wildcards [cite: 334, 446]
    g = [["?" for _ in range(len(s))]]

    print(f"Initial S: {s}")
    print(f"Initial G: {g}\n")

    for i, row in enumerate(data):
        features, target = row[:-1], row[-1]

        if target == "Yes":
            # 1. Update Specific Boundary (Generalize S) [cite: 344, 453]
            for x in range(len(s)):
                if features[x] != s[x]:
                    s[x] = "?"
            
            # 2. Remove hypotheses from G inconsistent with positive example [cite: 381]
            g = [h for h in g if all(h[j] == "?" or h[j] == features[j] for j in range(len(s)))]
            print(f"Ex {i+1} [POS]: S={s}, G={g}")

        else:
            # 3. Update General Boundary (Specialize G) [cite: 352, 460]
            new_g = []
            for h in g:
                if all(h[j] == "?" or h[j] == features[j] for j in range(len(s))):
                    for j in range(len(s)):
                        # Specialize G to exclude the negative attribute [cite: 354, 466]
                        if h[j] == "?" and features[j] != s[j]:
                            temp_g = h.copy()
                            temp_g[j] = s[j]
                            if temp_g not in new_g:
                                new_g.append(temp_g)
                else:
                    new_g.append(h)
            g = new_g
            print(f"Ex {i+1} [NEG]: S={s}, G={g}")

    return s, g

if __name__ == "__main__":
    final_s, final_g = candidate_elimination(cricket_data)
    print(f"\n" + "="*30)
    print("FINAL VERSION SPACE")
    print("="*30)
    print(f"S (Specific Boundary): {final_s}")
    print(f"G (General Boundary): {final_g}")