#import numpy as np
import os
import sys





##Example input python ask.py article.txt nquestions

if __name__ == '__main__':

    article_file = sys.argv[1]
    num_ques     = int(sys.argv[2])

    with open(article_file, "r") as f:
        print(f.read())

    #print(num_ques, article_file)
