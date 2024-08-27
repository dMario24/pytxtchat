from textual import on
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Container, Vertical, Center, Middle
from textual.widgets import (
  Input, RichLog, Button, Sparkline,
  Header, Footer
)
from textual.worker import Worker
from textual import work

from pytxtchat.kafka.producer import create_producer
from pytxtchat.kafka.consumer import create_consumer

from textual.reactive import reactive

from rich.text import Text
from rich.panel import Panel

import random

# 
CHAT_ROOM = ""
CHAT_ID = ""
CHAT_SERVERS=""

class HomeScreen(Screen):
    
    def compose(self) -> ComposeResult:
        yield Container(
            Input(placeholder="Chat Room", classes="chat_setting_input_widget", id="chat_room_input_widget"),
            Input(placeholder="Chat ID", classes="chat_setting_input_widget", id="chat_id_input_widget"),
            Input(placeholder="Chat Server A:9092,B:9092", classes="chat_setting_input_widget", id="chat_servers_input_widget"),
            Button("Jumping into the world", id="get_started", classes="button_widget"),
            Button("Backward step", id="exit", classes="button_widget"),
            classes="home_screen_container",
        )
        
    @on(Button.Pressed)
    def button_pressed_handler(self, event: Button.Pressed) -> None:
        if event.button.id == "get_started":
            global CHAT_ROOM, CHAT_ID, CHAT_SERVERS
            CHAT_ROOM = self.query_one("#chat_room_input_widget", Input).value
            CHAT_ID = self.query_one("#chat_id_input_widget", Input).value
            CHAT_SERVERS = self.query_one("#chat_servers_input_widget", Input).value.split(",")
            self.app.push_screen(ChatScreen())
        elif event.button.id == "exit":
            self.app.exit()
            
            
class ChatScreen(Screen):
    def on_mount(self) -> None:
        
        self.load_msg()
        self.notify(
            message="You have entered successfully."
            "[b]conversation[/b] and [i][b]communication[/b][/i] are alive!",
            title="Welcome Chat World 🥳",
            severity="information", #warning #error
        )
        self.kafka_producer = create_producer(CHAT_SERVERS)
        self.screen.styles.border = ("heavy", "white")

    def compose(self) -> ComposeResult:
        yield Header(
            show_clock = True,
            icon = "💬"
        )
        yield Footer(
            show_command_palette = False
        )
        yield Vertical(
            RichLog(classes="chat_history_widget", min_width=self.app.size.width - 6),
            Input(placeholder="Enter chat", classes="chat_input_widget"),
            classes="vertical_layout"
        )

    @on(Input.Submitted)
    def input_submitted_handler(self, event: Input.Submitted):
        
        msg = {
            "to" : CHAT_ID,
            "msg" : event.value
        }

        self.kafka_producer.send(topic=CHAT_ROOM, value=msg)
        self.kafka_producer.flush()

        input = self.query_one(Input)
        input.value = "" 

    @work(exclusive=True, thread=True)
    def load_msg(self) -> None:
        """https://textual.textualize.io/guide/workers"""
        consumer = create_consumer(topic_name=CHAT_ROOM, bootstrap_server_list=CHAT_SERVERS)

        chat_history_widget = self.query_one(RichLog)
        for m in consumer:
            data = m.value
            to = data['to']
            msg = data['msg']

            if to == CHAT_ID:
                justify_value = "right"
                style_value = "bold white"
            else:
                justify_value = "left"
                style_value = "bold green"
 
            text_prod = Text(f"{to}: {msg}", style=style_value, justify=justify_value)
            chat_history_widget.write(text_prod)


class ChatApp(App):
    CSS_PATH = "chat.tcss"
    
    def on_mount(self) -> None:
        self.app.push_screen(HomeScreen())
        self.title = "Terminal-based chat with Kafka and Python"

if __name__  == "__main__":
    app=ChatApp()
    app.run()