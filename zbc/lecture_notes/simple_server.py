import who_am_i
from flask import Flask


my_app = Flask(__name__)


@my_app.route('/')
def hello():
    my_ip = who_am_i.get_my_ip()
    return f'Hej from {my_ip}!'


if __name__ == '__main__':
    my_app.run(host='0.0.0.0')


# 10.50.137.35
# 10.50.136.232
# 10.50.130.46
# 10.50.137.11
# 10.50.130.73
# 10.50.138.89
