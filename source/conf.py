# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Brass' de l'Eyre"
copyright = "2024, Brass' de L'Eyre"
author = 'Vincent Deguin'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

comments_config = {
   "utterances": {
      "repo": "https://github.com/BrassdelEyre/SP-BrassdelEyre",
      "optional": "config",
   }
}

comments_config = {
   "hypothesis": True
}



extensions = [
  
  "myst_parser",
  "sphinx_design",
  "sphinx_comments",
  "sphinx_new_tab_link",
  "sphinx_book_theme",
  "sphinx_togglebutton",
  "sphinx_thebe",
]

myst_enable_extensions = ["colon_fence", "linkify", "substitution"]
myst_heading_anchors = 2



templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_logo = "_static/Logo/logo-Vince.svg"
html_favicon = "_static/Logo/logo-Vince.svg"
html_static_path = ['_static']

html_theme_options = {
    "external_links": [
        {
            "url": "https://BrassdelEyre.github.io/jb-asso/_build/html/",
            "name": "&nbsp &nbsp &nbsp &nbsp 📃 L'Asso",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://BrassdelEyre.github.io/jb-brasserie/_build/html/",
            "name": "&nbsp &nbsp &nbsp &nbsp 💪 La Brasserie",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://BrassdelEyre.github.io/jb-bieres/_build/html/intro.html",
            "name": "&nbsp &nbsp &nbsp &nbsp 🍺 Les Bières",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://BrassdelEyre.github.io/jb-evenements/_build/html/intro.html",
            "name": "&nbsp &nbsp &nbsp &nbsp  🎉 Les Evenements",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://BrassdelEyre.github.io/jb-culture/_build/html/intro.html",
            "name": "&nbsp &nbsp &nbsp &nbsp 🎓 La Culture",
            "attributes": {"target": "_blank"},
        },
    ],
    "header_links_before_dropdown": 7,    
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/BrassdelEyre/SP-BrassdelEyre",
            "icon": "fa-brands fa-github",
        },
    ],
    

    "logo": {
        "text": " &nbsp Brass' de L'Eyre &nbsp &nbsp &nbsp",
        "image_dark": "_static/Logo/logo-Vince.svg",
        "alt_text": " &nbsp Pharmacie &nbsp &nbsp",
    },
    
    
    "navbar_start": ["navbar-logo"],
    
}


html_css_files = ["css/custom_style.css", "css/slider.css"]
html_js_files = ["_static/assets/scripts/slider-script.js"]

    
