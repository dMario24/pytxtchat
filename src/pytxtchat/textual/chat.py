from textual import on
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Container, Vertical
from textual.widgets import Input, RichLog, Button
from textual.widgets import Header, Footer


class HomeScreen(Screen):
    
    def compose(self) -> ComposeResult:
        yield Container(
            Button("Get Started", id="get_started", classes="button_widget"),
            Button("Exit", id="exit", classes="button_widget"),
            classes="home_screen_container",
        )
        
    @on(Button.Pressed)
    def button_pressed_handler(self, event: Button.Pressed) -> None:
        if event.button.id == "get_started":
            self.app.push_screen(ChatScreen())
        elif event.button.id == "exit":
            self.app.exit()
            
            
class ChatScreen(Screen):
    
    def compose(self) -> ComposeResult:
        yield Header(
            show_clock = True,
            icon = "💬"
        )
        yield Footer(
            show_command_palette = False
        )
        yield Vertical(
            RichLog(classes="richlog_widget"),
            Input(placeholder="Enter chat", classes="input_widget"),
            classes="vertical_layout"
        )
                
    @on(Input.Submitted)
    def input_submitted_handler(self, event: Input.Submitted):
        log = self.query_one(RichLog)
        log.write(f"me: {event.value}")
        input = self.query_one(Input)
        input.value = ""    
    


class ChatApp(App):
    CSS_PATH = "chat.css"
    
    def on_mount(self) -> None:
        self.app.push_screen(HomeScreen())
        self.title = "Terminal-based chat with Kafka and Python"


if __name__  == "__main__":
    app=ChatApp()
    app.run()