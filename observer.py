def receive_notification_by(func, attr_res='all', timing_res='pre/post', funcreqarg=0):
    def observer_callback(retval, attr_name, timing, *arg, **kwarg):
        # argset: =(attr_name, timing, retval)
        if (attr_res == 'all' or attr_name in attr_res) and timing in timing_res:
            if funcreqarg==2:
                func(retval, attr_name, timing)
            elif funcreqarg==1:
                func(retval)
            else:
                func()
    return observer_callback

if __name__ == "__main__":
    f1 = receive_notification_by(print,'write','post',True)
    f2 = receive_notification_by(print,'read','pre',True)
    print(f1)
    f1(0, 'write','post')    # to be executed
    f2(1, 'read','pre')      # to be exectuted
    f2(2, 'read','post')     # not to be exectuted
    f1(3, 'read','post')     # not to be exectuted