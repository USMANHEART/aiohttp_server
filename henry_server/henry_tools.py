from aiohttp import web
from db_utils import fetchall, fetchone
from henry_api import set_status
import json


async def today_task(request):
    print("Request Received")
    tasks = ""
    e = set_status()
    import datetime
    today = datetime.datetime.now()
    today = today.date()

    try:
        _sql = 'SELECT task FROM `task_manager` WHERE date="{today}" LIMIT 1;'.format(today=today)
        result = fetchone(_sql)
        print(result)
        if result:
            tasks = result
    except Exception as Ex:
        e = set_status(0, str(Ex))
    e['tasks'] = tasks
    return web.json_response(e)


async def save_task(request):
    post_json = await request.json()
    tasks = post_json.get('tasks')
    tasks = str(tasks)
    _id = 0
    e = set_status()

    import datetime
    today = datetime.datetime.now()
    today = today.date()

    try:
        _sql = 'SELECT `id` FROM `task_manager` WHERE `date` = "{today}" LIMIT 1;'.format(today=today)
        result = fetchone(_sql)
        if result:
            _id = int(result)
        if _id == 0:
            _sql = 'INSERT INTO `task_manager` (`task`, `date`) VALUES ("{tasks}", "{today}")'.\
                format(tasks=tasks, today=today)
        else:
            _sql = 'UPDATE `task_manager` SET `task`="{tasks}", `date`="{today}" WHERE `id`={id}'.\
                format(tasks=tasks, today=today, id=_id)
        result = fetchone(_sql)
        print(result)
    except Exception as Ex:
        e = set_status(0, str(Ex))
    return web.json_response(e)


async def get_test(request):
    try:
        response_obj = {'status': 1, "msg": "API is working"}
        return web.Response(text=json.dumps(response_obj))
    except Exception as e:
        response_obj = {'status': 0, 'reason': str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)


async def post_test(request):
    try:
        value = request.query['value']
        response_obj = {'status': 1, "value": value}
        return web.json_response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj = {'status': 0, 'reason': str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)
