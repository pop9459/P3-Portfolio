# NHL Stenden Computer Science P3 Portfolio

This repository aggregates multiple project repositories using Git subtrees.

- Name: Peter Kapsiar
- Student ID: 5486866
- Main repository: https://github.com/pop9459/P3-Portfolio

## Included Projects

- `P3-ComputerScience`
- `P3-EmbeddedSystems`
- `AutomaticCourtainBlinder`

## Quick Links

- [Computer Science Portfolio](P3-ComputerScience/portfolio.md)
- [Embedded Systems Portfolio](P3-EmbeddedSystems/portfolio.md)
- [AutomaticCourtainBlinder Portfolio](AutomaticCourtainBlinder/portfolio.md)
- [Combined Portfolio](PORTFOLIO.md)

## Updating the Combined Portfolio

Run these commands from the root of this repository.

### 1. Pull all subprojects

```bash
git subtree pull --prefix P3-ComputerScience https://github.com/pop9459/P3-ComputerScience main --squash && \
git subtree pull --prefix P3-EmbeddedSystems https://github.com/pop9459/P3-EmbeddedSystems main --squash && \
git subtree pull --prefix AutomaticCourtainBlinder https://github.com/pop9459/AutomaticCourtainBlinder main --squash
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
```
