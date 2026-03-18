# Skill: flutter-build-deploy

## Purpose
Prepare and validate Flutter apps for Android/iOS distribution and CI/CD automation.

## Procedure
1. Build configuration
   - Confirm flavors/env strategy.
   - Confirm signing setup (keystore/cert profiles handled securely).

2. Quality gates before artifact generation
   - `flutter analyze`
   - `flutter test`
   - Integration test subset for release-critical flows

3. Artifact generation
   - Android: `flutter build apk` and/or `flutter build appbundle`
   - iOS: `flutter build ipa` (or Xcode archive flow)

4. CI/CD expectations
   - Cache pub dependencies
   - Run analysis + tests on each PR
   - Produce signed artifacts for release branches/tags

5. Release readiness checklist
   - Versioning/build numbers
   - Changelog/release notes
   - Crash/performance monitoring hooks

## Output format
1. Build commands by target
2. CI pipeline checklist
3. Signing/secrets handling notes
4. Release risks and mitigations
