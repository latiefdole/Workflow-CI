"""
modelling.py — untuk MLProject (K3 Workflow CI)
Versi yang berjalan di GitHub Actions environment.
"""
import os
import pandas as pd
import mlflow
import mlflow.sklearn
import dagshub
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import cross_val_score

# ── Load Data ─────────────────────────────────────────────────────────────────
PREP = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wine_quality_preprocessing')

X_train = pd.read_csv(f'{PREP}/X_train.csv').values
X_test  = pd.read_csv(f'{PREP}/X_test.csv').values
y_train = pd.read_csv(f'{PREP}/y_train.csv').squeeze().values
y_test  = pd.read_csv(f'{PREP}/y_test.csv').squeeze().values

print(f"Data loaded — Train: {X_train.shape}, Test: {X_test.shape}")

# ── Training ──────────────────────────────────────────────────────────────────
with mlflow.start_run(run_name='RF_CI_run') as run:
    # Save run ID to file for CI
    with open('run_id.txt', 'w') as f:
        f.write(run.info.run_id)

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Extra manual metrics
    mlflow.log_metric('test_accuracy',  accuracy_score(y_test, y_pred))
    mlflow.log_metric('test_f1',        f1_score(y_test, y_pred))
    mlflow.log_metric('test_precision', precision_score(y_test, y_pred))
    mlflow.log_metric('test_recall',    recall_score(y_test, y_pred))
    
    # Log model manually
    mlflow.sklearn.log_model(model, 'model')

    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"F1 Score: {f1_score(y_test, y_pred):.4f}")
    print("✅ Training selesai!")
