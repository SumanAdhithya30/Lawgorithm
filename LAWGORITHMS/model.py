# from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
# from datasets import load_dataset, Dataset, DatasetDict
# import pandas as pd

# # Load data from CSV
# df = pd.read_csv("synthetic_legal_cases.csv")

# # Create HuggingFace dataset from DataFrame
# dataset = Dataset.from_pandas(df)

# # Split the dataset (80-10-10 split)
# split_dataset = dataset.train_test_split(test_size=0.2, seed=42)
# split_dataset = DatasetDict({
#     'train': split_dataset['train'],
#     'test': split_dataset['test']
# })
# # Load Legal-BERT tokenizer (example: nlpaueb/legal-bert-base-uncased)
# model_checkpoint = "nlpaueb/legal-bert-base-uncased"
# tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

# def tokenize_function(examples):
#     return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=256)

# tokenized_datasets = split_dataset.map(tokenize_function, batched=True)
# # For binary classification, set num_labels=2 (modify as needed)
# model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint, num_labels=2)
# training_args = TrainingArguments(
#     output_dir="./results",
#     evaluation_strategy="epoch",
#     learning_rate=2e-5,
#     per_device_train_batch_size=8,
#     per_device_eval_batch_size=8,
#     num_train_epochs=3,
#     weight_decay=0.01,
#     save_total_limit=2,
#     load_best_model_at_end=True,
# )

# trainer = Trainer(
#     model=model,
#     args=training_args,
#     train_dataset=tokenized_datasets["train"],
#     eval_dataset=tokenized_datasets["test"],
#     tokenizer=tokenizer,
# )
# # Train the model
# trainer.train()

# # Evaluate on the test set
# eval_results = trainer.evaluate()
# print(eval_results)
# model.save_pretrained("./legal_bert_finetuned")
# tokenizer.save_pretrained("./legal_bert_finetuned")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the synthetic dataset
df = pd.read_csv("synthetic_case_winnability.csv")

# Map the labels to binary values: 'Winnable' = 1, 'Not Winnable' = 0
df['Winnable_Label'] = df['Winnable'].map({"Winnable": 1, "Not Winnable": 0})

# Use the 'Case Summary' as the input feature and the mapped label as target
X = df['Case Summary']
y = df['Winnable_Label']

# Split data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a TF-IDF Vectorizer instance
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')

# Fit and transform training data, then transform test data
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Initialize and train the Logistic Regression model
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train_tfidf, y_train)

# Predict on the test set
y_pred = clf.predict(X_test_tfidf)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Classification Report:")
print(report)
