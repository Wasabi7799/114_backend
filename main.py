from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

class MyHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # 指定服務的目錄為 'public'
        super().__init__(*args, directory='public', **kwargs)
    def do_GET(self):
        # 如果請求的路徑是根目錄 '/'
        if self.path == '/':
            # 將路徑變更為 'mainpage.html'
            self.path = 'main_page.html'
        
        # 執行父類別的 GET 方法來處理請求
        return super().do_GET()

# Define the server address and port
HOST = '0.0.0.0'
PORT = 8000

# Create a handler to manage requests
#Handler = SimpleHTTPRequestHandler

# Create the server object
httpd = HTTPServer((HOST, PORT), MyHandler)

# Function to run the server
def run_server():
    print(f"Serving HTTP on {HOST} port {PORT} (http://localhost:{PORT}/) ...")
    print("Type 'stop' to shut down the server...")
    httpd.serve_forever()

# Create and start the server in a separate thread
server_thread = threading.Thread(target=run_server)
server_thread.daemon = True  # This allows the main program to exit even if the thread is still running
server_thread.start()

# Main thread waits for user input
try:
    while True:
        command = input()
        if command.lower() == 'stop':
            print("Shutting down the server...")
            httpd.shutdown()  # This method shuts down the server
            break
        else:
            print("unknown command...")
except KeyboardInterrupt:
    print("Shutting down the server...")
    httpd.shutdown()