import 'package:flutter/material.dart';

class SampleScreen extends StatelessWidget {
  const SampleScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Sample Feature')),
      body: const Center(
        child: Text('Replace with feature-specific widgets and state wiring.'),
      ),
    );
  }
}
