import pytest

def test_fetch_data(jpy_analyzer):

    jpy_analyzer.fetch_data()
    print(jpy_analyzer.data)
    assert jpy_analyzer.data

@pytest.mark.skip()
def test_send_to_line(jpy_analyzer):
    jpy_analyzer._send_to_line('test')