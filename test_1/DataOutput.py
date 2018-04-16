
class DataOutput(object):
    def __init__(self):
        self.datas=[]
    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    def output_html(self):
        html=open('baike.html','w',encoding='utf-8')
        html.write("<html>")
        html.write("<head><meta charset='utf-8'/></head>")
        html.write("<body>")
        html.write("<table border='1'>")
        for data in self.datas:
            html.write("<tr>")
            html.write("<td>%s</td>" % data['url'])
            html.write("<td>%s</td>" % data['title'])
            html.write("<td>%s</td>" % data['summary'])
            html.write("</tr>")
        html.write("</table>")
        html.write("</body>")
        html.write("</html>")
        html.close()