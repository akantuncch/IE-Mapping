class Technology:
    def __init__(self, name, fields, requirements, progress_metrics):
        self.name = name
        self.fields = set(fields)  # A set of fields the technology falls under
        self.requirements = requirements
        self.progress_metrics = progress_metrics


class Program:
    def __init__(self, name, fields, expertise, resources, eligibility_criteria):
        self.name = name
        self.fields = set(fields)  # A set of fields the program supports
        self.expertise = expertise
        self.resources = resources
        self.eligibility_criteria = eligibility_criteria


def calculate_match_score(technology, program):
    field_match_score = len(technology.fields.intersection(program.fields))
    # Additional logic can be added here for other criteria
    return field_match_score


def recommend_programs(technology, programs):
    recommendations = []
    for program in programs:
        match_score = calculate_match_score(technology, program)
        if match_score > 0:  # Adjust threshold as needed
            recommendations.append((program, match_score))
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations


def evaluate_matches(technology, recommendations):
    if recommendations:
        best_match = recommendations[0]
        print(
            f"Best match for {technology.name} is {best_match[0].name} with a score of {best_match[1]}"
        )
    else:
        print(f"No suitable match found for {technology.name}")


# Example Data
def evaluate_matches(technology, recommendations):
    if recommendations:
        best_match = recommendations[0]
        print(
            f"Best match for {technology.name} is {best_match[0].name} with a score of {best_match[1]}"
        )
    else:
        print(f"No suitable match found for {technology.name}")


# Example Data
tech1 = Technology(
    "Pelvic Floor Physical Therapy Smart Wand", ["medtech", "healthtech"], {}, {}
)
tech2 = Technology("ENVIROSCAN", ["tech", "software"], {}, {})
tech3 = Technology(
    "STING-IL-35 Axis Targeting Treatment for Cold Tumors",
    ["therapeutics", "oncology"],
    {},
    {},
)

prog1 = Program("Innovate Carolina", ["general"], {}, {}, {})
prog2 = Program("FastTraCS", ["medtech", "design"], {}, {}, {})
prog3 = Program(
    "The Eshelman Institute", ["therapeutics", "digital health"], {}, {}, {}
)
prog3 = Program("Venture Catalyst Program", ["general"], {}, {}, {})
prog4 = Program("Center for the Business of Health", ["general"], {}, {}, {})
prog5 = Program(
    "KickStart Venture Services",
    ["medtech", "biotech", "therapeutics", "tech", "software"],
    {},
    {},
    {},
)


# Using the Prototype
recommendations = recommend_programs(tech1, [prog1])
evaluate_matches(tech1, recommendations)
