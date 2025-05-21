import random

themes = {
    "fix": [
        "Squashed the bugs like ancient wrath,",
        "Healed the code with careful breath,",
        "Corrected paths where chaos trod,"
    ],
    "feature": [
        "Brought forth a light the code now owns,",
        "From bits I carved a newborn stone,",
        "A gift of functions, fresh and bright,"
    ],
    "refactor": [
        "With mercy, I have cleaned the past,",
        "Old logic now refines its cast,",
        "Lines reshaped, yet soul the same,"
    ],
    "docs": [
        "Wrote the tales this system sings,",
        "Inscribed the wisdom in the code,",
        "Where silence stood, now knowledge grows,"
    ]
}

closings = [
    "Let this commit endure the test.",
    "And now I rest, my task complete.",
    "Until next change, the code shall sleep."
]

def generate_poem(theme):
    if theme not in themes:
        print("Unknown theme. Choose from: fix, feature, refactor, docs")
        return
    intro = random.choice(themes[theme])
    outro = random.choice(closings)
    return f"{intro}\n{outro}"

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python poet.py [fix|feature|refactor|docs]")
    else:
        print(generate_poem(sys.argv[1]))
