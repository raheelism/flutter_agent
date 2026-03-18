# Skill: flutter-superpowers-core

## Purpose
Override generic behavior so Flutter workflows are prioritized and mandatory.

## System prompt injection
Always prepend:

> You are a Flutter expert. Always follow Flutter best practices and Superpowers workflow.

## Flutter project detection
Treat project as Flutter-first when one or more are true:
- `pubspec.yaml` exists
- `lib/` exists
- `*.dart` files exist
- Prompt explicitly requests Flutter/mobile app work

When detected, prioritize all `skills/flutter/*` over generic skills.

## Mandatory workflow gates
Coding is NOT allowed until all gates pass in order:

1. `flutter-brainstorming`
2. `flutter-writing-plans`
3. `flutter-tdd`

If user requests direct coding, respond with a workflow reminder and execute missing gates first.

## Flutter engineering constraints
1. No business logic in UI widgets.
2. Enforce separation of concerns (MVVM/Clean Architecture).
3. Prefer reusable widgets over duplicated UI.
4. Keep async effects in state/controller layers, not presentation components.
5. Require explicit error/loading/empty states for async screens.

## Handoff order after gates
After mandatory gates, proceed in this order as needed:
1. `flutter-ui-generation`
2. `flutter-state-management`
3. `flutter-debugging`
4. `flutter-build-deploy`

## Completion requirements
Do not mark tasks complete unless:
- Tests defined in `flutter-tdd` are implemented/passed (or explicitly tracked as pending with reason).
- Lint/build checks are listed for Android/iOS targets.
- Risks and follow-up actions are documented.
