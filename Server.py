from http.server import HTTPServer, BaseHTTPRequestHandler
import TrainedModel as tm
import threading

class Server(BaseHTTPRequestHandler):
    
    def do_GET(self):
        add= '' if self.path=='/styles.css' else '.html'
        
        
        self.path='/pages/'+self.path+ add
        
        try:
            file_to_get=open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_get='File not found'
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_get,'utf-8'))
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        post_data=post_data.decode('utf-8')
        ans=tm.predict(post_data)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(ans, 'utf-8'))

    
    
        
httpd=HTTPServer(('localhost',8080),Server)


httpd.serve_forever()


