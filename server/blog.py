from sanic import Blueprint
from sanic import response as res
from sanic.views import HTTPMethodView
from motor.motor_asyncio import AsyncIOMotorClient


blog = Blueprint('blog', url_prefix='/blog')

blog.static('/static', './static')


@blog.get('/blog/<id:int>')
async def blogPage(req, id):
    
    return await res.file('page/blog/blog.html')


class BlogAPI(HTTPMethodView):

    async def get(self, req, id):

        col = AsyncIOMotorClient().blog.blogs
        db_res = await col.find_one({}, {'_id':0})
        db_res['content'] = '大家撒六点就撒了'
        return res.json(db_res)

blog.add_route(BlogAPI.as_view(), '/api/blog/<id>')