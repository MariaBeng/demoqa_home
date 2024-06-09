from pages.swag_labs import SwagLabs

def test_check_swag(browser):
    demo_qa_page = SwagLabs(browser)
    demo_qa_page.visit()
    demo_qa_page.exist_icon()
    demo_qa_page.exist_username()
    demo_qa_page.exist_password()
    assert demo_qa_page.exist_icon()
    assert demo_qa_page.exist_username()
    assert demo_qa_page.exist_password()