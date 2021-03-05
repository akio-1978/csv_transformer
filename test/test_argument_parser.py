import unittest
from csvtransformer import TransformArgumentParser, TransfomerParameters


class ArgumentParserTest(unittest.TestCase):
    
    def test_minimum_args(self):
        params = TransformArgumentParser().parse_parameters(['template', 'csv'])
        
        self.assertEqual('template', params.template)
        self.assertEqual('csv', params.csv)
        self.assertFalse(params.header)

    def test_header(self):
        params = TransformArgumentParser().parse_parameters(['template', 'csv', '-H'])
        self.assertEqual('template', params.template)
        self.assertEqual('csv', params.csv)
        self.assertTrue(params.header)

        params = TransformArgumentParser().parse_parameters(['template', 'csv', '--header'])
        self.assertEqual('template', params.template)
        self.assertEqual('csv', params.csv)
        self.assertTrue(params.header)

    def test_encoding(self):
        params = TransformArgumentParser().parse_parameters(['template', 'csv'])
        self.assertEqual('template', params.template)
        self.assertEqual('csv', params.csv)
        self.assertEqual('utf-8', params.input_encoding)

        params = TransformArgumentParser().parse_parameters(['template', 'csv', '--input-encoding', 'sjis'])
        self.assertEqual('template', params.template)
        self.assertEqual('csv', params.csv)
        self.assertEqual('sjis', params.input_encoding)

    def test_key_values_action(self):
        params = TransformArgumentParser().parse_parameters(['template', 'csv', 'A=B', 'C=D'])
        
        self.assertEqual('template', params.template)
        self.assertEqual('csv', params.csv)
        self.assertFalse(params.header)
        self.assertEqual(params.key_values['A'], 'B')
        self.assertEqual(params.key_values['C'], 'D')

    def test_delimiter_comma_action(self):
        params = TransformArgumentParser().parse_parameters(['template', 'csv', 'A=B'])
        
        self.assertEqual('template', params.template)
        self.assertEqual('csv', params.csv)
        self.assertFalse(params.header)
        self.assertEqual(params.delimiter, ',')

    def test_delimiter_tab_action(self):
        params = TransformArgumentParser().parse_parameters(['template', 'csv', '-T' , 'A=B'])
        self.assertEqual('template', params.template)
        self.assertEqual('csv', params.csv)
        self.assertFalse(params.header)
        self.assertEqual(params.delimiter, '\t')

        params = TransformArgumentParser().parse_parameters(['template', 'csv', '--tab' , 'A=B'])
        self.assertEqual('template', params.template)
        self.assertEqual('csv', params.csv)
        self.assertFalse(params.header)
        self.assertEqual(params.delimiter, '\t')

if __name__ == '__main__':
    unittest.main()