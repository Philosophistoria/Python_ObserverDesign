def receive_notification_by(func, attr_res='all', timing_res='pre/post', funcreqarg=False):
    def observer_func(attr, timing):
        if (attr_res == 'all' or attr in attr_res) and timing in timing_res:
            if funcreqarg:
                func(attr,timing)
            else:
                func()
    return observer_func