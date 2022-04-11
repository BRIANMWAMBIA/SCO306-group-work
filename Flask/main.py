
from flask import Flask, request, abort
from flask_restful import Resource, Api,reqparse,fields, marshal_with

app = Flask(__name__)
api = Api(app)


POSTS = {
    'post1': {'post': 'build an API'},
    'post2': {'post': '?????'},
    'post3': {'post': 'profit!'},
}

def abort_if_post_doesnt_exist(post_id):
    if post_id not in POSTS:
        abort(404)


parser = reqparse.RequestParser()
parser.add_argument('post')

#Todo
class Post(Resource):
    def get(self, post_id):
    	abort_if_post_doesnt_exist(post_id)
    	return POSTS[post_id]
    	
    def put (self, post_id):
    	args = parser.parse_args()
    	post={'post':args['post']}
    	POSTS[post_id]=post
    	return task, 201
   
    def delete(self, post_id):
        abort_if_post_doesnt_exist(post_id)
        del POSTS[post_id]
        return '', 204

      
    	
#TODOLIST
class PostList (Resource):
	def get(self):
		return POSTS 

	def post(self):
		args=parser.parse_args()
		todo_id=int(max(POSTS.keys()).lstrip('post')) + 1  
		post_id = 'post%i' % post_id  
		POSTS[post_id] = {'post': args['post']}
		return POSTS[post_id], 201

api.add_resource(PostList, '/posts')
api.add_resource(Post, '/posts/<post_id>')
if __name__ == '__main__':
    app.run(debug=True)