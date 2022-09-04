# --------------------
# This file is used for defining Ttk styles.
# Use the 'style' object to define styles.

# Pygubu Designer will need to know which style definition file
# you wish to use in your project.

# To specify a style definition file in Pygubu Designer:
# Go to: Edit -> Preferences -> Ttk Styles -> Browse (button)

# In Pygubu Designer:
# Assuming that you have specified a style definition file,
# - Use the 'style' combobox drop-down menu in Pygubu Designer
#   to select a style that you have defined.
# - Changes made to the chosen style definition file will be
#   automatically reflected in Pygubu Designer.
# --------------------

# Example code:

# Left menu config
style.configure('Sphinx_M.TFrame', background='#0A507A')
style.configure('Sphinx_M.TLabel', background='#0A507A',
                font=('helvetica', 12, 'bold'),
                foreground='#ffffff')

style.configure('Sphinx_M.TButton',
                relief="flat",
                background='#FFFFFF',
                font=('helvetica', 12))

# Right area config
style.configure('Sphinx_R.TFrame', background='#eeeeee')
style.configure('Sphinx_R.TLabel', background='#eeeeee',
                font=('helvetica', 12, 'bold'),
                foreground='#000000')

style.configure('Sphinx_R.TButton',
                relief="flat",
                # relief="raised",
                background='#777777',
                foreground='#FFFFFF',
                font=('helvetica', 10),
                activebackground='#555555',
                activeforground='#FF0055',
                highlightbackground='#222222',
                highlightforeground='#FF0055',
                )

style.map("Sphinx_R.TButton",
    foreground=[('pressed', '#FFFFFF'), ('active', '#FFFFFF')],
    background=[('pressed', '!disabled', '#555555'), ('active', '#444444')]
    )