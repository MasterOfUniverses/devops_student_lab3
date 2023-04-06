from tornado.web import RequestHandler, Application
import sympy


def fibonacchi_mod(pos: int) -> str:
    i = 1
    nums = [1, 1]
    while i < pos:
        i += 1
        nums = [nums[1], nums[0] + nums[1]]
    c = str(nums[0])
    if pos == 0:
        c = '0'
    elif pos == -1:
        c = '#'
    return c


def prime_mod(pos: int, force: int) -> str:
    if force == 0:
        if pos > 1000000000:
            return """please, enter number smaller then 1 000 000 000
or use force-mode /P/n (if you really want to wait so long)"""
    if pos > 0:
        c = str(sympy.prime(pos))
    else:
        c = '#'
    return c


class MainHandler(RequestHandler):
    def get(self, data: str) -> None:
        data = str(data)
        mode = data[0]
        if mode == 'f':
            pos = data[2:]
            int_pos = int(pos) - 1
            result = fibonacchi_mod(int_pos)
            self.write({"num": result})
        elif mode == 'p':
            pos = data[2:]
            int_pos = int(pos)
            result = prime_mod(int_pos, 0)
            self.write({"num": result})
        elif mode == 'P':
            pos = data[2:]
            int_pos = int(pos)
            result = prime_mod(int_pos, 1)
            self.write({"num": result})
        else:
            self.write({"hello": """"please, write in address bar /f/n
or /p/n to get n-th fibonacchi or prime number""",
                        "warning":
                        """you can try to calculate n-th prime number
with n>=1 000 000 000 but it is too long and if you really want to do
it enter in address bar /P/n"""
                        })


app = Application([(r"/([f|p|P]/[0-9]+)?", MainHandler)])
