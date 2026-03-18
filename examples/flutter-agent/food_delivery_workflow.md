# Example Workflow: "Build a food delivery Flutter app"

This example demonstrates the mandatory sequence:
1. Brainstorming
2. Writing plans
3. TDD
4. Implementation

---

## Brainstorm output (`flutter-brainstorming`)

### Problem framing
Users need a fast way to browse nearby restaurants, place orders, and track deliveries.

### Personas and goals
- Busy professional: reorder quickly in under 60 seconds.
- Family planner: compare options and estimated delivery times.
- Student: apply discounts and track budget.

### Screen map
- Onboarding/Login
- Home (restaurant feed)
- Restaurant detail
- Cart
- Checkout
- Order tracking

### Widget hierarchy (Home screen)
- `Scaffold`
  - `AppBar`
  - `Column`
    - `SearchBar`
    - `CategoryChips`
    - `Expanded`
      - `ListView`
        - `RestaurantCard` (reusable)

### Risks
- Real-time tracking requires websocket/background handling.
- Payment plugins differ between Android and iOS.

---

## Plan output (`flutter-writing-plans`)

### File structure (excerpt)
- `lib/features/restaurants/presentation/home_screen.dart`
- `lib/features/restaurants/presentation/widgets/restaurant_card.dart`
- `lib/features/cart/domain/cart_item.dart`
- `lib/features/cart/domain/cart_repository.dart`
- `lib/features/cart/data/cart_repository_impl.dart`
- `lib/features/cart/presentation/cart_screen.dart`

### Milestones
1. Home feed read-only flow (tests + UI)
2. Cart operations (tests + state)
3. Checkout form and validation
4. Order tracking skeleton

---

## TDD output (`flutter-tdd`)

### Widget tests
- Home shows loading spinner then restaurant cards.
- Cart shows empty state when no items exist.

### Unit tests
- Cart use case computes totals correctly.
- Discount rules applied deterministically.

### Integration tests
- User can browse -> add item -> checkout.

---

## Sample code generated

```dart
import 'package:flutter/material.dart';

class RestaurantCard extends StatelessWidget {
  const RestaurantCard({
    super.key,
    required this.name,
    required this.deliveryEta,
    required this.onTap,
  });

  final String name;
  final String deliveryEta;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    return Card(
      child: ListTile(
        title: Text(name),
        subtitle: Text('ETA: $deliveryEta'),
        onTap: onTap,
      ),
    );
  }
}
```

## Sample test generated

```dart
import 'package:flutter_test/flutter_test.dart';

double calculateTotal(List<double> prices) =>
    prices.fold(0, (sum, item) => sum + item);

void main() {
  test('calculateTotal sums all items', () {
    expect(calculateTotal([4.5, 10.0, 2.5]), 17.0);
  });
}
```

---

## Build/deploy checklist (`flutter-build-deploy`)

- [ ] `flutter analyze` passes
- [ ] `flutter test` passes
- [ ] Android AAB generated
- [ ] iOS archive validation completed
