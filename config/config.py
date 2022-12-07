xpaths = {"username": "/html/body/div[1]/form/div[1]/input", "password": "/html/body/div[1]/form/div[2]/input",
          "login_button": "/html/body/div[1]/form/button", "trigger_folder": "/html/body/section[2]/ul/li[1]/div/a[13]/i[1]",
          "new_scan": "html body section#layout section#titlebar a#new-scan.button.floatright.secondary",
          "host_discovery": "html body section#layout section#content section div.mt10 div.category-templates div.library a.library-item",
          "name": "html body section#layout section#content section div.mt10 div.category-templates div.library a.library-item",
          "description": "html body section#layout section#content section div.mt10 div.category-templates div.library a.library-item",
          "target": "html body section#layout section#content section div.mt10 div.category-templates div.library a.library-item",
          "dropdown": "html body section#layout section#content section div.mt10 div.category-templates div.library a.library-item",
          "save_and_launch": "html body section#layout section#content section div.mt10 div.category-templates div.library a.library-item"
          }

# return the xpaths dictionary from a function
def get_xpaths():
    return xpaths