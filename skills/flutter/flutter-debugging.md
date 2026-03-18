# Skill: flutter-debugging

## Purpose
Debug Flutter issues systematically across UI, state, and platform layers.

## Common issue buckets
1. Layout/render overflow and constraints
2. State sync bugs/race conditions
3. Async/network handling issues
4. Performance/jank and rebuild hot spots
5. Platform-specific plugin/channel failures

## Procedure
1. Reproduce and isolate
   - Define exact steps and expected vs actual behavior.
2. Instrument
   - Add targeted logs/assertions, inspect stack traces, and use Flutter DevTools.
3. Hypothesis-driven fixes
   - Change one variable at a time.
4. Verify
   - Add/extend tests to lock fix.
5. Prevent regression
   - Document root cause and guardrails.

## Performance checks
- Rebuild minimization (`const`, split widgets, selectors).
- Frame timing and raster/UI thread analysis.
- Image/cache/memory considerations.

## Output format
1. Repro case
2. Root cause
3. Fix summary
4. Verification steps
5. Regression tests added
