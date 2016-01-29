from system.core.controller import *
from flask import session
import math

class Moments(Controller):
    def __init__(self, action):
        super(Moments, self).__init__(action)
        self.load_model('Moment')

    def index(self):
        cats = self.models['Moment'].get_cats()
        return self.load_view('success.html', cats = cats)

    def add(self):
        beg = request.form['beg']
        print beg
        begInt = int(float(beg))

        print type(begInt)

        data = {
            'category':     request.form['category'],
            'beg':          int(float(request.form['beg'])),
            'end':          int(float(request.form['end'])),
            'url':          request.form['url']
        }
        test = self.models['Moment'].create(data)
        return jsonify(test=test)

    def category(self):
        data = {'category': request.form['category']}
        self.models['Moment'].cat(data)
        return redirect('/moments/add')

    def cat(self, id):
        cats = self.models['Moment'].get_cats()
        # catId = request.form['cat']
        # print catId
        list = self.models['Moment'].get_by_cat(id)
        listURLs = []
        for item in list:
            listURLs.append('https://www.youtube.com/embed/' + item['url'] + '?start=' + item['beg'] + '&end=' + item['end'] )
            print listURLs
        return self.load_view('cat.html', list = listURLs, cats = cats)