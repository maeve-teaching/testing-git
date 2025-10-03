# Exercise 1: Basic Changes

In this exercise, you will make simple changes to the `main.py` file and commit those changes. This will help you understand how to edit files, stage changes, and commit them using Git.

## Instructions

1. **Open the Project**: Start by opening the project in your Codespace.

2. **Locate `main.py`**: Navigate to the `src` directory and open the `main.py` file. This file is the main entry point of the application.

3. **Make Changes**: 
   - Look for the function that prints a greeting message. 
   - Modify the greeting message to say something different. For example, change it from "Hello, World!" to "Welcome to Git Collaboration!".
   - You can also add a new print statement below the existing ones to display your name or any other message.

4. **Save Your Changes**: After making your edits, save the `main.py` file.# 
   - If this was real work and not a training exercise, you'd obviously test your changes and make sure everything is working!!

5. **Check Git Status**: Open the terminal in your Codespace and run the following command to see the status of your changes:
   ```
   git status
   ```

6. **Stage Your Changes**: Stage the changes you made to `main.py` by running:
   ```
   git add src/main.py
   ```

7. **Commit Your Changes**: Commit your changes with a descriptive message:
   ```
   git commit -m "Updated greeting message in main.py"
   ```

8. **Push Your Changes**: If you are working on your own repository, push your changes to the remote repository:
   ```
   git push origin main
   ```

9. **Review Your Changes**: Go to your GitHub repository in your web browser and review the changes you made. You should see the commit listed in the commit history.

10. **Collaborative Work**: If you are working with a partner, share your repository link with them and ask them to pull the latest changes to see your updates.

## Conclusion

Congratulations! You have successfully made and committed changes to a file in your Git repository. This exercise has introduced you to the basic workflow of editing files, staging changes, and committing them using Git.