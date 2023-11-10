import asyncio
import json
import time
import websocket
import threading

WS_URL = "ws://89.58.53.238:51155"


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(f"Error: {error}")


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


async def send_stop(ws: websocket.WebSocketApp):
    jdata = {"stop_immediately": True}
    time.sleep(5)
    ws.send(json.dumps(jdata).encode("utf-8"))


def on_open(ws):
    def run(*args):
        while True:
            # data = "骁龙 8 Gen 3 芯片相较于骁龙 8 Gen 2 芯片有哪些改进和提升？"#
            data = input("Please enter a message (or 'exit' to close): ")
            # asyncio.create_task(send_stop(ws))
            if data == "exit":
                ws.close()
                # break
            jdata = {
                "message": data,
                "doc_range": {"category": "", "b_type": [], "ids": ["doc_id_666"]},
                "is_summary": False,
            }
            ws.send(json.dumps(jdata).encode("utf-8"))

            ###################
            # 等待十秒 发送一个停止信号
            """ time.sleep(10)
            # 发送停止消息
            print("send stop")
            stop_message = {"stop_immediately": True}
            ws.send(json.dumps(stop_message).encode("utf-8"))  """
            ###################

    threading.Thread(target=run).start()


if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        WS_URL,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    ws.run_forever()
