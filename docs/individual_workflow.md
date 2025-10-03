# Individual Workflow Instructions

This document provides a step-by-step guide for students working individually on the git-collaboration-template project. Follow these instructions to learn how to create branches, make changes, and merge them back into the main branch.

## Step 1: Create a Repository from Template

1. Navigate to the template repository on GitHub.
2. Click the green "Use this template" button.
3. Select "Create a new repository".
4. Give your repository a name (e.g., "my-git-practice").
5. Choose whether to make it public or private.
6. Click "Create repository from template".

## Step 2: Access Your Repository

You can work with your repository in two ways:

### Option A: Using GitHub Codespaces (Recommended for beginners)

1. Navigate to your newly created repository on GitHub.
2. Click the green "Code" button.
3. Select the "Codespaces" tab.
4. Click "Create codespace on main" or "+" to create a new codespace.
5. Wait for the codespace to load - this may take a few minutes.
6. Once loaded, you'll have a full development environment in your browser.

### Option B: Clone to Local Machine

1. Navigate to your newly created repository on GitHub.
2. Click the green "Code" button and copy the repository URL.
3. Open your terminal or command prompt.
4. Use the following command to clone the repository:

   ```bash
   git clone <repository-url>
   ```

5. Change into the project directory:

   ```bash
   cd <your-repository-name>
   ```

## Step 3: Create a New Branch

**For both Codespaces and Local:**

1. Before making any changes, create a new branch for your work. Use the following command, replacing `my-feature` with a descriptive name for your branch:

   ```bash
   git checkout -b my-feature
   ```

## Step 4: Make Changes

**For both Codespaces and Local:**

1. Open the `src/main.py` file in your code editor.
2. Make some changes to the script. For example, you can modify the greeting message or add a new function call.
3. Save your changes.

## Step 5: Stage and Commit Your Changes

**For both Codespaces and Local:**

1. Stage the changes you made:

   ```bash
   git add src/main.py
   ```

2. Commit your changes with a descriptive message:

   ```bash
   git commit -m "Updated greeting message in main.py"
   ```

## Step 6: Push Your Branch to GitHub

**For both Codespaces and Local:**

1. Push your feature branch to the remote repository:

   ```bash
   git push origin my-feature
   ```

## Step 7: Merge Changes Back to Main Branch

You have two options for merging:

### Option A: Using GitHub Pull Request (Recommended)

1. Navigate to your repository on GitHub.
2. You should see a prompt to create a pull request for your recently pushed branch.
3. Click "Compare & pull request".
4. Add a title and description for your pull request.
5. Click "Create pull request".
6. Review your changes and click "Merge pull request".
7. Confirm the merge by clicking "Confirm merge".
8. Optionally, delete the feature branch by clicking "Delete branch".

### Option B: Using Command Line

**For both Codespaces and Local:**

1. Switch back to the main branch:

   ```bash
   git checkout main
   ```

2. Pull any remote changes (good practice):

   ```bash
   git pull origin main
   ```

3. Merge your feature branch into the main branch:

   ```bash
   git merge my-feature
   ```

4. Push your changes to the remote repository:

   ```bash
   git push origin main
   ```

## Step 8: Clean Up

**For both Codespaces and Local:**

1. After merging, you can delete your feature branch locally:

   ```bash
   git branch -d my-feature
   ```

2. If you used the command line to merge and want to delete the remote branch:

   ```bash
   git push origin --delete my-feature
   ```

## Step 9: Sync Your Local Repository (Local Only)

**For Local Machine only:**

If you merged using a GitHub pull request, make sure to sync your local main branch:

1. Switch to main branch:

   ```bash
   git checkout main
   ```

2. Pull the latest changes:

   ```bash
   git pull origin main
   ```

## Conclusion

You have successfully completed the individual workflow for this project! You have learned how to create a repository from a template, create branches, make changes, and merge those changes back into the main branch using both GitHub's web interface and command line tools. Continue to explore the exercises provided in the `exercises` directory to further enhance your Git and GitHub skills.