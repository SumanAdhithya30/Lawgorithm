# import pandas as pd
# import random

# # Define sample legal case details templates
# case_details_templates = [
#     "The plaintiff alleges breach of contract and seeks damages for non-performance by the defendant.",
#     "The defendant is accused of failing to uphold fiduciary duties, resulting in significant losses for the plaintiff.",
#     "The plaintiff presents evidence of negligence, with the defendant found liable for failing to exercise due care.",
#     "The defendant denies all allegations, claiming the plaintiff failed to fulfill contractual obligations.",
#     "The plaintiff asserts that the defendant committed fraud and misrepresentation, seeking both compensatory and punitive damages.",
#     "The defendant argues that the plaintiff's claims are without merit and that the contract was void due to misrepresentation.",
#     "The plaintiff has submitted multiple pieces of evidence supporting breach of warranty, alleging that the defendant delivered defective products.",
#     "The defendant insists that all terms of the contract were followed, and the plaintiff's claims are an attempt to unjustly enrich themselves."
# ]

# # Define possible winner labels
# winners = ["plaintiff", "defendant"]

# # Generate synthetic dataset
# num_cases = 100  # Number of synthetic cases
# data = []

# for _ in range(num_cases):
#     # Randomly select 1 or 2 sentences to form the case details
#     num_sentences = random.randint(1, 2)
#     case_details = " ".join(random.sample(case_details_templates, k=num_sentences))
#     # Randomly assign a winner
#     winner = random.choice(winners)
#     data.append({"case_details": case_details, "winner": winner})

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Display the first few rows
# print(df.head())

# # Save to CSV
# df.to_csv("synthetic_legal_cases.csv", index=False)
import pandas as pd
import random

# Sample names for synthetic legal parties
party_names = ["John Doe", "Jane Smith", "Acme Corp", "State of Texas", "Alice Brown", "Bob Williams", "XYZ Ltd.", "Global Tech Inc."]

# Sample legal case descriptions
case_descriptions = [
    "A dispute over contract breach.",
    "An intellectual property rights violation.",
    "A criminal case involving fraud charges.",
    "A corporate lawsuit regarding employment policies.",
    "A civil rights case related to discrimination.",
    "A property dispute over land ownership.",
    "A regulatory compliance issue with government authorities."
]

import pandas as pd
import random

# Synthetic case summaries for winnable cases (Indian judiciary context)
winnable_summaries = [
    "The case demonstrates compelling evidence, strong witness testimony, and clear legal precedent, making it highly winnable.",
    "With robust documentation and expert testimonies, the plaintiff's claim is expected to succeed in court.",
    "Substantial evidence and clear contractual obligations support the plaintiff's case, indicating a favorable outcome.",
    "Well-supported legal arguments and significant merits, reinforced by past precedents, suggest the case is winnable.",
    "Strong evidence and effective legal representation ensure a promising outcome in this dispute."
]

# Corresponding keywords for winnable cases
winnable_keywords = [
    "compelling evidence; strong testimony; clear precedent",
    "robust documentation; expert testimony",
    "substantial evidence; contractual obligations; favorable outcome",
    "legal arguments; past precedents; significant merits",
    "strong evidence; effective representation"
]

# Synthetic case summaries for non-winnable cases
non_winnable_summaries = [
    "The case suffers from insufficient evidence, weak witness testimonies, and ambiguous legal arguments, making it unlikely to win.",
    "Lack of robust documentation and unclear contractual obligations hinder the plaintiff’s claim, reducing win probability.",
    "The absence of compelling evidence and presence of strong counterarguments by the defendant diminish the case's merits.",
    "Weak witness statements and the lack of established legal precedent indicate that the case is not winnable.",
    "Ambiguous legal arguments and minimal supporting evidence render the case unconvincing and unlikely to succeed."
]

# Corresponding keywords for non-winnable cases
non_winnable_keywords = [
    "insufficient evidence; weak testimony; ambiguous arguments",
    "lack of documentation; unclear obligations; reduced probability",
    "absence of compelling evidence; strong counterarguments",
    "weak witness statements; lack of precedent",
    "ambiguous arguments; minimal evidence; unconvincing"
]

# Generate synthetic dataset
num_cases = 2000  # Total number of cases to generate
synthetic_data = []

for _ in range(num_cases):
    if random.random() < 0.5:
        # Create a winnable case
        idx = random.randint(0, len(winnable_summaries) - 1)
        summary = winnable_summaries[idx]
        keywords = winnable_keywords[idx]
        label = "Winnable"
    else:
        # Create a non-winnable case
        idx = random.randint(0, len(non_winnable_summaries) - 1)
        summary = non_winnable_summaries[idx]
        keywords = non_winnable_keywords[idx]
        label = "Not Winnable"
    
    synthetic_data.append([summary, keywords, label])

# Create a DataFrame with the synthetic data
columns = ["Case Summary", "Keywords", "Winnable"]
df = pd.DataFrame(synthetic_data, columns=columns)

# Save the dataset to a CSV file
df.to_csv("synthetic_case_winnability.csv", index=False)
print("Synthetic dataset saved as synthetic_case_winnability.csv")
