#-*- coding:utf-8 -*-
from __future__ import unicode_literals

import os
import threading
from collections import Counter

from more_itertools import flatten

from models import QUESTIONS, TYPES_DESC

# 完成测试的人数锁
tested_count_lock = threading.Lock()


def get_questions():
    '''获取题目'''
    questions = []
    for question in QUESTIONS:
        questions.append({
            'question': question['q'],
            'choice_a': {
                'value': question['t1'],
                'text': question['a1']
            },
            'choice_b': {
                'value': question['t2'],
                'text': question['a2']
            }
        })
    return questions


def get_result(answers):
    '''计算测试结果
    E-I S-N T-F J-P
    '''
    types = [('E', 'I'), ('S', 'N'), ('T', 'F'), ('J', 'P')]
    answers = Counter(answers)
    if set(answers.keys()) - set(flatten(types)):
        raise Exception('TypesError', 'answer type is not in types')
    result = ''.join(t1 if answers.get(t1, 0) > answers.get(t2, 0) else t2
                     for t1, t2 in types)
    return result


def get_types_desc():
    '''十六种人格简要描述'''
    return sorted(TYPES_DESC.items(), key=lambda i: i[0])


def get_tested_count():
    '''获取完成测试的人数'''
    try:
        root_path = os.path.dirname(os.path.dirname(
            os.path.realpath(__file__)))
        tested_count_file = os.path.join(root_path, 'tested_count.txt')
        with open(tested_count_file) as txt:
            count = int(txt.read().strip())
            return count
    except Exception as e:
        print(e)
        return 0


def incr_tested_count():
    '''完成测试人数 +1'''
    tested_count_lock.acquire()
    try:
        root_path = os.path.dirname(os.path.dirname(
            os.path.realpath(__file__)))
        tested_count_file = os.path.join(root_path, 'tested_count.txt')
        count = 1
        if os.path.isfile(tested_count_file):
            count = get_tested_count() + 1
        with open(tested_count_file, "w") as txt:
            txt.write(str(count))
    except Exception as e:
        print(e)
    finally:
        tested_count_lock.release()


if __name__ == '__main__':
    assert 'ISFP' == get_result(['I', 'S', 'F', 'P'])
    assert len(get_questions()) == 72
    assert len(get_types_desc()) == 16
