# Skill: flutter-brainstorming

## Purpose
Refine product ideas into an implementation-ready Flutter concept before planning or code.

## Mandatory position in workflow
This skill MUST run before `flutter-writing-plans`, `flutter-tdd`, or any code generation.

## Inputs
- Product/problem statement
- Target users and platforms (Android/iOS)
- Constraints (offline support, auth, localization, timelines)

## Procedure
1. Clarify product scope
   - Define primary user persona.
   - List top 3 user goals.
   - Define non-goals to avoid scope creep.

2. UX flow and screen breakdown
   - Build a happy-path user journey.
   - Enumerate screens and transitions.
   - Identify empty/loading/error states per screen.

3. Widget hierarchy planning
   - For each screen, draft:
     - Page-level scaffold
     - Primary layout widgets
     - Reusable widget candidates
   - Separate display widgets from logic owners.

4. Data and state boundaries
   - Identify entities/models.
   - Identify local UI state vs app/business state.
   - Identify async operations and side effects.

5. Risks and technical decisions
   - State management recommendation (Riverpod/Bloc/Provider) with rationale.
   - Navigation recommendation (GoRouter/Navigator 2.0) with rationale.
   - Platform/plugin dependencies and risks.

## Output format
Return all sections:
1. Problem framing
2. User personas and goals
3. Screen map + navigation flow
4. Widget hierarchy per screen
5. Data model candidates
6. Risks/unknowns
7. Assumptions needing confirmation

## Quality gate
Do NOT allow transition to planning unless:
- At least one complete end-to-end user flow exists.
- Each major screen has a first-pass widget hierarchy.
- State boundaries are explicitly documented.
