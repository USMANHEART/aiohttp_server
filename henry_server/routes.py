import aiohttp_cors
from aiohttp import web
from henry_tools import (
    get_test, post_test, today_task, save_task
)


def start_services():
    print("Starting services")
    app = web.Application()
    add_route = app.router.add_route
    header = {
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers=("X-Custom-Server-Header","Access-Control-Allow-Origin"),
                allow_headers=("X-Requested-With", "Content-Type", "Access-Control-Allow-Origin"),
                max_age=3600,
            )
    }
    GET = 'GET'
    POST = 'POST'

    # app.router.add_get('/today_task', today_task)
    # app.router.add_get('/get_test', get_test)
    #
    # app.router.add_post('/save_task', save_task)
    # app.router.add_post('/post_test', post_test)

    ######################
    add_route(GET, '/today_task', today_task, name='today_task')
    add_route(GET, '/get_test', get_test, name='get_test')

    add_route(POST, '/save_task', save_task, name='save_task')
    add_route(POST, '/post_test', post_test, name='post_test')
    ########################

    cors = aiohttp_cors.setup(app)
    for route in list(app.router.routes()):
        cors.add(route, header)
    web.run_app(app)
    return app
