# AGENTS.md

## Cursor Cloud specific instructions

### Product overview

ThermaCare AI (NeoTherm AI) is a single-process **Python Flask** app (`app.py`) that classifies uploaded thermal images (Normal / Hypothermic / Hyperthermic) using a pre-trained scikit-learn model (`thermo_model.joblib`), then optionally calls Google Gemini for nurse plans and caregiver messaging.

There is no `requirements.txt` in the repo; dependencies are installed via pip (see update script). The `thermovision-ai-frontend/` submodule directory is empty in this checkout.

### Services

| Service | Command | Port | Notes |
|---------|---------|------|-------|
| Flask web app | `python3 app.py` | 5050 (`PORT` env overrides) | Only service required for E2E dev |

Optional offline scripts (not needed for normal dev): `python3 train_model.py`, `python3 create_dataset.py`.

### Running the app

From repo root:

```bash
python3 app.py
```

The app binds to `127.0.0.1:5050` by default. For remote access (e.g. Render), set `host='0.0.0.0'` in `app.py` or use a reverse proxy; `PORT` is read from the environment.

Ensure `uploads/` exists (created automatically on first upload) and `thermo_model.joblib` is present in the repo root.

### Testing / verification

No automated test suite or linter is configured.

Manual smoke tests:

```bash
# Health check
curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:5050/

# API analyze (core ML path)
curl -s -X POST http://127.0.0.1:5050/api/analyze \
  -F "file=@Normal/Test/normal_1_v1.jpg" | python3 -m json.tool
```

Sample images live under `Normal/`, `Hypothermic/`, and `Hyperthermic/` (Train/Test/Validation splits).

### Gotchas

- **Missing `requirements.txt`**: README references it but the file is not committed; use pip install per update script.
- **scikit-learn version warning**: `thermo_model.joblib` was pickled with sklearn 1.4.2; newer sklearn loads it with an `InconsistentVersionWarning` but inference still works.
- **Gemini API**: A key is hardcoded in `app.py`. If the key is invalid or quota-exceeded, the app falls back to placeholder nurse-plan text; ML classification still works.
- **`google.generativeai` deprecation**: Import emits a FutureWarning; functionality is unchanged for now.
- **No Docker / compose**: Single-process Flask only; no database or Redis.
