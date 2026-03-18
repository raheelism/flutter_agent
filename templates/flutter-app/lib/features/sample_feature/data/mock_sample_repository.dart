import '../domain/sample_item.dart';
import '../domain/sample_repository.dart';

class MockSampleRepository implements SampleRepository {
  @override
  Future<List<SampleItem>> fetchItems() async {
    return const <SampleItem>[
      SampleItem(id: '1', name: 'Sample item'),
    ];
  }
}
