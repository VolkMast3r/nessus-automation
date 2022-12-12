#!/usr/bin/python

# xpaths dictionary

xpaths = {"username": "/html/body/div[1]/form/div[1]/input",
          "password": "/html/body/div[1]/form/div[2]/input",
          "login_button": "/html/body/div[1]/form/button",
          "trigger_folder": "/html/body/section[2]/ul/li[1]/div/a[13]",
          "new_scan": "html body section#layout section#titlebar a#new-scan.button.floatright.secondary",
          "host_discovery": "html body section#layout section#content section div.mt10 div.category-templates div.library a.library-item",
          "name": "html body section#layout section#content section form div.content-block div#editor-tab-view div.hidden div.content.editor-content section div.editor-view.save.hidden div.editor-view-subsection.settings div.editor-settings-section div.form-group div input.editor-input.required",
          "description": "html body section#layout section#content section form div.content-block div#editor-tab-view div.hidden div.content.editor-content section div.editor-view.save.hidden div.editor-view-subsection.settings div.editor-settings-section div.form-group div textarea.editor-input",
          "target": "html body section#layout section#content section form div.content-block div#editor-tab-view div.hidden div.content.editor-content section div.editor-view.save.hidden div.editor-view-subsection.settings div.editor-settings-section div.form-group div textarea.editor-input.required",
          "start_scan": "",
          "folders": "html body section#layout section#content section form div.content-block div#editor-tab-view div.hidden div.content.editor-content section div.editor-view.save.hidden div.editor-view-subsection.settings div.editor-settings-section div.form-group div span.select2.select2-container.select2-container--nessus.select2-container--below.select2-container--focus span.selection"
          }

platcorp_subs = {
    "Eezy Track": "142",
    "Premier Credit Uganda": "127",
    "Platcorp Holdings": "148",
    "Momentum Credit":  "139",
    "Premier Credit Kenya": "136",
    "Platinum Credit Tanzania": "119",
    "Viva 365 Insurance Brokers": "145",
    "Platinum Credit Kenya": "121",
    "Fanikiwa Microfinance Limited": "133",
    "Platinum Credit Uganda": "124",
}

# return the xpaths dictionary from a function
def get_xpaths():
    return xpaths

# return the platcorp_subs dictionary from a function
def get_platcorp_subs():
    return platcorp_subs
