# Skill: flutter-writing-plans

## Purpose
Translate brainstorm output into an actionable Flutter implementation plan.

## Preconditions
- `flutter-brainstorming` output is available and approved.

## Procedure
1. Architecture selection
   - Choose architecture style (feature-first clean architecture by default).
   - Define presentation/domain/data responsibilities.

2. File structure planning
   - Propose exact files and folders under `lib/`.
   - Include `core/` shared layers and feature modules.
   - Map each file to responsibility.

3. Implementation slices
   - Break work into small vertical increments.
   - Each increment must include tests first.

4. Dependency & plugin plan
   - List packages and why they are needed.
   - Identify platform setup steps (Android/iOS permissions/config).

5. Definition of done
   - Lint/build requirements
   - Test pass criteria
   - UX acceptance checks

## Output format
1. Architecture decision
2. File-by-file plan
3. Incremental milestones
4. Dependency/plugin plan
5. Acceptance criteria

## Quality gate
Do NOT transition to implementation unless:
- File-level responsibilities are explicit.
- Each milestone has test tasks.
- Shared/reusable widgets are identified.
