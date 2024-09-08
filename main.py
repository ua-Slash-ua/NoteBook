import flet as ft


from recording_notes import RecordingNote, ShowNotes





def main(page: ft.Page):
    page.window.width = 600
    page.window.height = 600
    page.window.top = 225
    page.window.left = 600
    page.title = 'NoteBook'
    win_add_title = ft.TextField(label='Title',max_length=30)
    win_add_text = ft.TextField(label='Descriptions',multiline=True, min_lines=1, max_lines=10)
    content_notes = ft.Column()
    show_notes = ShowNotes()

    def update_note():
        content_notes.controls.clear()  # Очищуємо список нотаток перед оновленням
        notes_all = show_notes.return_all_data()
        for n in notes_all:
            content_notes.controls.append(create_tab_note(n[0], n[2]))  # Створюємо нові таби для нотаток
        page.update()

    def delete_note(num_del):
        print(num_del)
        content_notes.controls.clear()
        content_notes.update()
        page.update()  # Оновлюємо сторінку
        show_notes.delete_note(num_del)  # Видаляємо нотатку з файлу
        update_note()  # Оновлюємо список нотаток
        page.update()  # Оновлюємо сторінку

    def create_tab_note(num_note, title_note):
        # Створюємо рядок з номером і назвою нотатки та кнопкою видалення
        note = ft.Row([
            ft.Text(value=num_note),
            ft.Text(value=title_note),
            ft.TextButton(text='del', on_click=lambda e: delete_note(num_note[:len(num_note)-1]))  # Прив'язуємо функцію видалення
        ])
        return note
    def remember_note(e):
        note = RecordingNote(win_add_title.value,win_add_text.value)
        note.create_note()
        num_note, title_note = note.return_data_note()
        new_note = create_tab_note(num_note,title_note)
        content_notes.controls.append(new_note)
        win_add.open = False
        win_add_title.label = 'Title'
        win_add_text.label = 'Descriptions'

        page.update()

    win_add = ft.AlertDialog(
        title=ft.Text(value='Create a new note'),
        content=ft.Container(ft.Column([
            win_add_title,
            win_add_text,
            ft.TextButton(text='Add note', on_click=remember_note)
        ]),
            width=300,
            height=400
        )
    )
    def add_note(e):
        page.overlay.append(win_add)
        win_add.open = True
        page.update()

    btn_add = ft.TextButton(text='ADD', on_click=add_note)
    update_note()
    page.add(ft.Column([ft.Container(content_notes), btn_add]))
if __name__ == '__main__':
    ft.app(target = main)
