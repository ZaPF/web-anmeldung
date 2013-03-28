from bottle import ServerAdapter

class CustomWSGIRefServer(ServerAdapter):
    def run(self, handler): # pragma: no cover
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        import socket
        from sys import stderr
        class LogHandler(WSGIRequestHandler):
            def log_message(self, format, *args):
                """ This loggs the host found in X-Forwarded-For instead of the client host.

                This is a combination of
                https://github.com/defnull/bottle/blob/master/bottle.py#L2498
                and https://github.com/python-git/python/blob/master/Lib/BaseHTTPServer.py#L427
                """
                host = self.headers.get('X-Forwarded-For', '')
                host = socket.getfqdn(host) if host else self.address_string()
                stderr.write("%s - - [%s] %s\n" %
                                 (host,
                                  self.log_date_time_string(),
                                  format%args))
        self.options['handler_class'] = LogHandler
        srv = make_server(self.host, self.port, handler, **self.options)
        srv.serve_forever()

