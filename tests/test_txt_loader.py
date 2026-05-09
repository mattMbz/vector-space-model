import pytest

from vsm.exceptions import EmptyDocumentsError
from vsm.loaders import load_txt_directory, load_txt_file


def test_load_txt_file_reads_text(tmp_path):
    file_path = tmp_path / "doc.txt"
    file_path.write_text("hello world", encoding="utf-8")

    assert load_txt_file(file_path) == "hello world"


def test_load_txt_directory_returns_documents_by_filename_stem(tmp_path):
    (tmp_path / "b.txt").write_text("second document", encoding="utf-8")
    (tmp_path / "a.txt").write_text("first document", encoding="utf-8")
    (tmp_path / "ignored.md").write_text("ignored", encoding="utf-8")

    docs = load_txt_directory(tmp_path)

    assert docs == {
        "a": "first document",
        "b": "second document",
    }


def test_load_txt_directory_raises_when_no_txt_files(tmp_path):
    (tmp_path / "doc.md").write_text("not loaded", encoding="utf-8")

    with pytest.raises(EmptyDocumentsError):
        load_txt_directory(tmp_path)


def test_load_txt_directory_raises_when_directory_does_not_exist(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_txt_directory(tmp_path / "missing")
