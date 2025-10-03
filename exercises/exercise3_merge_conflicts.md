# Exercise 3: Merge Conflicts

In this exercise, you will intentionally create merge conflicts to learn how to resolve them. Follow the steps below to complete the exercise.

If you are doing this exercise without a partner, just repeat the steps first for student A, and then for student b, creating different branches with different changes.

## Steps to Create Merge Conflicts

1. **Set Up Your Environment**:
   - Ensure you have the repository set up in Codespaces.
   - Both students should clone the repository or fork it as per the collaborative workflow.
      - This will work either as collaborators on one repository, or with a repository and a fork of the repository. The guide below is for a single repository, but just follow the forking guidelines if you are working on two repositories.

2. **Create a New Branch**:
   - Each student should create a new branch from the `main` branch. You can name your branches `feature/student1` and `feature/student2`.

   ```bash
   git checkout -b feature/student1
   ```

   ```bash
   git checkout -b feature/student2
   ```

3. **Make Changes to `src/main.py`**:
   - In `src/main.py`, both students will modify the same line of code. For example, change the greeting message in the `greet` function.

   **Student 1**:
   ```python
   def greet():
       return "Hello from Student 1!"
   ```

   **Student 2**:
   ```python
   def greet():
       return "Hello from Student 2!"
   ```

4. **Commit Your Changes**:
   - After making the changes, commit them to your respective branches.

   ```bash
   git add src/main.py
   git commit -m "Update greeting message in main.py"
   ```

5. **Push Your Changes**:
   - Push your changes to the remote repository.

   ```bash
   git push origin feature/student1
   ```

   ```bash
   git push origin feature/student2
   ```

6. **Open Pull Requests**:
   - Each student should open a pull request (PR) from their feature branch to the `main` branch.

7. **Merge the First Pull Request**:
   - One student should merge their pull request first. This will update the `main` branch with their changes.

8. **Attempt to Merge the Second Pull Request**:
   - The second student will now attempt to merge their pull request. This should result in a merge conflict since both students modified the same line in `src/main.py`.

## Resolving Merge Conflicts

1. **Identify the Conflict**:
   - Git will indicate that there is a conflict in `src/main.py`. Open the file to see the conflict markers.

2. **Resolve the Conflict**:
   - Edit `src/main.py` to resolve the conflict. You can choose one of the greetings or combine them as needed.

   Example resolution:
   ```python
   def greet():
       return "Hello from Student 1 and Student 2!"
   ```

3. **Mark the Conflict as Resolved**:
   - After resolving the conflict, add the file to the staging area.

   ```bash
   git add src/main.py
   ```

4. **Commit the Resolved Changes**:
   - Commit the changes to finalize the merge.

   ```bash
   git commit -m "Resolve merge conflict in main.py"
   ```

5. **Complete the Merge**:
   - Push the resolved changes to the remote repository.

   ```bash
   git push origin feature/student2
   ```

## Conclusion

Congratulations! You have successfully created and resolved a merge conflict. This exercise has helped you understand how to handle conflicts in Git, which is an essential skill for collaborative development.