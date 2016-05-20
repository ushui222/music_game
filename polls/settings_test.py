# -*- coding:utf-8 -*-
from polls.settings import *
import os

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
#�J�o���b�W���|�[�g(html)���o�͂���t�H���_���w��
COVERAGE_REPORT_HTML_OUTPUT_DIR = '.cover'

# �e�X�g���s���̈����̐ݒ�(nose�̈���)
NOSE_ARGS = [
    '--with-xunit',
    '--with-coverage',
    '--cover-xml',
    '--cover-html',
    '--cover-package=polls', #�e�X�g���s��app�����w��
]

#�e�X�g�p��B���̐ݒ�(settings.py��DB���ƕ����Ă���)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test.db'),
    }
}
