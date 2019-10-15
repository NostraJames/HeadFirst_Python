from httplib2 import Http
from json import dumps

#
# Hangouts Chat incoming webhook quickstart
#
def main():
    url = 'https://hangouts.google.com/webchat/u/0/frame?v=1569446403&hl=en&pvt=AMP3uWYO-vW7eN0pdxhRFEolDuZokVkii8MfsAOC9JQKDr4tySfmwaBRlmoVse5BgDro_sojoMzg9TlgtvvYv6wg--94AZ0myQ%3D%3D&prop=gmail#tgtn_42oo9j'
    bot_message = {
        'text' : 'Hello from Python script!'}

    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

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

