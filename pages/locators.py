class Locators:

    # header section locators
    header_sign_up_link_text = "Sign up"
    header_sign_up_link_css = "a[href*='signup']"

    # Sign up section locators
    sign_up_learner_button_xpath = "//button[text()='Learner']"
    month_birthday_picker_dropdown_id = "monthBirthdayPickerDropdown"
    day_birthday_picker_dropdown_id = "dayBirthdayPickerDropdown"
    year_birthday_picker_dropdown_id = "yearBirthdayPickerDropdown"
    sign_up_with_email_button_xpath = "//button[@data-test-id='sign-up-with-email-button']"
    email_id = "uid-identity-text-field-1-your-parent-or-guardians-email"
    username_id = "uid-identity-text-field-2-choose-a-username"
    password_id = "uid-identity-text-field-3-create-a-password"
    sign_up_button_css = "button[data-test-id*='progress-shell-proceed-button']"
    personalize_ka_choose_grade_button_text = "//button[text()='Choose a grade to continue']"
    ka_popup_header_xpath = "//span[text()='Personalize Khan Academy']"