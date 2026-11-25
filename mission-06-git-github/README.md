# Mission 06 — Git and GitHub Workflow

## 1. Task / Objective

The objective of this mission was to understand Git and GitHub workflows, practise creating branches, tracking changes, committing files, pushing changes and creating a Pull Request.

## 2. Work Completed

- Practised Git commands for version control.
- Created a new branch named `update-about`.
- Updated the root README.md file.
- Added a My Learning section.
- Committed and pushed the changes to GitHub.
- Created a Pull Request from `update-about` to `main`.

## 3. Git Commands Practised

| Command | Purpose |
|---|---|
| `git status` | Checks the current working tree status |
| `git branch` | Displays available branches |
| `git branch --show-current` | Displays the current branch |
| `git switch -c update-about` | Creates and switches to a new branch |
| `git add README.md` | Adds changes to the staging area |
| `git commit -m "message"` | Saves changes as a commit |
| `git push -u origin update-about` | Pushes the branch to GitHub and sets its upstream |
| `git push` | Pushes new commits to the connected remote branch |

## 4. Branching

A branch is a separate line of development in Git.

For this mission, I created a branch named `update-about` to make changes without directly modifying the main branch.

Command used:

```bash
git switch -c update-about
```

## 5. Changes Made

I updated the root README.md file by adding a My Learning section.

This section describes the concepts and skills learned during the completed missions.

## 6. Pull Request

A Pull Request (PR) is a request to review and merge changes from one branch into another.

For this mission:

- Base branch: `main`
- Compare branch: `update-about`
- Purpose: To submit the README changes for review.
- Status: Created and awaiting review.

The Pull Request was not merged because the assignment instructions require waiting for the instructor's permission before merging.

## 7. My Understanding

I learned how Git tracks changes and how branches allow developers to work separately from the main project. I also understood how GitHub Pull Requests are used to submit changes for review.

## 8. Difficulties Faced

When I first tried pushing the new branch using `git push`, Git displayed an error saying that the branch had no upstream branch.

## 9. How I Resolved Them

I used the following command to push the branch and connect it to the remote repository:

```bash
git push -u origin update-about
```

The branch was successfully pushed to GitHub, and I created the Pull Request.

## 10. Evidence / Files

- Root `README.md` — Updated with the My Learning section.
- This README — Documents the Git and GitHub activities performed in this mission.
- GitHub Pull Request — Shows the submitted branch changes.

## 11. Commit Details

To be updated after committing and pushing this mission documentation.