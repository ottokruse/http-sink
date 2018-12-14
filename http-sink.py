import datetime
import os
import socket

from jinja2 import Template
from sanic import Sanic
from sanic.exceptions import NotFound
from sanic.response import html

app = Sanic()
hostname = socket.getfqdn()


def get_request_html(request):
    template = Template(open('html_template.jinja2').read())

    return template.render({
        'headers': {
            header: request.headers[header]
            for header in sorted(request.headers)
        },
        'method': request.method,
        'url': request.url,
        'body': request.body or 'null',
        'hostname': hostname,
        'isodate': f'{datetime.datetime.utcnow().isoformat()}Z',
        'requester': f'{request.ip}:{request.port}',
    })


@app.exception(NotFound)
async def sink(request, exception):
    return html(get_request_html(request))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '80')))
