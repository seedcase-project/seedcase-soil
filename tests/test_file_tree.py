import pytest

from seedcase_soil.file_tree import file_tree


@pytest.fixture
def package_dir(tmp_path):
    (tmp_path / "data").mkdir()
    (tmp_path / "data" / "raw.csv").touch()
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "index.md").touch()
    (tmp_path / "README.md").touch()
    (tmp_path / "datapackage.json").touch()
    (tmp_path / ".git").mkdir()
    (tmp_path / ".git" / "config").touch()
    return tmp_path


def test_file_tree_returns_string(package_dir):
    assert isinstance(file_tree(package_dir), str)


def test_file_tree_excludes_git(package_dir):
    assert ".git" not in file_tree(package_dir)


def test_file_tree_includes_files(package_dir):
    result = file_tree(package_dir)
    for file in ["raw.csv", "index.md", "README.md", "datapackage.json"]:
        assert file in result
    for dir in ["data", "docs"]:
        assert dir in result


def test_file_tree_errors_with_non_directory(tmp_path):
    file_path = tmp_path / "README.md"
    file_path.touch()
    with pytest.raises(ValueError, match="is not a directory"):
        file_tree(file_path)
