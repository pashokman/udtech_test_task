def test_example2(setup):
    home_page = setup
    home_page.navigate()
    login_page = home_page.build_for_free_btn_click()
    workout_editor_page = login_page.login("jason1tester1@gmail.com", "JE4Ys2K523")
    workout_editor_page.tablet_info_window_ok_button_click()
    workout_editor_page.check_builder_visibility()
    workout_editor_page.log_out()
