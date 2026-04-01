# NHL Stenden Computer Science Y1 P3 Portfolio

This repository aggregates multiple project repositories using Git subtrees.

- Name: Peter Kapsiar
- Student ID: 5486866
- Main repository: https://github.com/pop9459/P3-Portfolio

## Quick Links

- [Computer Science Portfolio](P3-ComputerScience/portfolio.md)
- [Embedded Systems Portfolio](P3-EmbeddedSystems/portfolio.md)
- [AutomaticCourtainBlinder Portfolio](AutomaticCourtainBlinder/portfolio.md)
- [Professional Skills Portfolio](P3-ProfessionalSkills/portfolio.md)
- [Combined Portfolio](PORTFOLIO.md)

## Updating the Combined Portfolio

Run these commands from the root of this repository.

### 1. Pull all subprojects

```bash
git subtree pull --prefix P3-ComputerScience https://github.com/pop9459/P3-ComputerScience main --squash && \
git subtree pull --prefix P3-EmbeddedSystems https://github.com/pop9459/P3-EmbeddedSystems main --squash && \
git subtree pull --prefix AutomaticCourtainBlinder https://github.com/pop9459/AutomaticCourtainBlinder main --squash && \
git subtree pull --prefix P3-ProfessionalSkills https://github.com/pop9459/P3-ProfessionalSkills main --squash 
```

### 2. Regenerate Combined Portfolio

After pulling updates, rebuild the combined portfolio file:

```bash
python combine_portfolios.py
```

### 3. Then commit the changes

```bash
git add .
git commit -m "Update subprojects and regenerate portfolio"
git push
```

### 4. Generate PDF (optional)
To generate a PDF version of the combined portfolio, you can use this Visual Studio Code extension: [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf)

## Adding New Subproject Repositories

To add a new project repository as a subtree:

### 1. Add the new subtree

Replace `PROJECT_NAME`, `GITHUB_URL`, and `BRANCH` with your values:

```bash
git subtree add --prefix PROJECT_NAME GITHUB_URL BRANCH --squash
```

**Example:**
```bash
git subtree add --prefix MyNewProject https://github.com/username/my-new-project main --squash
```

### 2. Update "Quick Links" section

Add a new bullet point for the new project in the "Quick Links" section of this README:

```markdown
- [My New Project Portfolio](PROJECT_NAME/portfolio.md)
```

### 3. Update pull command

Add a new line to the `git subtree pull` command in section "1. Pull all subprojects":

```bash
git subtree pull --prefix PROJECT_NAME GITHUB_URL BRANCH --squash && \
```

### 4. Regenerate and commit

```bash
python combine_portfolios.py
git add .
git commit -m "Add PROJECT_NAME as subtree"
```

The script will automatically detect and merge the new project's portfolio file (if it exists) into `PORTFOLIO.md`.
