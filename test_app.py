from app import app  

def test_header_is_present(dash_duo):
    dash_duo.start_server(app)
    
    dash_duo.wait_for_element("h1", timeout=10)
    header_text = dash_duo.find_element("h1").text
    
    assert header_text == "Soul Foods: Pink Morsel Sales Visualizer"

def test_visualization_is_present(dash_duo):
    dash_duo.start_server(app)
    
    dash_duo.wait_for_element("#sales-chart", timeout=10)
    
    assert True

def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(app)
    
    dash_duo.wait_for_element("#region-filter", timeout=10)
    
    assert True