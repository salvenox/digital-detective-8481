# Mission 06 — Git and GitHub

## 1. Task / Objective

The objective of this mission was to learn how Git and GitHub work and practise basic version control operations such as creating branches, committing changes, pushing code and creating Pull Requests.

## 2. Work Completed

- Practised basic Git commands.
- Created a separate branch named `update-about`.
- Updated the main project README.md file.
- Added a My Learning section to the root README.
- Committed the changes.
- Pushed the branch to GitHub.
- Created a Pull Request for review.

## 3. Git Commands Practised

| Command | Purpose |
|---|---|
| `git status` | Checks the status of files |
| `git branch` | Displays available branches |
| `git switch -c update-about` | Creates and switches to a new branch |
| `git add README.md` | Adds changes to staging |
| `git commit -m "message"` | Saves changes in Git |
| `git push` | Uploads commits to GitHub |
| `git push -u origin update-about` | Pushes a new branch and connects it to the remote branch |

## 4. Branching

A branch is a separate version of the project where changes can be made without directly modifying the main branch.

For this mission, I created a branch named `update-about`.

Command used:

```bash
git switch -c update-about
```

## 5. README Update

I updated the root README.md file and added a section named My Learning.

This section contains a summary of the concepts I learned in the previous missions.

## 6. GitHub Pull Request

A Pull Request is a request to review changes made in one branch before merging them into another branch.

Details of my Pull Request:

- Source branch: `update-about`
- Target branch: `main`
- Purpose: Submit the README changes for review.
- Status: Created on GitHub.

The Pull Request has not been merged because the assignment instructions require instructor permission before merging.

## 7. My Understanding

I learned how Git helps track changes in a project and how GitHub allows developers to collaborate. I also understood the importance of branches and Pull Requests in software development.

## 8. Difficulties Faced

Initially, Git displayed an error because the new branch did not have an upstream branch configured.

## 9. How I Resolved Them

I used the following command:

```bash
git push -u origin update-about
```

This successfully uploaded the branch and configured its upstream connection.

## 10. Evidence / Files

- Root README.md — Updated with the My Learning section.
- This README — Documents the Git and GitHub practical activities.
- GitHub Pull Request — Contains the submitted changes.

## 11. Commit Details

Branch: `update-about`

Changes committed and pushed to the GitHub repository.