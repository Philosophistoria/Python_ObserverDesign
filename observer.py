def receive_notification_by(func, attr_res='all', timing_res='pre/post', funcreqarg=False):
    def observer_callback(retval, attr_name, timing, *arg, **kwarg):
        # argset: =(attr_name, timing, retval)
        if (attr_res == 'all' or attr_name in attr_res) and timing in timing_res:
            if funcreqarg:
                func(retval, attr_name, timing)
            else:
                func()
    return observer_callback

if __name__ == "__main__":
    f1 = receive_notification_by(print,'write','post',True)
    f2 = receive_notification_by(print,'read','pre',True)
    print(f1)
    f1('write','post',0)    # to be executed
    f2('read','pre',2)      # to be exectuted
    f2('read','post',4)     # not to be exectuted