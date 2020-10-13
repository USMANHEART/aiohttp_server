
def set_status(status_passed=1, msg="Success!", error=False):
    _dict = {'status': status_passed, 'msg': msg}
    if error:
        _dict['status'] = 0
        _dict['msg'] = "Failed!"
    return _dict
