from system.core.model import Model

class Moment(Model):
    def __init__(self):
        super(Moment, self).__init__()


    def cat(self, info):
        query = 'INSERT INTO categories (name) VALUES (%s)'
        data = [info['category']]
        return self.db.query_db(query, data)
    
    def get_cats(self):
		query = 'SELECT * FROM categories'
		return self.db.query_db(query)
     def create(self, info):
        query_moments = 'INSERT INTO moments (url, beg, end, categories_id, created_at) VALUES  '
        data = 
        query_plalist = 'INSERT INTO playlist (moments_id, users_id) VALUES ()'
        data_playlist = 