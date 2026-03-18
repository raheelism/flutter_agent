# Skill: flutter-ui-generation

## Purpose
Convert UX and component plans into production-grade Flutter UI code.

## Inputs
- Approved brainstorm + plan + TDD artifacts
- Design references (wireframes/Figma/spec text)

## UI generation rules
1. Prefer composition with small reusable widgets.
2. Keep widgets focused on rendering and input handling.
3. Move business logic to controller/viewmodel/provider/bloc layers.
4. Use adaptive/responsive layouts for diverse device sizes.
5. Ensure accessibility basics (semantic labels, contrast, tap targets).

## Procedure
1. Build screen scaffold and app shell.
2. Implement reusable components first.
3. Integrate state holders from `flutter-state-management`.
4. Add loading/empty/error visuals for async content.
5. Match theme tokens (spacing, colors, typography).

## Output format
1. Screen-level widget tree summary
2. Reusable widget inventory
3. Theming/accessibility notes
4. Pending UI risks
