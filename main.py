from nicegui import ui

ui.label('Welcome to My NiceGUI Web App!')

ui.button('Click Me', on_click=lambda: ui.notify('Hello, GitHub Pages!'))

ui.run(title='My NiceGUI App')
