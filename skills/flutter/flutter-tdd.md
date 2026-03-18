# Skill: flutter-tdd

## Purpose
Enforce Flutter test-first development.

## Preconditions
- `flutter-writing-plans` completed.

## Test pyramid rules
1. Unit tests for domain/business logic and use cases.
2. Widget tests for presentation behavior.
3. Integration tests for primary user journeys.

## Procedure
1. For each planned milestone, define failing tests first.
2. Prioritize deterministic tests (mock network/time/platform behavior).
3. Keep tests close to feature boundaries.
4. Add regression tests for every resolved bug.

## Required checks
- `flutter test`
- Widget tests cover loading/success/error states for async views.
- Critical flows include integration tests.

## Output format
1. Test matrix (file -> test type -> scenarios)
2. Red/green/refactor loop plan
3. Mocking strategy
4. Coverage risks and mitigations

## Quality gate
Do NOT allow implementation to proceed unless initial failing tests are specified.
