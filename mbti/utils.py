#-*- coding:utf-8 -*-
from __future__ import unicode_literals

import os
from collections import Counter

from more_itertools import flatten

from models import QUESTIONS, TYPES_DESC


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


if __name__ == '__main__':
    assert 'ISFP' == get_result(['I', 'S', 'F', 'P'])
    assert len(get_questions()) == 72
    assert len(get_types_desc()) == 16
