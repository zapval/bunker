import command_system
import keyb

def hello():
    message = 'Привет!\nДавай сыграем с тобой в бункер...\n По всем вопросам и предложениям пиши создателю -- @zapeka_infinity (Валентину Запеке)'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Бункер роль', color = 'primary')]
            ]
            }


    return message, attachment, keyboard

hello_command = command_system.Command()

hello_command.keys = ['[club194336319|@zapekabot] меню', 'меню', 'Начать', 'помощь', 'бункер']
hello_command.process = hello
