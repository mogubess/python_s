import contextlib

# contextlib.ExitStack() 内で最後に、stack.pop_all()がコールされない
# 場合は、stack.callbackに登録された関数が実行される、
# エラーハンドリングに最適


def is_ok_job():
    try:
        print('do somthing')
        #raise Exception('error')
        return True
    except Exception:
        return False


def cleanup():
    print('clean up')


def cleanup2():
    print('clean up2')


with contextlib.ExitStack() as stack:
    stack.callback(cleanup)
    stack.callback(cleanup2)

    @stack.callback
    def cleanup3():
        print('clean up3')

    is_ok = is_ok_job()
    print('more task')

    if is_ok:
        stack.pop_all()
