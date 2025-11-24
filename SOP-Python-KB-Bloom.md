# SOP: Python Knowledge Base (Obsidian) — Bloom-aware

This variant of the SOP adds guidance to design content using Bloom's Taxonomy and to follow beginner-first learning paths.

## Why Bloom's Taxonomy here
Bloom's Taxonomy helps structure learning goals from simple recall (Remember) up to creation (Create). When building atomic notes, tagging each note with a Bloom level and ordering MOCs accordingly enables progressive learning and better onboarding for beginners.

## Additions to Phase 2 — Atomic Notes
- Frontmatter additions (recommended):
  - `difficulty`: Beginner | Intermediate | Advanced
  - `bloom_level`: Remember | Understand | Apply | Analyze | Evaluate | Create
  - `learning_objectives`: short list of objectives matching Bloom stages
- Each note should include an "Exercises by Bloom Level" section providing tasks that map to each level.
- When creating or updating notes, prefer starting at Remember/Understand for beginner-facing content.

## Phase 1 — MOCs and Beginner Paths
- Create a `Python - Beginner Learning Path (MOC)` that orders starter notes by Bloom level.
- MOCs should have a short description indicating their intended audience (e.g., Beginner Path, Intermediate Topics).

## Workflow rules (quick)
1. Search the vault for existing notes first. If a note exists, update frontmatter to include bloom_level and learning objectives.
2. For new notes, prefer `difficulty: Beginner` and `bloom_level: Remember/Understand` until content is mature.
3. Add exercises ranging from Remember → Create to support progression.
4. Link notes back to both the relevant MOC and the beginner path MOC when appropriate.

## Example frontmatter (beginner-targeted)
```
---
tags: [python]
moc: [[Python Fundamentals (MOC)]]
difficulty: Beginner
bloom_level: Remember
learning_objectives:
  - "Remember: list the syntax"
  - "Understand: explain how it works"
---
```

## Tools & Recommendation
- Continue to use Obsidian Git for backups. Consider adding a tag `learning-path` for notes included in the Beginner MOC to quickly filter progress.

---

This file augments the main SOP with Bloom-aware guidance; you can merge the guidance into `SOP-Python-KB.md` or keep it as a separate reference.
