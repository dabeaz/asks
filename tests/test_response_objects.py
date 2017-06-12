import asks.response_objects

def test_response_repr():
    r = asks.response_objects.Response('ascii', status_code=200, reason_phrase="Meh")
    assert repr(r) == '<Response 200 Meh>'

def test_response_guess_encoding():
    r = asks.response_objects.Response('ascii', headers={'content-type': 'text/plain; charset=utf-8'})
    r._guess_encoding()
    assert r.encoding == 'utf-8'

    r = asks.response_objects.Response('ascii', headers={'content-type': 'text/plain'})
    r._guess_encoding()
    assert r.encoding == 'ascii'

    r = asks.response_objects.Response('ascii', headers={})
    r._guess_encoding()
    assert r.encoding == 'ascii'
