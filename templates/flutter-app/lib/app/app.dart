import 'package:flutter/material.dart';

import 'router.dart';
import 'theme.dart';

class TemplateApp extends StatelessWidget {
  const TemplateApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      title: 'Flutter Superpowers Template',
      theme: buildAppTheme(),
      routerConfig: buildRouter(),
    );
  }
}
