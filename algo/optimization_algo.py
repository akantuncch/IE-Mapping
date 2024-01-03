import pulp

from source_data.tech import tech_data
from source_data.prog import nodes as program_data

# Create a linear programming problem
problem = pulp.LpProblem("Minimize_Development_Time", pulp.LpMinimize)

# Example placeholder data for technologies
techs = ["T1", "T2", "T3"]
programs = ["1", "2", "3", "4", "5", "6", "7"]

""" tech_data = {
    "T1": {
        "resource_needs": {
            "Research and Development Support": [
                "Patent and Market Research",
                "Research Grants",
            ],
            "Technology and Infrastructure": ["Design Services"],
            "Mentorship and Support": ["Commercialization and Startup Support"],
        },
        "readiness_level": "Prototype",
        "expertise_required": "Biotech",
    },
    "T2": {
        "resource_needs": "Lab Space",
        "readiness_level": "Concept",
        "expertise_required": "AI",
    },
    "T3": {
        "resource_needs": "Mentorship",
        "readiness_level": "Market Ready",
        "expertise_required": "Medtech",
    },
}

# Example placeholder data for programs
program_data = {
    "P1": {
        "resources_offered": "Funding",
        "efficiency": 0.8,
        "expertise_available": "Biotech",
    },
    "P2": {
        "resources_offered": "Mentorship",
        "efficiency": 0.7,
        "expertise_available": "Digital Health",
    },
    "P3": {
        "resources_offered": "Lab Space",
        "efficiency": 0.6,
        "expertise_available": "Renewable Energy",
    },
} """

data = {"tech_data": tech_data, "program_data": program_data}


""" def calculate_resource_alignment(tech, program, data):
    # Basic logic: 1 if needs and offerings match, else 0
    return (
        1
        if data["tech_data"][tech]["resource_needs"]
        == data["program_data"][program]["resources_offered"]
        else 0
    ) """


def calculate_resource_alignment(tech_id, program_id, data):
    # Find the technology dictionary by tech_id
    tech_dict = next(
        (item for item in data["tech_data"] if item["id"] == tech_id), None
    )
    # Find the program dictionary by program_id
    program_dict = next(
        (item for item in data["program_data"] if item["id"] == program_id), None
    )

    if not tech_dict or not program_dict:
        return 0  # Return 0 if tech or program not found

    # Check if any resource need matches any resource offered
    for need in tech_dict["resource_needs"]:
        if any(
            offer in program_dict["resources_offered"]
            for offer in tech_dict["resource_needs"][need]
        ):
            return 1

    return 0


def calculate_program_efficiency(program_id, data):
    # Find the program dictionary by program_id
    program_dict = next(
        (item for item in data["program_data"] if item["id"] == program_id), None
    )

    if not program_dict:
        return 0  # Return 0 if program not found

    return program_dict.get("efficiency", 0)  # Default to 0 if efficiency not found


def calculate_tech_readiness(tech_id, data):
    # Find the technology dictionary by tech_id
    tech_dict = next(
        (item for item in data["tech_data"] if item["id"] == tech_id), None
    )

    if not tech_dict:
        return 0  # Return 0 if tech not found

    # Define the readiness levels
    readiness_levels = {
        "Prototype": 0.6,
        "Concept": 0.4,
        "Market Ready": 1.0,
        "Research": 0.5,
        "Development": 0.7,
    }

    return readiness_levels.get(
        tech_dict.get("readiness_level"), 0
    )  # Default to 0 if readiness level not found


def calculate_expertise_match(tech_id, program_id, data):
    # Find the technology and program dictionaries by their respective ids
    tech_dict = next(
        (item for item in data["tech_data"] if item["id"] == tech_id), None
    )
    program_dict = next(
        (item for item in data["program_data"] if item["id"] == program_id), None
    )

    if not tech_dict or not program_dict:
        return 0  # Return 0 if either tech or program not found

    # Check if the expertise required by the tech matches any expertise available in the program
    tech_expertise = tech_dict.get("expertise_required", [])
    program_expertise = program_dict.get("expertise_available", [])

    return 1 if any(exp in program_expertise for exp in tech_expertise) else 0


def dynamic_development_time_score(tech, program, data):
    # Example weights - these may need to be adjusted
    weights = {
        "resource_alignment": 0.4,
        "program_efficiency": 0.3,
        "tech_readiness": 0.2,
        "expertise_match": 0.1,
    }

    # Calculate each component of the score
    resource_score = calculate_resource_alignment(tech, program, data)
    efficiency_score = calculate_program_efficiency(program, data)
    readiness_score = calculate_tech_readiness(tech, data)
    expertise_score = calculate_expertise_match(tech, program, data)

    # Combine scores into a final development time score
    total_score = (
        resource_score * weights["resource_alignment"]
        + efficiency_score * weights["program_efficiency"]
        + readiness_score * weights["tech_readiness"]
        + expertise_score * weights["expertise_match"]
    )

    return total_score


# Decision variables: 1 if tech is assigned to program, 0 otherwise
choices = pulp.LpVariable.dicts("Choice", (techs, programs), 0, 1, pulp.LpBinary)


# Update the objective function in your model to pass this data
problem += pulp.lpSum(
    [
        choices[t][p] * dynamic_development_time_score(t, p, data)
        for t in techs
        for p in programs
    ]
)

for t in techs:
    problem += pulp.lpSum([choices[t][p] for p in programs]) == 1

for p in programs:
    problem += pulp.lpSum([choices[t][p] for t in techs]) <= 2

problem.solve()

for t in techs:
    for p in programs:
        if pulp.value(choices[t][p]) == 1:
            print(f"Technology {t} is assigned to Program {p}")

# Output results with detailed explanation
for t in techs:
    for p in programs:
        if pulp.value(choices[t][p]) == 1:
            # Calculate scores for the matched pair
            resource_score = calculate_resource_alignment(t, p, data)
            efficiency_score = calculate_program_efficiency(p, data)
            readiness_score = calculate_tech_readiness(t, data)
            expertise_score = calculate_expertise_match(t, p, data)

            # Print the assignment with explanations
            print(f"Technology {t} is assigned to Program {p}")
            print(f"  Reasoning for this match:")
            print(f"    - Resource Alignment Score: {resource_score}")
            print(f"    - Program Efficiency Score: {efficiency_score}")
            print(f"    - Technology Readiness Score: {readiness_score}")
            print(f"    - Expertise Match Score: {expertise_score}")
            print(
                f"    - Total Score: {resource_score + efficiency_score + readiness_score + expertise_score}"
            )
            print("----------------------------------------------------")
