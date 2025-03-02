import unittest
from chat_analysis import EmotionAnalyzer, OpenAIClient

class TestEmotionAnalyzer(unittest.TestCase):
    def setUp(self):
        self.openai_client = OpenAIClient(api_key='test_api_key')
        self.analyzer = EmotionAnalyzer(openai_client=self.openai_client)

    def test_analyze_emotions_by_date(self):
        conversations_by_date = {
            '2025-02-28': [
                'U08BTPRSAHZ: 今日はとても良い日でした。 (timestamp: 2025-02-28 08:00:00)',
            ],
        }
        result = self.analyzer.analyze_emotions_by_date(conversations_by_date)
        self.assertIn('2025-02-28', result)
        self.assertLessEqual(len(result['2025-02-28'].split('\n')), 2)

if __name__ == '__main__':
    unittest.main()