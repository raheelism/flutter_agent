import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import '../features/sample_feature/presentation/sample_screen.dart';

GoRouter buildRouter() {
  return GoRouter(
    routes: <RouteBase>[
      GoRoute(
        path: '/',
        builder: (BuildContext context, GoRouterState state) {
          return const SampleScreen();
        },
      ),
    ],
  );
}
