# Skill: flutter-state-management

## Purpose
Apply a structured state management strategy (Riverpod/Bloc/Provider) with clean boundaries.

## Decision framework
Choose based on scope/complexity:
- Riverpod: default for scalable compile-safe dependency/state handling.
- Bloc: event-driven workflows requiring strict transitions.
- Provider: simpler apps or lightweight inherited dependencies.

## Rules
1. No mutable app state in UI widgets.
2. One source of truth per feature state.
3. Async states represented explicitly (loading/data/error).
4. Side effects isolated in repositories/services/controllers.

## Procedure
1. Define state models/events/intents.
2. Define controller/provider/bloc responsibilities.
3. Wire dependencies through DI boundaries.
4. Map UI interactions to state transitions.
5. Add unit/widget tests for transitions and rendering.

## Output format
1. Selected pattern + rationale
2. State diagram/table
3. Provider/bloc/class map
4. Error/retry handling strategy
