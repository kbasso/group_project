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
        query_moments = 'INSERT INTO moments (url, beg, end, categories_id, created_at) VALUES (%s, %s, %s, SELECT id FROM categories WHERE name = %s, NOW()) '
        data_moments = [info['url'], info['beg'], info['end'], info['category']]
        self.db.query_db(query_moments, data_moments)

        query_mID = 'SELECT id FROM moments WHERE url = %s and beg=%s and end = %s'
        data_mID = [info['url'], info['beg'], info['end']]
        moment_id = self.db.query_db(query_mID, data_mID)

        query_plalist = 'INSERT INTO playlist (moments_id, users_id) VALUES (%s, %s)'
        data_playlist = [moment_id, session['userID']]
        
        return self.db.query_db(query_plalist, data_playlist)