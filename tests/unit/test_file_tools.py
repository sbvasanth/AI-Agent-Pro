from src.tools import file_tools

# -----------------------------
# read_file()
# -----------------------------


def test_read_existing_file(tmp_path, monkeypatch):
    # Create a temporary documents folder
    docs = tmp_path / "documents"
    docs.mkdir()

    # Create a sample file
    sample = docs / "hello.txt"
    sample.write_text("Hello AI Agent")

    # Replace BASE_DIR with our temporary folder
    monkeypatch.setattr(file_tools, "BASE_DIR", docs)

    result = file_tools.read_file.invoke({"filename": "hello.txt"})

    assert result == "Hello AI Agent"


def test_read_missing_file(tmp_path, monkeypatch):
    docs = tmp_path / "documents"
    docs.mkdir()

    monkeypatch.setattr(file_tools, "BASE_DIR", docs)

    result = file_tools.read_file.invoke({"filename": "missing.txt"})

    assert "was not found" in result


# -----------------------------
# find_file()
# -----------------------------


def test_find_existing_file(tmp_path, monkeypatch):
    docs = tmp_path / "documents"
    docs.mkdir()

    file = docs / "notes.txt"
    file.write_text("Python")

    monkeypatch.setattr(file_tools, "BASE_DIR", docs)

    result = file_tools.find_file.invoke({"filename": "notes"})

    assert result == "notes.txt"


def test_find_missing_file(tmp_path, monkeypatch):
    docs = tmp_path / "documents"
    docs.mkdir()

    monkeypatch.setattr(file_tools, "BASE_DIR", docs)

    result = file_tools.find_file.invoke({"filename": "unknown"})

    assert result == "NOT_FOUND"
