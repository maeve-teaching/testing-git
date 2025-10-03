# Exercise 2: Branching

In this exercise, you will learn how to create a new branch in your Git repository, make changes to the code, and push your branch to the remote repository. This is an essential skill for collaborating with others in a project.

## Steps to Complete the Exercise

1. **Create a New Branch**
   - Open your terminal in Codespaces.
   - Ensure you are on the `main` branch by running:
     ```
     git checkout main
     ```
   - Pull the latest changes from the remote repository:
     ```
     git pull origin main
     ```
   - Create a new branch for your changes. You can name it something relevant, like `feature/branching-exercise`:
     ```
     git checkout -b feature/branching-exercise
     ```

2. **Make Changes**
   - Open `src/main.py` and add a new function or modify an existing one. For example, you could add a function that prints a message indicating you are working on a new branch. You can also just add a comment `# like this!`.
   - Save your changes.

3. **Stage and Commit Your Changes**
   - Stage the changes you made:
     ```
     git add src/main.py
     ```
   - Commit your changes with a descriptive message:
     ```
     git commit -m "Add new function to demonstrate branching"
     ```

4. **Push Your Branch to the Remote Repository**
   - Push your new branch to the remote repository:
     ```
     git push origin feature/branching-exercise
     ```

5. **Open a Pull Request**
   - Go to your GitHub repository in your web browser.
   - You should see a prompt to create a pull request for your newly pushed branch. Click on it.
   - Fill in the details for the pull request and submit it.

6. **Review and Merge the Pull Request**
   - If you are working with a partner, ask them to review your pull request.
   - Otherwise, read through and review it yourself.
   - Once reviewed, you can merge the pull request into the `main` branch.

## Conclusion

Congratulations! You have successfully created a new branch, made changes, pushed it to the remote repository, and opened a pull request. This exercise is crucial for understanding how to collaborate effectively using Git and GitHub.