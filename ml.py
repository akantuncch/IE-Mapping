import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx

from source_data.prog import nodes as programs
from source_data.tech import tech_data as technologys

# Initialize the TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()

print("Number of programs:", len(programs))

for program in programs:
    print(program["name"])

# Combine relevant text fields for each program
for program in programs:
    # Check if the key 'description' exists in the dictionary
    if "description" in program:
        # Combine the description with other relevant fields
        program["combined_description"] = program["description"]
    else:
        # Handle the case where 'description' is not a key in the dictionary
        print(f"Key 'description' not found in program: {program}")
        program["combined_description"] = ""  # Setting a default value

for technology in technologys:
    # Check if the required keys exist in the dictionary
    if "short_description" in technology and "long_description" in technology:
        # Combine the short and long descriptions
        technology["combined_description"] = (
            technology["short_description"] + " " + technology["long_description"]
        )
    else:
        # Handle the case where one or both descriptions are not available
        print(
            f"Missing 'short_description' or 'long_description' in technology: {technology}"
        )
        technology[
            "combined_description"
        ] = ""  # Setting a default value or alternative handling


# Combine all descriptions
all_descriptions = [tech["combined_description"] for tech in technologys] + [
    prog["combined_description"] for prog in programs
]

# Initialize and fit the TF-IDF vectorizer on the combined descriptions
tfidf_vectorizer = TfidfVectorizer()
tfidf_vectorizer.fit(all_descriptions)

# Transform the descriptions of technologies
tech_tfidf_matrix = tfidf_vectorizer.transform(
    [tech["combined_description"] for tech in technologys]
)

# Transform the descriptions of programs
program_tfidf_matrix = tfidf_vectorizer.transform(
    [prog["combined_description"] for prog in programs]
)

# Print out a few TF-IDF vectors to check their diversity
print(tech_tfidf_matrix[0].toarray())  # First technology
print(program_tfidf_matrix[0].toarray())  # First program

print("Shape of program TF-IDF matrix:", program_tfidf_matrix.shape)


def score_match(technology, program, tech_tfidf, prog_tfidf):
    print(
        f"Evaluating match for Technology: '{technology['name']}' and Program: '{program['name']}'"
    )

    # 1. Description Similarity - Scale it up for more impact
    description_similarity = cosine_similarity(tech_tfidf, prog_tfidf)[0][0]
    similarity_score = description_similarity * 10  # Scale up the similarity score
    print(f"  Description similarity score: {similarity_score}")

    # 2. Technology Type Alignment
    tech_type_match = technology["techtype"] == program["techtype"]
    type_match_score = 5 if tech_type_match else 0  # Assign a higher score for a match
    print(f"  Technology type match score: {type_match_score}")

    # 3. Resource Alignment
    technology_needs = set(technology.get("resource_needs", []))
    program_offers = set(program.get("resources_offered", []))
    matching_resources = technology_needs.intersection(program_offers)
    resource_match_score = (
        len(matching_resources) * 2
    )  # Assign a score for each matching resource
    print(f"  Resource alignment score: {resource_match_score}")

    # Total score calculation
    total_score = similarity_score + type_match_score + resource_match_score
    print(f"  Total match score: {total_score}\n")

    return total_score


# Store the match scores in a list
match_scores = []

for tech_index, technology in enumerate(technologys):
    for prog_index, program in enumerate(programs):
        # Compute TF-IDF vectors for current technology and program
        tech_tfidf = tech_tfidf_matrix[tech_index]
        prog_tfidf = program_tfidf_matrix[prog_index]

        # Compute the match score
        score = cosine_similarity(tech_tfidf, prog_tfidf)

        # Flatten the score array and get the first element
        score_value = score.flatten()[0]

        # Add the score and the corresponding tech-program pair to the list
        match_scores.append((score_value, technology["name"], program["name"]))

# Sorting the match scores in descending order to see the best matches first
match_scores.sort(reverse=True, key=lambda x: x[0])

# Optionally, print or process the top matches
for score, tech_name, prog_name in match_scores[:20]:  # Adjust the number as needed
    print(f"Match Score: {score}, Technology: {tech_name}, Program: {prog_name}")
