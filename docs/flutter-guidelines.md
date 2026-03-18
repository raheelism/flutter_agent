# Flutter Guidelines for Superpowers Agent

## Development principles

1. **Workflow discipline**
   - Always run brainstorming, planning, and TDD before implementation.
2. **Separation of concerns**
   - UI widgets render and forward interactions.
   - Domain logic lives in use cases/services/controllers.
3. **Feature-first organization**
   - Group code by feature with presentation/domain/data layers.
4. **Testability**
   - Design for deterministic tests and dependency injection.
5. **Performance and accessibility**
   - Avoid unnecessary rebuilds, support semantics and responsive layouts.

## Flutter architecture baseline

Recommended structure:

- `lib/app/` app shell, routing, theming
- `lib/core/` shared utilities, network, failures, constants
- `lib/features/<feature>/`
  - `presentation/` screens/widgets/viewmodels
  - `domain/` entities/usecases/repositories (contracts)
  - `data/` repository implementations, DTOs, data sources

## State management policy

Default: **Riverpod** for medium/large apps unless constraints suggest Bloc/Provider.

Rules:
- Keep state transitions explicit.
- Represent async states via sealed patterns (`loading`, `data`, `error`).
- Do not make network calls directly in widgets.

## Navigation policy

Use **GoRouter** or Navigator 2.0 style declarative routing for multi-screen apps.

Rules:
- Centralize route definitions.
- Keep route guards/auth logic outside UI widgets.
- Ensure deep-link capability for production apps.

## Platform integration policy

- Prefer vetted Flutter plugins.
- Use platform channels only when plugin alternatives are insufficient.
- Document platform permissions and configuration changes in plans.

## Build and deployment policy

Required pre-release checks:
- `flutter analyze`
- `flutter test`
- Critical-path integration tests

Release outputs:
- Android AAB/APK
- iOS IPA/archive

## Debugging policy

- Reproduce first, then fix.
- Use DevTools for frame/render/memory analysis.
- Add regression tests for every bug fix.

## TDD policy

For each milestone:
1. Write failing tests
2. Implement minimal code to pass
3. Refactor while keeping tests green

No feature is complete without:
- Unit coverage for core logic
- Widget tests for view states
- Integration coverage for critical journeys
