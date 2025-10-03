# Collaborative Workflow Instructions

This document provides a step-by-step guide for students working collaboratively on the git-collaboration-template project. Follow these instructions to learn how to work together using Git and GitHub.

## Step 1: Create a Repository from Template (Student A)

**Student A should complete this step:**

1. Navigate to the template repository on GitHub.
2. Click the green "Use this template" button.
3. Select "Create a new repository".
4. Give your repository a name (e.g., "git-collaboration-project").
5. Choose to make it public.
6. Click "Create repository from template".

## Step 2: Fork the Repository (Student B)

**Student B should complete this step:**

1. Navigate to Student A's newly created repository.
2. Click on the "Fork" button in the upper right corner to create a copy of the repository in your own GitHub account.

## Step 3: Access Your Repositories

Both students can work with their repositories in two ways:

### Option A: Using GitHub Codespaces (Recommended for beginners)

**For both Student A and Student B:**

1. Navigate to your respective repository on GitHub (Student A uses the original, Student B uses the fork).
2. Click the green "Code" button.
3. Select the "Codespaces" tab.
4. Click "Create codespace on main" or "+" to create a new codespace.
5. Wait for the codespace to load - this may take a few minutes.
6. Once loaded, you'll have a full development environment in your browser.

### Option B: Clone to Local Machine

(Better for general use)

**For both Student A and Student B:**

1. Navigate to your respective repository on GitHub.
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

## Step 4: Create Branches (Optional but Recommended)

**For both Codespaces and Local:**

Both students should create feature branches for their work:

```bash
git checkout -b feature/student-a-changes
```

```bash
git checkout -b feature/student-b-changes
```

## Step 5: Make Changes

**For both Codespaces and Local:**

1. Each student should work on different parts of the project to avoid conflicts initially.
2. Student A might modify `src/main.py` while Student B works on `src/utils/helpers.py`.
3. Make your changes and save the files.

## Step 6: Stage and Commit Changes

**For both Codespaces and Local:**

1. Stage your changes:

   ```bash
   git add .
   ```

2. Commit your changes with a descriptive message:

   ```bash
   git commit -m "Add feature: descriptive message"
   ```

## Step 7: Push Changes

**For both Codespaces and Local:**

1. Push your changes to your respective repositories:

   ```bash
   git push origin feature/your-branch-name
   ```

   Or if working directly on main:

   ```bash
   git push origin main
   ```

## Step 8: Create a Pull Request (Student B)

**Student B should complete this step:**

1. Navigate to Student A's original repository on GitHub.
2. You should see a prompt to create a pull request for your recently pushed changes.
3. Click "Compare & pull request".
4. Ensure the pull request is going from your fork to Student A's repository.
5. Add a title and description for your pull request.
6. Click "Create pull request".

## Step 9: Review and Merge (Student A)

**Student A should complete this step:**

1. Navigate to the "Pull requests" tab in your repository.
2. Click on the pull request created by Student B.
3. Review the changes by clicking on the "Files changed" tab.
4. Add comments or request changes if needed.
5. If the changes look good, click "Merge pull request".
6. Confirm the merge by clicking "Confirm merge".
7. Optionally, delete the feature branch by clicking "Delete branch".

## Step 10: Sync Changes

### For Student A (Codespaces and Local):

If you merged using a pull request and were working on a feature branch:

1. Switch to main branch:

   ```bash
   git checkout main
   ```

2. Pull the latest changes:

   ```bash
   git pull origin main
   ```

### For Student B:

**Codespaces and Local:**

To keep your fork up to date with Student A's repository:

1. Add Student A's repository as an upstream remote (only needed once):

   ```bash
   git remote add upstream <student-a-repository-url>
   ```

2. Fetch changes from upstream:

   ```bash
   git fetch upstream
   ```

3. Switch to your main branch:

   ```bash
   git checkout main
   ```

4. Merge upstream changes:

   ```bash
   git merge upstream/main
   ```

5. Push updated main to your fork:

   ```bash
   git push origin main
   ```

## Step 11: Continue Collaborating

Both students can now continue the cycle:
1. Create new feature branches
2. Make changes
3. Push changes
4. Create pull requests
5. Review and merge
6. Sync repositories

## Alternative: Direct Collaboration (Optional)

Instead of forking, Student A can invite Student B as a collaborator:

**Student A:**
1. Go to repository "Settings"
2. Click "Manage access"
3. Click "Invite a collaborator"
4. Enter Student B's GitHub username
5. Send invitation

**Student B:**
1. Accept the invitation via email or GitHub notifications
2. Clone Student A's repository directly (no fork needed)
3. Both students can push to the same repository using branches

## Conclusion

You have successfully completed the collaborative workflow! You've learned how to fork repositories, create pull requests, review code, and keep repositories synchronized. This workflow mirrors real-world collaborative development practices. Continue practicing with the exercises in the `exercises` directory to further enhance your Git and GitHub collaboration skills.