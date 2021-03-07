import io
import sys
import argparse
from csv_transformer.csv_transformer import CsvTransformer, TransfomerParameters


class TransformArgumentParser():

    def parse_parameters(self, args):
        # コマンドライン引数の処理
        parser = argparse.ArgumentParser()
        
        # 使用するテンプレートと処理するcsvファイル
        # jinja2 template to use.
        parser.add_argument('template', help='jinja2 template to use.')
        parser.add_argument('csv', help='transform csv.')
        parser.add_argument('key_values', nargs='*', help='additional values [KEY=VALUE] format.', action=KeyValuesParseAction)
        # flag first line is header
        parser.add_argument('-H', '--header', help='first line is header.', action='store_true')
        # flag tab separate values
        parser.add_argument('-T', '--tab', help='tab separate values.', dest='delimiter', default=',', action=DelimiterSelectAction)
        # source encoding
        parser.add_argument('--input-encoding', metavar='enc', help='file encoding.', default='utf-8')
        # output file (default stdout)
        parser.add_argument('-O', '--output', metavar='file', help='output file.', nargs=1)

        options = TransfomerParameters()
        parser.parse_args(args=args, namespace=options)

        return options

    # def parse_addtional(self, values):
    #     addtional = {}
    #     for value in values:
    #         key_value = value.split('=')
    #         addtional[key_value[0]] = key_value[1]
    #     return addtional

class KeyValuesParseAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, self.parse_key_values(values))

    def parse_key_values(self, values):
        key_values = {}
        for value in values:
            key_value = value.split('=')
            key_values[key_value[0]] = key_value[1]
        return key_values

class DelimiterSelectAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string):
        delimiter = ''
        if option_string == '-T' or option_string == '--tab':
            delimiter = '\t'

        setattr(namespace, self.dest, delimiter)

if __name__ == '__main__':
    # windows対策
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
