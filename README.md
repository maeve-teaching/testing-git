# Git Collaboration Template

Welcome to the Git Collaboration Template! This repository is designed to help students learn how to collaborate using Git and GitHub, both in pairs and individually. 

## Table of Contents with things added
- [Getting Started](#getting-started)
- [Collaborative Workflow](#collaborative-workflow)
- [Individual Workflow](#individual-workflow)
- [Exercises](#exercises)
- [Project Structure](#project-structure)

## Getting Started
To get started, you can either create a repository using this template. Follow the instructions below based on your chosen workflow.

## Individual Workflow
1. **Create a Repository from Template**: create a new repository using this template.
2. **Clone the Repository**: clone the repository to your local machine or open an instance of Codespaces.
3. **Create a Branch**: create a new branch for your changes.
4. **Make Changes**: edit the code as needed; add and commit your changes.
6. **Push Changes**: push the branch to the remote repository.
7. **Merge Changes**: merge your branch back into the main branch.

For detailed steps, refer to the [Individual Workflow Document](docs/individual_workflow.md).

## Collaborative Workflow
1. **Create a Repository from Template**: one student should create a new repository using this template.
2. **Fork the Repository**: The second student should fork the newly created repository.
3. **Clone the Repositories**: Both students should clone their respective repositories to their local machines or open Codespaces on their version.
4. **Make Changes**: Each student can work on their own features or fixes in their respective environments. Add and commit changes. Use branches if desired, as in the individual workflow.
5. **Push Changes**: After making changes, push them to their remote repositories.
6. **Open Pull Requests**: The student who created the fork can open up a pull request to merge their changes.

For detailed steps, refer to the [Collaborative Workflow Document](docs/collaborative_workflow.md).


## Exercises
To practice your Git skills, complete the following exercises:
- [Exercise 1: Basic Changes](exercises/exercise1_basic_changes.md)
- [Exercise 2: Branching](exercises/exercise2_branching.md)
- [Exercise 3: Merge Conflicts](exercises/exercise3_merge_conflicts.md)

## Project Structure
```
git-collaboration-template
├── src
│   ├── main.py
│   ├── utils
│   │   └── helpers.py
│   └── data
│       └── sample_data.txt
├── docs
│   ├── collaborative_workflow.md
│   └── individual_workflow.md
├── exercises
│   ├── exercise1_basic_changes.md
│   ├── exercise2_branching.md
│   └── exercise3_merge_conflicts.md
├── .gitignore
├── .devcontainer
│   └── devcontainer.json
├── requirements.txt
└── README.md
```

Happy coding and collaborating!