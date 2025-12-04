# School Hosted Tasks — Guide

This guide explains how to prepare and upload School Hosted Tasks to the HKOI Online Judge platform.

## Overview

- Task IDs for school-hosted tasks must start with one of the letters: `U`, `V`, `W`, `X`, `Y`, `Z`. This avoids
  collisions with other schools.
- Choose a concise, descriptive title so users can find the task via search.
- Only original tasks created by your school may be uploaded. If you want to redistribute the task to other users
  from your school, you must grant HKOI a CC-BY licence (see Terms of Use for details).

## Statement (Markdown)

- Write the problem statement in Markdown (GitHub-flavored Markdown features are supported).
- All sections (including sample explanations and subtask constraints) support Markdown.
- Wrap math expressions with dollar signs. Example: `$1 \\le K < N \\le 100$`.
  - Do not split math expressions across multiple lines.
  - To render a literal dollar sign use `\\$`.

## Samples

- Format samples carefully: do not include trailing whitespace at the end of any line and ensure the last line
  ends with a newline character.
- Keep sample numbering sequential.

## Images

- The Markdown renderer does not support image resizing; scale images before uploading.
- Prefer `PNG` for simple diagrams and `JPG` for complex photographs.

## Custom Checker Program (optional)

If a task accepts multiple correct outputs (or needs special grading), provide a custom checker written in C++17.

- Invocation:

```text
checker.exe {input_filename} {output_filename} {answer_filename}
```

  - `output_filename` is the contestant's output.
  - `answer_filename` is the model answer (test data output file).

- You may use `testlib.h` or example checkers as needed.
- The checker must report the verdict using one of these methods:
  - Exit status: return `0` for Accepted, `1` for Wrong Answer (or other non-AC states).
  - Standard error: print a score (0–100) on the first line of `stderr` and exit with code `0`.
  - Testlib API: call `quitf(_ok, ...)`, `quitf(_wa, ...)`, etc.
- The checker program must not crash and must respect the same time and memory limits as solutions.

## Solution Program (model solution)

- Provide a model solution in any supported language. The system uses it to verify and validate the task.
- Validate inputs where appropriate (e.g., `assert(n >= 1 && n <= 100)`) when helpful for sanity.

## Subtasks

- In the Test Data tab, set the number of test cases and subtasks.
- If adding subtasks, make sure subtask numbers are sequential and the total score sums to `100`.
- Leaving the constraints field blank hides that subtask from the statement.

## Test Data

- Upload test data files named `subtask-case.in` and `subtask-case.out` (this naming is required).
- Test files must not contain trailing whitespace and must end with a newline.
- Windows EOLs will be converted to LF automatically, but do not include a byte order mark (BOM).

## Enable Submissions

- Changing a task status from `Disabled` to `Submissions Allowed` triggers an automatic verification submission.
- The platform will set the task to `Submissions Allowed` if the verification submission is Accepted.

## Task Visibility

- Tasks are initially `Hidden` (visible to School Admins only).
- After preparation, you may make a task `Visible` if your school holds a School Licence (Full Version) and you
  have enough storage.
- If a previously visible task is made hidden again, students can no longer access its submissions.

## Submission Visibility and Solves

- Submissions to school-hosted tasks are visible only to users within the same school.
- Submissions from other schools are not shown under Judge Status.
- Solves from school-hosted tasks:
  - do not appear on the home page;
  - do not count toward the global leaderboard;
  - do not appear in the user profile or stats page.
- You can add hosted tasks to Matrix: Task — solves will then appear in Matrix: Weekly.

## Limits

- Time limit: `1.000 s` (fixed).
- Memory limit: `256 MB` (fixed).
- These limits apply to both solution programs and custom checkers.

## Field Lengths and Counts

- Main Statement, After Samples: `20 KB` each.
- Constraint fields, subtask constraints, and sample explanations: `2 KB` each.
- Number of images: `20`.
- Maximum size per image: `5 MB`.
- Number of samples: `10`.
- Number of subtasks: `10`.
- Test cases per subtask: up to `100`.
- Max size per test case file: `20 MB`.

## Storage Limits

- School Licence (Full Version): `6144 MB`.
- Other schools: `100 MB`.

Consumed storage components:

- Task metadata (statement, compiled solutions, etc.): fixed `16384 KB` per task.
- Uploaded images: sizes rounded up to nearest `128 KB`, then multiplied by `16`.
- Test data: sizes rounded up to nearest `128 KB`.

## Expiration

- If the School Licence (Full Version) expires:
  - existing visible tasks remain visible but students cannot make new submissions;
  - visible tasks may be made hidden;
  - hidden tasks cannot be made visible again while the licence is expired.

---
