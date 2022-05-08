from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    """Main program"""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_to_height = {"James": "2.03m", "Curry": "1.93m", "Morant": "1.9m"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_w.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.name_to_height:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.text
        self.status_text = "{}'s height is {}".format(name, self.name_to_height[name])

    def clear_all(self):
        self.root.ids.entries_box.clear_widgets()


DynamicWidgetsApp().run()
