import web

urls = ( '/', 'index' )

class index:
    def GET(self):
        render = web.template.render('./')

        return render.index()

        
    
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


    with open(myfile) as f:



