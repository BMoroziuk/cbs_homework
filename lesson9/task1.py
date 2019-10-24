class Editor:
    def view_document(self):
        print('DOCUMENT CONTENT')

    def edit_document(self):
        print('Show me your money!')


class ProEditor(Editor):
    def edit_document(self):
        print('Ok, you can edit, a little.')


key = input('Enter key: ')

if key == '$$$':
    proggram = ProEditor()
else:
    proggram = Editor()

proggram.view_document()
proggram.edit_document()
