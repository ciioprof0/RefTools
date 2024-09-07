#!/usr/bin/env python
# -*- coding: utf-8 -*-
# src/domain/model.py

"""
This module defines the core domain models for the project.

It includes the `Repository` and `GitHubUser` classes that represent
a user's repository and a GitHub user, respectively. These models
are used to store information about repositories and users in the
business domain.
"""

from typing import List, Dict


class Repository:
    """
    A class representing a repository in the system.

    This class stores information about a repository, such as its name,
    URL, description, and the directory structure of its contents.

    Attributes:
        name (str): The name of the repository.
        url (str): The URL of the repository.
        description (str): A brief description of the repository.
        inventory (dict): A dictionary containing directories and root files.
    """

    def __init__(self, name: str, url: str, description: str = "") -> None:
        """
        Initializes a new Repository object.

        Args:
            name (str): The name of the repository.
            url (str): The URL of the repository.
            description (str): A brief description of the repository.
        """
        self.name = name
        self.url = url
        self.description = description
        self.inventory = {"directories": [], "root_files": []}

    def add_directory(self, dir_name: str, files: List[Dict[str, str]]) -> None:
        """
        Adds a directory and its associated files to the repository's inventory.

        Args:
            dir_name (str): The name of the directory.
            files (List[Dict[str, str]]): A list of file metadata for the directory.
        """
        self.inventory["directories"].append({"name": dir_name, "files": files})

    def add_root_file(self, file_name: str, description: str) -> None:
        """
        Adds a file to the root of the repository.

        Args:
            file_name (str): The name of the file to add.
            description (str): A brief description of the file.
        """
        self.inventory["root_files"].append({"name": file_name, "description": description})


class GitHubUser:
    """
    A class representing a GitHub user in the system.

    This class stores information about the user and their repositories.

    Attributes:
        username (str): The GitHub username.
        repositories (List[Repository]): A list of repositories owned by the user.
    """

    def __init__(self, username: str) -> None:
        """
        Initializes a new GitHubUser object.

        Args:
            username (str): The GitHub username.
        """
        self.username = username
        self.repositories = []

    def add_repository(self, repo: Repository) -> None:
        """
        Adds a repository to the user's list of repositories.

        Args:
            repo (Repository): The repository to add to the user.
        """
        self.repositories.append(repo)
