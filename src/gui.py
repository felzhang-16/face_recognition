import dearpygui.dearpygui as dpg
from src.comm_def import user_data, ORIGIN_PATH, DESTINATION_PATH
from src.processor import handle_known_picture, process_pictures_with_mp, collect_picture
from multiprocessing import Manager


def set_origin_path(sender):
    user_data.origin_path = dpg.get_value(sender) # validate done once set value


def set_destination_path(sender):
    user_data.destination_path = dpg.get_value(sender)


def main_process(*args):
    with Manager() as manager:
        mp_origin_pics = manager.list()
        mp_done_pics = manager.list()
        collect_picture(mp_origin_pics)
        handle_known_picture()
        process_pictures_with_mp(mp_origin_pics, mp_done_pics)


if __name__ == '__main__':
    dpg.create_context()
    with dpg.window(width=700):
        input_origin_path = dpg.add_input_text(
            label="origin path",
            default_value=ORIGIN_PATH,
            callback=set_origin_path
        )
        input_dest_path = dpg.add_input_text(
            label="destination path",
            default_value=DESTINATION_PATH,
            callback=set_destination_path
        )
        dpg.add_progress_bar(label='progress', tag='progress')
        dpg.add_button(label='start', callback=main_process)

    dpg.create_viewport(title='Custom Title', width=800, height=300)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
