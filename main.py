from st_pages import Page, show_pages, add_page_title

add_page_title()

show_pages(
    [
        Page("ruble_analysis/main.py", "Курс рубля от даты", "💵"),
        Page("gitlab-users/main.py", "Пользователи гитлаб", "👥"),
        Page("test/main.py", "Эксперимент", "?"),
    ]
)
