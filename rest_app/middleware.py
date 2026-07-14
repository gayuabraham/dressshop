class simpleMiddleware:
    def __init__(self , response):
        self.response = response
    def __call__(self, request):
        print("before view")
        result = self.response(request)
        print("after view")
        return result
        
        