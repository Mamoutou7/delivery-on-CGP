"""
Created by Mamoutou Fofana
November, 3, 2023

"""

import main

def test_index():
    main.app.Testing = True
    client = main.app.test_client()

    res = client.get('/')
    assert res.status_code == 200
    assert 'Hello World' in res.data.decode('utf-8')