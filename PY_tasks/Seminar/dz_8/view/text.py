main_menu = '''
        Hauptmenü
    1. Datei öffnen
    2. Datei speichern
    3. Alle Kontakte anzeigen
    4. Neuen Kontakt erstellen
    5. Kontakt suchen
    6. Kontakt bearbeiten
    7. Kontakt löschen
    8. Enden
    '''

menu_choice = 'Menüpunkt auswählen: '
input_error = 'alsche Eingabe. Geben Sie 1 bis 8 ein'
book_error = 'Telefonbuch leer oder Datei nicht geöffnet'

open_successful = 'Telefonbuch wurde erfolgreich geöffnet'

input_new_contact = 'Neue Kontaktdetails eingeben'
new_contact = ['Kontaktname eingeben: ', 'Telefonnummer eingeben: ', 'Kommentar eingeben: ']
search_word = 'Suchbegriff eingeben: '
input_index = 'Geben Sie den Index des zu ändernden Kontakts ein: '
input_change_contact = 'Geben Sie die Details des zu ändernden Kontakts ein oder geben Sie? ein, um ihn unverändert zu lassen: '

def contact_saved(name: str):
    return f'Der Kontakt {name} wurde erfolgreich gespeichert'

def contact_changed(name: str):
    return f'Kontakt {name} erfolgreich geändert'