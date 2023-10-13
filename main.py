import threading

import ATRHandler
import utils
from atr_cmd import AtrCmd
from daemon import Daemon
import os

if __name__ == '__main__':
    utils.get_client_id()  # creates necessary config before launch
    server = Daemon(('127.0.0.1', 1234), ATRHandler.ATRHandler)
    threading.Thread(target=server.serve_forever).start()
    atrcmd = AtrCmd()
    atrcmd.do_time(line='10')
    download_folder_path = os.environ['download_folder_path']
    if not download_folder_path:
        atrcmd.do_download_folder(line=f'{download_folder_path}')

    streamer = os.environ['streamer'].split(';')
    if len(streamer) > 0:
        for s in streamer:
            str_cmd = f'{s} best'
            print(str_cmd)
            atrcmd.do_add(line=str_cmd)

    atrcmd.do_list(line='list')
    atrcmd.do_start(line='start')
    atrcmd.cmdloop_with_keyboard_interrupt()
