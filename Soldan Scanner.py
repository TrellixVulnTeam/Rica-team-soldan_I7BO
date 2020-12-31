import subprocess
import webbrowser as wb
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup


##############example of a console command run via python. this reads out the model of a USB stick.
######### just change the string in the line cmd= .. or in the Popen strings.
# def model_USB(self, blockdev):
#     cmd = "udevadm info --query=all --name=/dev/{0} ".format(blockdev)  # want to find the model number
#     p1 = Popen(shlex.split(cmd), stdout=PIPE)
#     p2 = Popen(["grep", "ID_MODEL"], stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
#     p3 = Popen(["grep", "-v", "ID_MODEL_ENC"], stdin=p2.stdout, stdout=PIPE, stderr=PIPE)
#     output, err = p3.communicate()
#     return output.decode('ascii')[12:-1]


class SoldanScanner(App):

    def do_quit_button(self, obj):
        quit()
    def report(self, instance):
        #print("hi")
        popup = Popup(title='Test popup',
            content = Label(text='Hello world'),
            size_hint = (None, None), size = (400, 400),
            auto_dismiss = True)
        popup.open()
        subprocess.call('net user | find "Administrator"', shell=True)
        #regex : (?<=Administrator).*(?<=^\S*\s+)\S+ , need to get rid of first whitespaces

    def do_nessus_install_button(self, instance):
        wb.open("https://de.tenable.com/products/nessus")

    def do_nessus_button(self, instance):
        wb.open("https://localhost:8834/")

    def build(self):
        layout = GridLayout(cols=2, row_force_default=True, row_default_height=100)

        report_button = Button(text="Show report", pos=(300, 350), size_hint=(.10, .10))
        report_button.bind(on_press=self.report)
        email_button = Button(text="Check email", pos=(100, 350), size_hint=(.10, .10))
        kismet_button = Button(text="Start Kismet", pos=(100, 350), size_hint=(.10, .10))
        nessus_install_button = Button(text="Install Nessus", pos=(100, 350), size_hint=(.10, .10))
        nessus_install_button.bind(on_press = self.do_nessus_install_button)
        nessus_button = Button(text="Start Nessus", pos=(100, 350), size_hint=(.10, .10))
        nessus_button.bind(on_press = self.do_nessus_button)
        av_button = Button(text="Start Antivirus", pos=(100, 350), size_hint=(.10, .10))
        quit_button = Button(text="Quit", pos=(100, 350), size_hint=(.10, .10))
        quit_button.bind(on_press=self.do_quit_button)

        for but in [report_button, email_button, kismet_button, nessus_button, nessus_install_button, av_button, quit_button]:
            layout.add_widget(but)

        return layout


SoldanScanner().run()