import sys
from antlr4 import *
from deliverable1_lexer import deliverable1_lexer
from deliverable1_parser import deliverable1_parser

def test_file(filename):
    input_stream = FileStream(filename, encoding='utf-8')

    lexer = deliverable1_lexer(input_stream)
    stream = CommonTokenStream(lexer)

    parser = deliverable1_parser(stream)

    tree = parser.start()

    print("Parse completed successfully.")
    print(tree.toStringTree(recog=parser))

def main():
    test_file("project_deliverable_1.py")
main()