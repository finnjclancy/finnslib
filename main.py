# main.py
from pathlib import Path
import os

from finnslib.summarise.file import summarise_file
from finnslib.repo.tree import write_repo_tree
from finnslib.summarise.tree_with_files import summarise_repo_tree

if __name__ == "__main__":
    apikey = ""
    if not apikey:
        raise RuntimeError("please set OPENAI_API_KEY")

    # example 1: summarise this main.py file
    file_summary = summarise_file(
        path="main.py",
        apikey=apikey,
        level="long"
    )
    print("file summary written to:", file_summary)
    print(Path(file_summary).read_text())

    # example 2: write plain repo tree (no summaries)
    # change this part
    tree_path = write_repo_tree(
        root_dir=".",   # use repo_path
        output_file="repo_tree.txt"
    )

    print("repo tree written to:", tree_path)
    print(Path(tree_path).read_text())

    # example 3: summarise the repo tree
    tree_summaries = summarise_repo_tree(
        root_dir=".",   # keep this, because summarise_repo_tree might actually be 'path'
        output_file="tree_with_summaries.txt",
        apikey=apikey,
        level="short"
    )
    print("repo tree with summaries written to:", tree_summaries)
    print(Path(tree_summaries).read_text())