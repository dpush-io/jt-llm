import json
import websocket
import threading

WS_URL = "ws://0.0.0.0:8888" #replace with your url

def on_message(ws, message):
    print(message, end="")
     

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        while True:
            data = input("Please enter a message (or 'exit' to close): ")
            if data == 'exit':
                ws.close()
                break
            jdata = {"message": data, "doc_range": {"category":"jtreal1", "b_type":["公路业务","养护服务"]}, "is_summary": False, }
            ws.send(json.dumps(jdata).encode("utf-8"))
    threading.Thread(target=run).start()

if __name__ == "__main__":
    #websocket.enableTrace(True)
    ws = websocket.WebSocketApp(WS_URL,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
