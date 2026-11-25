# Link Archiving Service API

A fast and lightweight REST API built with **FastAPI** and **Playwright** that archives web pages by capturing full-page snapshots (screenshots), saving them locally, and storing their metadata in a database.

---

## Features

- **Automated Web Snapshots**: Uses Playwright headless browser to load and capture screenshots of submitted URLs.
- **Local Storage**: Stores snapshot image files locally on disk.
- **Metadata Persistence**: Saves snapshot records (`id`, `original_url`, `file_path`, and `timestamp`) in the database.
- **Retrieval Endpoints**:
  - List all archived snapshots.
  - Retrieve detailed metadata for a specific snapshot by ID.
  - View or download the captured screenshot image.
- **Interactive Documentation**: Auto-generated Swagger UI and ReDoc documentation out of the box.

---

## 🛠 Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Browser Automation**: [Playwright](https://playwright.dev/python/)
- **Server**: [Uvicorn](https://www.uvicorn.org/)
- **Package & Project Management**: [uv](https://docs.astral.sh/uv/) / standard Python tooling
- **Testing & Quality**: [Pytest](https://docs.pytest.org/), [Ruff](https://docs.astral.sh/ruff/)

---

## 📁 Project Structure

```text
Link-archiving-service-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entrypoint & middleware
│   ├── database.py          # Database connection and session management
│   ├── dependencies.py      # Dependency injection (e.g., db sessions)
│   ├── models.py            # Database models (ORM)
│   ├── schemas.py           # Pydantic schemas (Request / Response validation)
│   ├── services.py          # Playwright snapshot capturing & file saving logic
│   └── routers/
│       ├── __init__.py
│       └── snapshot.py      # Snapshot API endpoints
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Pytest fixtures and test client setup
│   └── test_snapshot.py     # Endpoint and service unit/integration tests
├── pyproject.toml           # Project dependencies and tool configurations
├── uv.lock                  # Pinned dependencies
└── README.md
```

---

## 📋 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/snapshots/` | Submit a URL, capture and save a snapshot, and record metadata |
| `GET` | `/snapshots/` | List all archived snapshot records |
| `GET` | `/snapshots/{id}` | Get metadata for a specific snapshot by ID |
| `GET` | `/snapshots/{id}/image` | View/download the local screenshot file for a snapshot |

### Example Payloads

#### 1. Create a Snapshot (`POST /snapshots/`)

**Request Body:**
```json
{
  "url": "https://example.com"
}
```

**Response (`201 Created`):**
```json
{
  "id": "9b1deb4d3b7d4fb9e1283a6913b5aa58",
  "original_url": "https://example.com",
  "file_path": "snapshots/1_example_com_20261125_120000.png",
  "timestamp": "2026-11-25T12:00:00Z"
}
```

#### 2. Get Snapshot Details (`GET /snapshots/{id}`)

**Response (`200 OK`):**
```json
{
  "id": "9b1deb4d3b7d4fb9e1283a6913b5aa58",
  "original_url": "https://example.com",
  "file_path": "snapshots/1_example_com_20261125_120000.png",
  "timestamp": "2026-11-25T12:00:00Z"
}
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.13+ installed
- [uv](https://docs.astral.sh/uv/) (recommended) or standard `pip` / `venv`

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Link-archiving-service-api
   ```

2. **Install project dependencies:**

   Using `uv`:
   ```bash
   uv sync
   ```

   *Or using standard pip:*
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e .
   ```

3. **Install Playwright browser binaries:**
   ```bash
   uv run playwright install chromium
   ```
   *(or `playwright install chromium` if inside an activated virtualenv)*

---

## 🏃 Running the Application

Start the local development server:

```bash
uv run fastapi dev app/main.py
```
*Or using uvicorn directly:*
```bash
uv run uvicorn app.main:app --reload
```

Once running, access:
- **API Base URL**: `http://127.0.0.1:8000`
- **Interactive Swagger Docs**: `http://127.0.0.1:8000/docs`
- **ReDoc Documentation**: `http://127.0.0.1:8000/redoc`

---

## 🧪 Testing & Linting

Run automated tests with `pytest`:
```bash
uv run pytest
```

Check and format code with `ruff`:
```bash
uv run ruff check .
uv run ruff format .
```

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
