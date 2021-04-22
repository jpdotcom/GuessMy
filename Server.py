from http.server import HTTPServer, BaseHTTPRequestHandler
import TrainedModel2 as tm2
import threading
import TrainedModel1 as tm1
class Server(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        file_name=None
        
        if self.path=='/numbers.html' or self.path=='/numbers.css':
            file_name='pages_1'+self.path
        elif self.path=='/clothes.html' or self.path=='/clothes.css':
            file_name='pages_2'+self.path
        print(file_name)
        
        try:
            file_to_get=open(file_name).read()
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

        ans=None
        if self.path=='/getNumbers':
            ans=tm1.predict(post_data)
           
        elif self.path=='/getClothes':

            ans=tm2.predict(post_data)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(ans, 'utf-8'))

    
    
        
httpd=HTTPServer(('localhost',8080),Server)


httpd.serve_forever()


