import webbrowser

import sys


def run_sample():
    edgeExecutablePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    print(f'Путь к исполняемому файлу MS Edge: {edgeExecutablePath}')
    edgeBrowserInstance = webbrowser.BackgroundBrowser(edgeExecutablePath)
    webbrowser.register(name='edge', klass=None, instance=edgeBrowserInstance, preferred=False)

    try:
        inst = webbrowser.get('edge')
        inst.open_new("http://yandex.ru")  # Открыть страницу http://yandex.ru в браузере MS Edge
    except TypeError:
        type, value, traceback = sys.exc_info()
        print(f'Error occured:\r\n\ttype: {type}\r\n\tvalue: {value}\r\n\ttraceback = {traceback}')

    webbrowser.open_new("http://python.org")
