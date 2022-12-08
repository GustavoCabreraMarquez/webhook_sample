from json import dumps

from httplib2 import Http


def main():
    url = 'https://your_webhook_link.com'
    bot_message = {
        'text': 'This is a webhook from a python file'}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    print(response)


if __name__ == '__main__':
    main()

