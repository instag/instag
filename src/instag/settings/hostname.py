# -*- coding: utf-8 -*-

def _get_hostname_socket():
    """
    0.006 秒ぐらいだが不安定。
    環境によってはhostnameがとれないことがある
    どんな値が返ってきているかは、実際にこのコードをインポートしてコールしてみること
    """
    try:
        import socket
        bulk = socket.gethostbyaddr(socket.gethostname())[0]
        return bulk.strip().lower()
    except:
        return ''


def _get_hostname_shell():
    """
    0.008 秒ぐらいで安定。
    Windowsでは多分動作しない。
    どんな値が返ってきているかは、hostname コマンドを実行してみること
    """
    try:
        import subprocess
        bulk = subprocess.Popen(['hostname'], stdout=subprocess.PIPE).communicate()[0].strip()
        return bulk.strip().lower()
    except:
        return ''

if not 'HOSTNAME' in vars():
    HOSTNAME = _get_hostname_shell()
