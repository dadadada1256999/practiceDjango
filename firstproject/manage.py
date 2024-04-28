#!/usr/bin/env python
"""最初に実行されるファイル"""
import os
import sys


def main():
    """Run administrative tasks."""
    # 環境変数にプロジェクトの設定を設定(settings.pyが読み込まれる)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # 以下が実行されるとプロジェクトの設定ファイルが読み込まれ、指定されたコマンドが検索されコマンドを実行する流れ
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
